#!/usr/bin/env python3
"""
NWFET Energy Band Diagram Program - Server Application.
Similar to Django's manage.py runserver functionality.
"""

import os
import sys
import json
import hashlib
import sqlite3
import threading
import time
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path

class DatabaseManager:
    """Handle database operations for users and sessions."""
    
    def __init__(self, db_path='database/nwfet_app.db'):
        """Initialize database manager with proper path resolution."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, db_path)
        self.init_database()
    
    def init_database(self):
        """Initialize database tables with proper error handling."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                self._create_users_table(cursor)
                self._create_sessions_table(cursor)
                self._create_user_preferences_table(cursor)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise
    
    def _create_users_table(self, cursor):
        """Create users table."""
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        """)
    
    def _create_sessions_table(self, cursor):
        """Create sessions table."""
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
    
    def _create_user_preferences_table(self, cursor):
        """Create user preferences table."""
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_preferences (
                user_id INTEGER PRIMARY KEY,
                default_material TEXT DEFAULT 'Si',
                default_dielectric TEXT DEFAULT 'SiO2',
                default_gate_type TEXT DEFAULT 'pi',
                theme TEXT DEFAULT 'light',
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
    
    def create_user(self, username, email, password, full_name=None):
        """Create a new user with proper error handling."""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (username, email, password_hash, full_name)
                    VALUES (?, ?, ?, ?)
                """, (username, email, password_hash, full_name))
                
                user_id = cursor.lastrowid
                cursor.execute("""
                    INSERT INTO user_preferences (user_id)
                    VALUES (?)
                """, (user_id,))
                
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
        except sqlite3.Error as e:
            print(f"User creation error: {e}")
            return False
    
    def authenticate_user(self, username, password):
        """Authenticate user credentials with secure password verification."""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, username, email, full_name FROM users
                    WHERE username = ? AND password_hash = ? AND is_active = 1
                """, (username, password_hash))
                
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Authentication error: {e}")
            return None
    
    def create_session(self, user_id):
        """Create a new session for user with secure session ID generation."""
        session_id = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()
        expires_at = datetime.now() + timedelta(hours=24)
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO sessions (id, user_id, expires_at)
                    VALUES (?, ?, ?)
                """, (session_id, user_id, expires_at))
                
                conn.commit()
                return session_id
        except sqlite3.Error as e:
            print(f"Session creation error: {e}")
            return None
    
    def validate_session(self, session_id):
        """Validate session and return user info with proper error handling."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT u.id, u.username, u.email, u.full_name
                    FROM sessions s
                    JOIN users u ON s.user_id = u.id
                    WHERE s.id = ? AND s.expires_at > ? AND u.is_active = 1
                """, (session_id, datetime.now()))
                
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Session validation error: {e}")
            return None
    
    def logout(self, session_id):
        """Remove session with proper error handling."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Logout error: {e}")

class NWFETRequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests for the NWFET application"""
    
    def __init__(self, *args, **kwargs):
        self.db = DatabaseManager()
        self.static_files = {
            '/': 'templates/dashboard.html',
            '/login': 'templates/login.html',
            '/signup': 'templates/signup.html',
            '/style.css': 'css/style.css',
            '/main.js': 'js/main.js',
            '/favicon.ico': 'assets/favicon.ico'
        }
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Route handling
        if path == '/':
            # Redirect to dashboard if authenticated, otherwise to login
            session_id = self.get_session_id()
            if self.db.validate_session(session_id):
                self.serve_file('templates/dashboard.html', 'text/html')
            else:
                self.serve_file('templates/login.html', 'text/html')
        elif path == '/login':
            self.serve_file('templates/login.html', 'text/html')
        elif path == '/signup':
            self.serve_file('templates/signup.html', 'text/html')
        elif path == '/dashboard':
            self.require_auth()
            self.serve_file('templates/dashboard.html', 'text/html')
        elif path == '/logout':
            self.logout()
        elif path.startswith('/api/'):
            self.handle_api_request()
        elif path in self.static_files:
            content_type = self.get_content_type(self.static_files[path])
            self.serve_file(self.static_files[path], content_type)
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/api/login':
            self.handle_login()
        elif path == '/api/signup':
            self.handle_signup()
        elif path == '/api/logout':
            self.handle_logout()
        elif path == '/api/calculate':
            self.require_auth()
            self.handle_calculation()
        elif path == '/api/drain_iv':
            self.require_auth()
            self.handle_drain_iv()
        elif path == '/api/transfer_iv':
            self.require_auth()
            self.handle_transfer_iv()
        else:
            self.send_error(404)
    
    def serve_file(self, file_path, content_type):
        """Serve static files"""
        try:
            # Convert relative path to absolute path
            if not os.path.isabs(file_path):
                # Get the directory where manage.py is located
                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, file_path)
            
            with open(file_path, 'rb') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            self.send_error(404)
        except Exception as e:
            print(f"Error serving file {file_path}: {e}")
            self.send_error(500)
    
    def get_content_type(self, file_path):
        """Get content type based on file extension"""
        if file_path.endswith('.html'):
            return 'text/html'
        elif file_path.endswith('.css'):
            return 'text/css'
        elif file_path.endswith('.js'):
            return 'application/javascript'
        elif file_path.endswith('.ico'):
            return 'image/x-icon'
        else:
            return 'application/octet-stream'
    
    def get_session_id(self):
        """Get session ID from cookies"""
        cookie_header = self.headers.get('Cookie')
        if cookie_header:
            cookies = {}
            for cookie in cookie_header.split(';'):
                if '=' in cookie:
                    name, value = cookie.strip().split('=', 1)
                    cookies[name] = value
            return cookies.get('session_id')
        return None
    
    def require_auth(self):
        """Require authentication"""
        session_id = self.get_session_id()
        if not session_id or not self.db.validate_session(session_id):
            self.send_response(302)
            self.send_header('Location', '/login')
            self.end_headers()
            return False
        return True
    
    def handle_login(self):
        """Handle login request"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))
        
        start_time = time.time()
        
        username = data.get('username', [''])[0]
        password = data.get('password', [''])[0]
        
        user = self.db.authenticate_user(username, password)
        
        if user:
            session_id = self.db.create_session(user[0])
            
            # Set session cookie
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Set-Cookie', f'session_id={session_id}; Path=/; HttpOnly; Max-Age=86400')
            self.end_headers()
            
            response = {
                'success': True,
                'user': {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'full_name': user[3]
                }
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {'success': False, 'error': 'Invalid credentials'}
            self.wfile.write(json.dumps(response).encode())
        
        print(f"Login request took {time.time() - start_time:.3f}s")
    
    def handle_signup(self):
        """Handle signup request"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))
        
        start_time = time.time()
        
        username = data.get('username', [''])[0]
        email = data.get('email', [''])[0]
        password = data.get('password', [''])[0]
        full_name = data.get('full_name', [''])[0]
        
        if self.db.create_user(username, email, password, full_name):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {'success': True, 'message': 'User created successfully'}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {'success': False, 'error': 'Username or email already exists'}
            self.wfile.write(json.dumps(response).encode())
        
        print(f"Signup request took {time.time() - start_time:.3f}s")
    
    def handle_logout(self):
        """Handle logout request"""
        session_id = self.get_session_id()
        if session_id:
            self.db.logout(session_id)
        
        self.send_response(302)
        self.send_header('Location', '/login')
        self.send_header('Set-Cookie', 'session_id=; Path=/; HttpOnly; Max-Age=0')
        self.end_headers()
    
    def handle_calculation(self):
        """Handle band diagram calculation"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))
        
        # Extract parameters
        params = {
            'gateType': data.get('gateType', ['pi'])[0],
            'material': data.get('material', ['Si'])[0],
            'dielectric': data.get('dielectric', ['SiO2'])[0],
            'oxideThickness': float(data.get('oxideThickness', ['2'])[0]),
            'nanowireDiameter': float(data.get('nanowireDiameter', ['10'])[0]),
            'channelLength': float(data.get('channelLength', ['20'])[0]),
            'dopingConcentration': float(data.get('dopingConcentration', ['1e18'])[0]),
            'gateVoltage': float(data.get('gateVoltage', ['0'])[0]),
            'drainVoltage': float(data.get('drainVoltage', ['0.1'])[0]),
            'temperature': float(data.get('temperature', ['300'])[0])
        }
        
        # Perform calculation (simplified for demo)
        results = self.perform_calculation(params)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(results).encode())
    
    def handle_drain_iv(self):
        """Handle drain IV calculation"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))
        
        # Extract parameters
        params = {
            'gateType': data.get('gateType', ['pi'])[0],
            'material': data.get('material', ['Si'])[0],
            'dielectric': data.get('dielectric', ['SiO2'])[0],
            'oxideThickness': float(data.get('oxideThickness', ['2'])[0]),
            'nanowireDiameter': float(data.get('nanowireDiameter', ['10'])[0]),
            'channelLength': float(data.get('channelLength', ['20'])[0]),
            'dopingConcentration': float(data.get('dopingConcentration', ['1e18'])[0]),
            'gateVoltage': float(data.get('gateVoltage', ['0'])[0]),
            'drainVoltage': float(data.get('drainVoltage', ['0.1'])[0]),
            'temperature': float(data.get('temperature', ['300'])[0])
        }
        
        # Perform calculation
        results = self.perform_drain_iv(params)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(results).encode())
    
    def handle_transfer_iv(self):
        """Handle transfer IV calculation"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))
        
        # Extract parameters
        params = {
            'gateType': data.get('gateType', ['pi'])[0],
            'material': data.get('material', ['Si'])[0],
            'dielectric': data.get('dielectric', ['SiO2'])[0],
            'oxideThickness': float(data.get('oxideThickness', ['2'])[0]),
            'nanowireDiameter': float(data.get('nanowireDiameter', ['10'])[0]),
            'channelLength': float(data.get('channelLength', ['20'])[0]),
            'dopingConcentration': float(data.get('dopingConcentration', ['1e18'])[0]),
            'gateVoltage': float(data.get('gateVoltage', ['0'])[0]),
            'drainVoltage': float(data.get('drainVoltage', ['0.1'])[0]),
            'temperature': float(data.get('temperature', ['300'])[0])
        }
        
        # Perform calculation
        results = self.perform_transfer_iv(params)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(results).encode())
    
    def perform_calculation(self, params):
        """Perform band structure calculation"""
        # Material properties
        material_props = {
            'Si': {'bandGap': 1.12, 'electronAffinity': 4.05},
            'Ge': {'bandGap': 0.66, 'electronAffinity': 4.0},
            'GaAs': {'bandGap': 1.42, 'electronAffinity': 4.07},
            'InAs': {'bandGap': 0.36, 'electronAffinity': 4.9}
        }
        
        # Get material properties
        props = material_props.get(params.get('material', 'Si'), material_props['Si'])
        band_gap = props['bandGap']
        electron_affinity = props['electronAffinity']
        
        # Adjust based on parameters
        gate_voltage = params.get('gateVoltage', 0)
        temperature = params.get('temperature', 300)
        drain_voltage = params.get('drainVoltage', 0.1)
        gate_type = params.get('gateType', 'pi')
        
        # Fermi level shift due to gate voltage, drain voltage, and temperature (dramatically amplified)
        fermi_shift = 1.0 * gate_voltage + 0.5 * drain_voltage - 0.05 * (temperature - 300)
        fermi_level = electron_affinity + band_gap/2 + fermi_shift
        
        positions = [x * 0.1 for x in range(-50, 51)]  # -5nm to 5nm
        
        # Band curvature depends on gate type (Pi vs Omega) - extreme difference
        curvature_factor = 0.05 if gate_type == 'pi' else 0.25
        
        # Conduction band with dramatic shifts
        conduction_band = [
            electron_affinity + band_gap + curvature_factor * (x/5)**2 + 0.1 * (temperature - 300) + 0.5 * gate_voltage
            for x in positions
        ]
        
        # Valence band
        valence_band = [cb - band_gap for cb in conduction_band]
        
        # Make energies relative to Fermi level for clear visualization
        conduction_band_relative = [cb - fermi_level for cb in conduction_band]
        valence_band_relative = [vb - fermi_level for vb in valence_band]
        fermi_level_relative = 0.0
        
        return {
            'positions': positions,
            'conductionBand': conduction_band_relative,
            'valenceBand': valence_band_relative,
            'fermiLevel': fermi_level_relative,
            'parameters': params,
            'timestamp': datetime.now().isoformat()
        }
    
    def perform_drain_iv(self, params):
        """Perform drain IV calculation"""
        v_gs = float(params.get('gateVoltage', 0))
        v_ds_list = [i * 0.1 for i in range(21)]  # 0 to 2V
        ids_list = []
        
        v_t = 0.3
        mu = 0.1
        c_ox = 1e-6
        w_l = 10
        
        for v_ds in v_ds_list:
            if v_gs > v_t:
                if v_ds < v_gs - v_t:
                    i_d = mu * c_ox * w_l * (v_gs - v_t - v_ds/2) * v_ds
                else:
                    i_d = mu * c_ox * w_l * (v_gs - v_t)**2 / 2
            else:
                i_d = 0
            ids_list.append(i_d)
        
        return {
            'vds': v_ds_list,
            'ids': ids_list,
            'params': params,
            'timestamp': datetime.now().isoformat()
        }
    
    def perform_transfer_iv(self, params):
        """Perform transfer IV calculation"""
        v_ds = float(params.get('drainVoltage', 0.1))
        v_gs_list = [i * 0.1 - 1 for i in range(21)]  # -1 to 1V
        ids_list = []
        
        v_t = 0.3
        mu = 0.1
        c_ox = 1e-6
        w_l = 10
        
        for v_gs in v_gs_list:
            if v_gs > v_t:
                if v_ds < v_gs - v_t:
                    i_d = mu * c_ox * w_l * (v_gs - v_t - v_ds/2) * v_ds
                else:
                    i_d = mu * c_ox * w_l * (v_gs - v_t)**2 / 2
            else:
                i_d = 0
            ids_list.append(i_d)
        
        return {
            'vgs': v_gs_list,
            'ids': ids_list,
            'params': params,
            'timestamp': datetime.now().isoformat()
        }
    
    def handle_api_request(self):
        """Handle API requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/api/user':
            self.require_auth()
            self.get_user_info()
        elif path == '/api/materials':
            self.get_materials()
        else:
            self.send_error(404)
    
    def get_user_info(self):
        """Get current user information"""
        session_id = self.get_session_id()
        user = self.db.validate_session(session_id)
        
        if user:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'full_name': user[3]
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(401)
            self.end_headers()
    
    def get_materials(self):
        """Get available materials"""
        materials = {
            'semiconductors': [
                {'name': 'Si', 'bandGap': 1.12, 'electronAffinity': 4.05},
                {'name': 'Ge', 'bandGap': 0.66, 'electronAffinity': 4.0},
                {'name': 'GaAs', 'bandGap': 1.42, 'electronAffinity': 4.07},
                {'name': 'InAs', 'bandGap': 0.36, 'electronAffinity': 4.9}
            ],
            'dielectrics': [
                {'name': 'SiO2', 'k': 3.9, 'barrierHeight': 3.2},
                {'name': 'Al2O3', 'k': 9.0, 'barrierHeight': 2.8},
                {'name': 'HfO2', 'k': 25.0, 'barrierHeight': 1.5},
                {'name': 'ZrO2', 'k': 25.0, 'barrierHeight': 1.4},
                {'name': 'La2O3', 'k': 30.0, 'barrierHeight': 2.1}
            ]
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(materials).encode())

