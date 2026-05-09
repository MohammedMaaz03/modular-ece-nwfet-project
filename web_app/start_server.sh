#!/bin/bash

echo "========================================"
echo "   NWFET Energy Band Diagram Server"
echo "========================================"
echo ""
echo "Starting server..."
echo ""

cd "$(dirname "$0")"

python manage.py runserver --host localhost --port 8000

echo "Server stopped."
