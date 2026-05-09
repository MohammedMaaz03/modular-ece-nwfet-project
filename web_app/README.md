# NWFET Energy Band Diagram Program

A comprehensive web application for calculating and visualizing energy band diagrams of Pi-Gate and Omega-Gate Nanowire Field Effect Transistors (NWFETs).

## 🎯 Features

### **Core Functionality**
- **Energy Band Diagrams**: Interactive visualization of conduction and valence bands
- **Wave Function Analysis**: Probability density distributions for quantum states
- **Electric Field Mapping**: Field distribution across the nanowire
- **Quantum State Calculations**: Discrete energy levels and occupancy
- **Material Database**: Comprehensive properties for semiconductors and dielectrics

### **Supported Materials**
- **Semiconductors**: Si, Ge, GaAs, InAs
- **Dielectrics**: SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃
- **Gate Architectures**: Pi-Gate (partial wrap) and Omega-Gate (full wrap)

### **Advanced Calculations**
- Quantum mechanical band structure
- Schrödinger equation solutions
- Poisson equation for electric field
- Temperature-dependent effects
- Quantum confinement in nanowires

## 🚀 Quick Start

1. **Open the Application**: Navigate to `web_app/index.html` in your browser
2. **Select Gate Type**: Choose between Pi-Gate and Omega-Gate
3. **Configure Materials**: Select semiconductor and dielectric materials
4. **Set Device Parameters**: Adjust dimensions, doping, and bias conditions
5. **Calculate**: Click "Calculate Band Diagram" to generate results
6. **Explore Results**: Switch between tabs to view different analyses

## 📁 Project Structure

```
web_app/
├── index.html              # Main application page
├── css/
│   └── style.css          # Complete styling
├── js/
│   └── main.js            # Core JavaScript functionality
├── assets/               # Images and icons
├── lib/                  # External libraries
└── README.md             # This file
```

## 🎮 Usage Instructions

### **Parameter Configuration**

#### **Gate Architecture**
- **Pi-Gate**: Partial wrap-around gate with moderate electrostatic control
- **Omega-Gate**: Full wrap-around gate with superior control

#### **Material Properties**
- **Gate Material**: Affects electron affinity and band gap
- **Dielectric Material**: Determines barrier height and capacitance
- **Oxide Thickness**: Influences gate control and quantum tunneling

#### **Device Dimensions**
- **Nanowire Diameter**: Controls quantum confinement effects
- **Channel Length**: Affects transport properties
- **Doping Concentration**: Determines Fermi level position

#### **Bias Conditions**
- **Gate Voltage**: Controls band bending and carrier density
- **Drain Voltage**: Sets operating conditions
- **Temperature**: Affects thermal broadening and carrier distribution

### **Result Analysis**

#### **Band Diagram Tab**
- Conduction band edge
- Valence band edge
- Fermi level position
- Band bending effects

#### **Wave Functions Tab**
- Probability density |ψ|²
- Multiple quantum states (n=1,2,3,4)
- Energy level annotations

#### **Electric Field Tab**
- Field distribution across nanowire
- Gate voltage effects
- Peak field locations

#### **Quantum States Tab**
- Discrete energy levels
- Occupation probabilities
- Degeneracy information

#### **Parameters Tab**
- Calculated device parameters
- Material properties
- Electrical characteristics

## 🔬 Physics Models

### **Band Structure Calculations**
The application solves the time-independent Schrödinger equation for cylindrical quantum wires:

$$-\frac{\hbar^2}{2m^*} \nabla^2 \psi(r) + V(r)\psi(r) = E\psi(r)$$

### **Quantum Confinement**
Energy levels for cylindrical geometry:

$$E_n = \frac{\hbar^2\pi^2n^2}{2m^*R^2}$$

where R is the nanowire radius.

### **Band Bending**
Electrostatic potential distribution:

$$V(x) = V_{max} \left(1 - \frac{x^2}{R^2}\right)$$

### **Electric Field**
Field distribution from Poisson equation:

$$E(x) = -\frac{dV}{dx}$$

## 🛠️ Technical Implementation

### **Frontend Technologies**
- **HTML5**: Semantic structure and modern elements
- **CSS3**: Responsive design with animations
- **JavaScript ES6+**: Modern JavaScript features
- **Plotly.js**: Interactive scientific plotting
- **Font Awesome**: Professional icons

### **Key Algorithms**
- **Numerical Integration**: For solving differential equations
- **Matrix Diagonalization**: For quantum state calculations
- **Finite Difference Methods**: For field calculations
- **Monte Carlo**: For carrier statistics

### **Data Management**
- **Local Storage**: Parameter persistence
- **JSON Export**: Structured data export
- **CSV Export**: Tabular data format
- **PNG/SVG Export**: High-quality figures

## 📊 Export Options

### **Image Export**
- **PNG**: High-resolution raster images
- **SVG**: Scalable vector graphics
- **Custom Sizing**: Publication-ready dimensions

### **Data Export**
- **JSON**: Complete calculation results
- **CSV**: Tabular data for analysis
- **Metadata**: Parameter information included

## 🎨 Customization

### **Adding New Materials**
To add new semiconductor materials, update the `materialProperties` object in `js/main.js`:

```javascript
'NewMaterial': {
    electronAffinity: 4.2,
    bandGap: 1.5,
    effectiveMass: 0.15,
    dielectricConstant: 12.0
}
```

### **Modifying Calculations**
Core physics functions are modular and can be extended:
- `calculateConductionBand()`
- `calculateWaveFunctions()`
- `calculateElectricField()`

### **UI Customization**
- Modify `css/style.css` for visual changes
- Update `index.html` for layout modifications
- Add new tabs in the results section

## 🔧 Development

### **Local Development**
1. Clone the repository
2. Open `web_app/index.html` in a modern browser
3. No build process required - runs directly

### **Browser Compatibility**
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### **Performance Optimization**
- Lazy loading of calculation results
- Efficient numerical algorithms
- Optimized plotting with Plotly.js
- Minimal memory footprint

## 📚 Educational Value

### **Learning Objectives**
- Understand quantum confinement in nanowires
- Explore gate architecture effects on band structure
- Analyze material properties impact on device behavior
- Visualize quantum mechanical wave functions

### **Teaching Applications**
- Classroom demonstrations
- Student assignments
- Research projects
- Publication figure generation

## 🤝 Contributing

### **Bug Reports**
- Open an issue with detailed description
- Include browser and OS information
- Provide steps to reproduce

### **Feature Requests**
- Propose new physics models
- Suggest UI improvements
- Request additional materials

### **Code Contributions**
- Follow existing code style
- Add comments for complex calculations
- Include unit tests for new functions

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Quantum mechanical models based on standard semiconductor physics
- Material properties from standard references
- Plotly.js for excellent scientific plotting
- Font Awesome for professional icons

## 📞 Contact

For questions, suggestions, or collaborations:
- Email: nwfet-simulation@example.com
- GitHub: [repository link]
- Documentation: [docs link]

---

**Note**: This application is for educational and research purposes. Results should be validated with experimental data for practical applications.