class NWFETServer:
    """Main server class"""
    
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.server = None
        self.server_thread = None
    
    def start(self):
        """Start the server"""
        try:
            self.server = HTTPServer((self.host, self.port), NWFETRequestHandler)
            
            print(f"""
========================================
   NWFET Energy Band Diagram Server
========================================
Server running at: http://{self.host}:{self.port}
Access URL: http://127.0.0.1:{self.port}

Commands:
  - Ctrl+C to stop server
  - Access in browser with the URL above

Features:
  - User authentication (login/signup)
  - Session management
  - Band diagram calculations
  - Material database
  - Export capabilities
========================================
            """)
            
            # Start server in a separate thread
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            return True
            
        except Exception as e:
            print(f"Error starting server: {e}")
            return False
    
    def stop(self):
        """Stop the server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("\nServer stopped.")

def main():
    """Main function - similar to Django's manage.py"""
    import argparse
    
    parser = argparse.ArgumentParser(description='NWFET Energy Band Diagram Server')
    parser.add_argument('command', choices=['runserver', 'createuser'], 
                       help='Command to execute')
    parser.add_argument('--host', default='localhost', 
                       help='Host to bind to (default: localhost)')
    parser.add_argument('--port', type=int, default=8000, 
                       help='Port to bind to (default: 8000)')
    parser.add_argument('--username', help='Username for createuser command')
    parser.add_argument('--email', help='Email for createuser command')
    parser.add_argument('--password', help='Password for createuser command')
    parser.add_argument('--fullname', help='Full name for createuser command')
    
    args = parser.parse_args()
    
    if args.command == 'runserver':
        print("Starting NWFET Energy Band Diagram Server...")
        server = NWFETServer(args.host, args.port)
        
        if server.start():
            try:
                # Keep server running
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nShutting down server...")
                server.stop()
    
    elif args.command == 'createuser':
        if not all([args.username, args.email, args.password]):
            print("Error: --username, --email, and --password are required for createuser")
            return
        
        db = DatabaseManager()
        if db.create_user(args.username, args.email, args.password, args.fullname):
            print(f"User '{args.username}' created successfully!")
        else:
            print("Error: Username or email already exists")

if __name__ == '__main__':
    main()
