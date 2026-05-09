// NWFET Energy Band Diagram Program - Main JavaScript

// Material properties database
const materialProperties = {
    'Si': {
        electronAffinity: 4.05,
        bandGap: 1.12,
        effectiveMass: 0.26,
        dielectricConstant: 11.7,
        latticeConstant: 5.43,
        density: 2.33
    },
    'Ge': {
        electronAffinity: 4.0,
        bandGap: 0.66,
        effectiveMass: 0.12,
        dielectricConstant: 16.0,
        latticeConstant: 5.66,
        density: 5.32
    },
    'GaAs': {
        electronAffinity: 4.07,
        bandGap: 1.42,
        effectiveMass: 0.067,
        dielectricConstant: 12.9,
        latticeConstant: 5.65,
        density: 5.32
    },
    'InAs': {
        electronAffinity: 4.9,
        bandGap: 0.36,
        effectiveMass: 0.023,
        dielectricConstant: 15.15,
        latticeConstant: 6.06,
        density: 5.67
    }
};

const dielectricProperties = {
    'SiO2': { 
        k: 3.9, 
        barrierHeight: 3.2,
        breakdownField: 10,
        thermalConductivity: 1.4
    },
    'Al2O3': { 
        k: 9.0, 
        barrierHeight: 2.8,
        breakdownField: 8,
        thermalConductivity: 30
    },
    'HfO2': { 
        k: 25.0, 
        barrierHeight: 1.5,
        breakdownField: 6,
        thermalConductivity: 2
    },
    'ZrO2': { 
        k: 25.0, 
        barrierHeight: 1.4,
        breakdownField: 7,
        thermalConductivity: 2
    },
    'La2O3': { 
        k: 30.0, 
        barrierHeight: 2.1,
        breakdownField: 5,
        thermalConductivity: 1.5
    }
};

// Global variables
let currentResults = {};
let calculationHistory = [];
let isCalculating = false;

// Physical constants
const CONSTANTS = {
    h: 6.626e-34,           // Planck constant (J·s)
    hbar: 1.055e-34,        // Reduced Planck constant (J·s)
    q: 1.602e-19,           // Elementary charge (C)
    m0: 9.109e-31,          // Electron rest mass (kg)
    k: 1.381e-23,           // Boltzmann constant (J/K)
    epsilon0: 8.854e-12,    // Vacuum permittivity (F/m)
    pi: Math.PI
};

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    loadSavedParameters();
    updateMaterialInfo();
});

// Event listeners initialization
function initializeEventListeners() {
    // Gate selection
    document.querySelectorAll('.gate-option').forEach(option => {
        option.addEventListener('click', function() {
            selectGate(this);
        });
    });

    // Material selection
    document.getElementById('material').addEventListener('change', function() {
        updateMaterialInfo();
    });

    // Range inputs with real-time updates
    setupRangeInput('oxide-thickness', 'nm');
    setupRangeInput('nanowire-diameter', 'nm');
    setupRangeInput('gate-voltage', 'V');

    // Form validation
    setupFormValidation();

    // Keyboard shortcuts
    setupKeyboardShortcuts();

    // Auto-save
    setupAutoSave();
}

// Gate selection
function selectGate(element) {
    document.querySelectorAll('.gate-option').forEach(opt => opt.classList.remove('selected'));
    element.classList.add('selected');
    
    // Update UI to reflect gate type
    const gateType = element.dataset.gate;
    updateGateInfo(gateType);
    
    // Save to history
    saveToHistory('gate_change', { gateType });
}

// Setup range inputs
function setupRangeInput(inputId, unit) {
    const input = document.getElementById(inputId);
    const display = input.nextElementSibling;
    
    input.addEventListener('input', function() {
        display.textContent = this.value + ' ' + unit;
        updateCalculationsPreview();
    });
}

// Update material information
function updateMaterialInfo() {
    const material = document.getElementById('material').value;
    const dielectric = document.getElementById('dielectric').value;
    
    const matProps = materialProperties[material];
    const dielProps = dielectricProperties[dielectric];
    
    if (matProps && dielProps) {
        // Update display with material properties
        updateMaterialDisplay(matProps, dielProps);
    }
}

// Update gate information
function updateGateInfo(gateType) {
    const gateInfo = {
        'pi': {
            name: 'Pi-Gate',
            description: 'Partial wrap-around gate',
            controlFactor: 0.6,
            fieldEnhancement: 1.0
        },
        'omega': {
            name: 'Omega-Gate',
            description: 'Full wrap-around gate',
            controlFactor: 0.8,
            fieldEnhancement: 1.2
        }
    };
    
    const info = gateInfo[gateType];
    if (info) {
        updateGateDisplay(info);
    }
}

// Main calculation function
async function calculateBandDiagram() {
    if (isCalculating) return;
    
    const button = document.querySelector('.calculate-btn');
    const status = document.getElementById('status');
    const welcomeContent = document.getElementById('welcome-content');
    const resultsContent = document.getElementById('results-content');
    
    try {
        // Set calculating state
        isCalculating = true;
        button.disabled = true;
        button.textContent = '🔄 Calculating...';
        status.className = 'status calculating';
        status.textContent = 'Calculating';
        
        // Show loading
        showLoading();
        
        // Hide welcome, show results
        welcomeContent.style.display = 'none';
        resultsContent.style.display = 'block';
        
        // Get parameters
        const params = getParameters();
        
        // Validate parameters
        if (!validateParameters(params)) {
            throw new Error('Invalid parameters');
        }
        
        // Calculate band structure
        currentResults = await calculateBandStructure(params);
        
        // Update all diagrams
        await updateAllDiagrams(currentResults);
        
        // Update parameters display
        updateParameters(currentResults);
        
        // Save to history
        saveToHistory('calculation', { params, results: currentResults });
        
        // Update UI
        button.disabled = false;
        button.textContent = '🧮 Calculate Band Diagram';
        status.className = 'status complete';
        status.textContent = 'Complete';
        
        // Hide loading
        hideLoading();
        
        // Show success notification
        showNotification('Calculation completed successfully!', 'success');
        
    } catch (error) {
        console.error('Calculation error:', error);
        
        // Update UI for error
        button.disabled = false;
        button.textContent = '🧮 Calculate Band Diagram';
        status.className = 'status ready';
        status.textContent = 'Ready';
        
        // Hide loading
        hideLoading();
        
        // Show error notification
        showNotification('Calculation failed: ' + error.message, 'error');
    } finally {
        isCalculating = false;
    }
}

// Get parameters from form
function getParameters() {
    return {
        gateType: document.querySelector('.gate-option.selected').dataset.gate,
        material: document.getElementById('material').value,
        dielectric: document.getElementById('dielectric').value,
        oxideThickness: parseFloat(document.getElementById('oxide-thickness').value),
        nanowireDiameter: parseFloat(document.getElementById('nanowire-diameter').value),
        channelLength: parseFloat(document.getElementById('channel-length').value),
        dopingConcentration: parseFloat(document.getElementById('doping-concentration').value),
        gateVoltage: parseFloat(document.getElementById('gate-voltage').value),
        drainVoltage: parseFloat(document.getElementById('drain-voltage').value),
        temperature: parseFloat(document.getElementById('temperature').value),
        // Display options
        showEnergyBands: document.querySelector('input[value="show-bands"]').checked,
        showWaveFunctions: document.querySelector('input[value="show-wavefunctions"]').checked,
        showElectricField: document.querySelector('input[value="show-field"]').checked,
        showQuantumStates: document.querySelector('input[value="show-quantum"]').checked
    };
}

// Validate parameters
function validateParameters(params) {
    const errors = [];
    
    if (params.oxideThickness <= 0 || params.oxideThickness > 10) {
        errors.push('Oxide thickness must be between 0.1 and 10 nm');
    }
    
    if (params.nanowireDiameter <= 0 || params.nanowireDiameter > 50) {
        errors.push('Nanowire diameter must be between 1 and 50 nm');
    }
    
    if (params.channelLength <= 0 || params.channelLength > 1000) {
        errors.push('Channel length must be between 1 and 1000 nm');
    }
    
    if (params.dopingConcentration < 1e15 || params.dopingConcentration > 1e20) {
        errors.push('Doping concentration must be between 1e15 and 1e20 cm⁻³');
    }
    
    if (Math.abs(params.gateVoltage) > 5) {
        errors.push('Gate voltage must be between -5 and 5 V');
    }
    
    if (params.temperature < 77 || params.temperature > 500) {
        errors.push('Temperature must be between 77 and 500 K');
    }
    
    if (errors.length > 0) {
        showNotification('Validation errors:\n' + errors.join('\n'), 'error');
        return false;
    }
    
    return true;
}

// Calculate band structure
async function calculateBandStructure(params) {
    const material = materialProperties[params.material];
    const dielectric = dielectricProperties[params.dielectric];
    
    // Generate position array
    const positions = generatePositionArray(params);
    
    // Calculate energy bands
    const conductionBand = calculateConductionBand(positions, params, material);
    const valenceBand = calculateValenceBand(conductionBand, material);
    const fermiLevel = calculateFermiLevel(params, material);
    
    // Calculate quantum mechanical properties
    const waveFunctions = calculateWaveFunctions(positions, params, material);
    const electricField = calculateElectricField(positions, params);
    const quantumStates = calculateQuantumStates(params, material);
    
    // Calculate additional properties
    const carrierConcentration = calculateCarrierConcentration(params, material);
    const mobility = calculateMobility(params, material);
    const capacitance = calculateCapacitance(params, dielectric);
    
    return {
        positions,
        conductionBand,
        valenceBand,
        fermiLevel,
        waveFunctions,
        electricField,
        quantumStates,
        carrierConcentration,
        mobility,
        capacitance,
        parameters: params,
        material,
        dielectric,
        timestamp: new Date().toISOString()
    };
}

// Generate position array
function generatePositionArray(params) {
    const positions = [];
    const radius = params.nanowireDiameter / 2;
    const step = radius / 50; // 100 points across the diameter
    
    for (let x = -radius; x <= radius; x += step) {
        positions.push(x);
    }
    
    return positions;
}

// Calculate conduction band
function calculateConductionBand(positions, params, material) {
    const { gateType, gateVoltage, oxideThickness, nanowireDiameter, temperature } = params;
    
    const gateInfo = gateType === 'omega' ? 
        { controlFactor: 0.8, fieldEnhancement: 1.2 } : 
        { controlFactor: 0.6, fieldEnhancement: 1.0 };
    
    return positions.map(x => {
        // Surface potential with gate control
        const surfacePotential = gateVoltage * gateInfo.controlFactor;
        
        // Band bending profile (parabolic for cylindrical geometry)
        const maxBending = surfacePotential * (oxideThickness / 5);
        const normalizedX = x / (nanowireDiameter / 2);
        const bandBending = maxBending * (1 - normalizedX * normalizedX);
        
        // Quantum confinement energy
        const confinementEnergy = calculateQuantumConfinementEnergy(x, params, material);
        
        // Temperature effects
        const thermalEffect = calculateThermalEffect(temperature, material);
        
        // Total conduction band energy
        return material.electronAffinity + bandBending + confinementEnergy + thermalEffect;
    });
}

// Calculate valence band
function calculateValenceBand(conductionBand, material) {
    return conductionBand.map(cb => cb - material.bandGap);
}

// Calculate quantum confinement energy
function calculateQuantumConfinementEnergy(x, params, material) {
    const { nanowireDiameter } = params;
    
    // Ground state confinement energy for cylindrical quantum wire
    const confinementEnergy = (CONSTANTS.hbar * CONSTANTS.hbar * CONSTANTS.pi * CONSTANTS.pi) / 
                              (2 * material.effectiveMass * CONSTANTS.m0 * Math.pow(nanowireDiameter * 1e-9, 2) * CONSTANTS.q);
    
    // Add spatial variation
    const normalizedX = x / (nanowireDiameter / 2);
    const spatialVariation = confinementEnergy * 0.1 * Math.cos(2 * CONSTANTS.pi * normalizedX);
    
    return confinementEnergy + spatialVariation;
}

// Calculate thermal effects
function calculateThermalEffect(temperature, material) {
    const kT = CONSTANTS.k * temperature / CONSTANTS.q; // eV
    const thermalBroadening = kT * 0.1; // Small thermal contribution
    return thermalBroadening;
}

// Calculate Fermi level
function calculateFermiLevel(params, material) {
    const { dopingConcentration, temperature } = params;
    
    // Simplified Fermi level calculation
    const kT = CONSTANTS.k * temperature / CONSTANTS.q; // eV
    
    // Intrinsic Fermi level
    const intrinsicFermi = material.electronAffinity + material.bandGap / 2;
    
    // Doping shift
    const dopingShift = kT * Math.log(dopingConcentration / 1e16);
    
    return intrinsicFermi + dopingShift;
}

// Calculate wave functions
function calculateWaveFunctions(positions, params, material) {
    const { nanowireDiameter } = params;
    const waveFunctions = [];
    
    // Calculate first few eigenfunctions for cylindrical quantum wire
    for (let n = 1; n <= 4; n++) {
        const psi = positions.map(x => {
            const normalizedX = x / (nanowireDiameter / 2);
            
            if (Math.abs(normalizedX) <= 1) {
                // Bessel function approximation for cylindrical coordinates
                const amplitude = Math.sqrt(2 / nanowireDiameter);
                const spatialPart = Math.sin(n * CONSTANTS.pi * (normalizedX + 1) / 2);
                return amplitude * spatialPart;
            }
            return 0;
        });
        
        // Calculate energy level
        const energy = calculateEnergyLevel(n, params, material);
        
        waveFunctions.push({
            n: n,
            psi: psi,
            energy: energy,
            probabilityDensity: psi.map(p => p * p)
        });
    }
    
    return waveFunctions;
}

// Calculate energy level
function calculateEnergyLevel(n, params, material) {
    const { nanowireDiameter, temperature } = params;
    
    // Energy level for cylindrical quantum wire
    const energy = (n * n * CONSTANTS.pi * CONSTANTS.pi * CONSTANTS.hbar * CONSTANTS.hbar) / 
                   (2 * material.effectiveMass * CONSTANTS.m0 * Math.pow(nanowireDiameter * 1e-9, 2) * CONSTANTS.q);
    
    // Add thermal broadening
    const kT = CONSTANTS.k * temperature / CONSTANTS.q;
    return energy + kT * 0.1;
}

// Calculate electric field
function calculateElectricField(positions, params) {
    const { gateType, gateVoltage, oxideThickness, nanowireDiameter } = params;
    
    const gateInfo = gateType === 'omega' ? 
        { fieldEnhancement: 1.2 } : 
        { fieldEnhancement: 1.0 };
    
    const maxField = gateVoltage / oxideThickness * gateInfo.fieldEnhancement;
    
    return positions.map(x => {
        const normalizedX = x / (nanowireDiameter / 2);
        
        // Field distribution for cylindrical geometry
        const fieldDistribution = maxField * normalizedX * Math.exp(-Math.abs(normalizedX) * 0.5);
        
        return fieldDistribution;
    });
}

// Calculate quantum states
function calculateQuantumStates(params, material) {
    const { nanowireDiameter, temperature } = params;
    const states = [];
    
    // Calculate quantum energy levels and occupancy
    for (let n = 1; n <= 6; n++) {
        const energy = calculateEnergyLevel(n, params, material);
        const occupancy = calculateOccupancy(energy, temperature);
        
        states.push({
            n: n,
            energy: energy,
            occupancy: occupancy,
            degeneracy: 2, // Spin degeneracy
            waveFunction: `ψ_${n}(r)`
        });
    }
    
    return states;
}

// Calculate occupancy
function calculateOccupancy(energy, temperature) {
    const kT = CONSTANTS.k * temperature / CONSTANTS.q; // eV
    return 1 / (1 + Math.exp(energy / kT));
}

// Calculate carrier concentration
function calculateCarrierConcentration(params, material) {
    const { dopingConcentration, temperature } = params;
    
    // Simplified carrier concentration calculation
    const kT = CONSTANTS.k * temperature / CONSTANTS.q; // eV
    const ni = Math.sqrt(material.effectiveMass * material.dielectricConstant) * 
              Math.exp(-material.bandGap / (2 * kT)); // Intrinsic concentration
    
    return {
        electrons: dopingConcentration,
        holes: ni * ni / dopingConcentration,
        intrinsic: ni
    };
}

// Calculate mobility
function calculateMobility(params, material) {
    const { temperature, nanowireDiameter } = params;
    
    // Temperature-dependent mobility
    const mobility0 = 1400 / material.effectiveMass; // Base mobility (cm²/V·s)
    const temperatureFactor = Math.pow(300 / temperature, 1.5);
    
    // Size-dependent mobility reduction
    const sizeFactor = 1 - Math.exp(-nanowireDiameter / 10);
    
    return mobility0 * temperatureFactor * sizeFactor;
}

// Calculate capacitance
function calculateCapacitance(params, dielectric) {
    const { nanowireDiameter, channelLength } = params;
    
    // Cylindrical capacitance
    const radius = nanowireDiameter / 2;
    const oxideThickness = params.oxideThickness;
    
    const capacitance = (2 * CONSTANTS.pi * CONSTANTS.epsilon0 * dielectric.k * channelLength * 1e-9) / 
                       Math.log((radius + oxideThickness) / radius);
    
    return capacitance * 1e12; // Convert to pF
}

// Update all diagrams
async function updateAllDiagrams(results) {
    const promises = [];
    
    if (results.parameters.showEnergyBands) {
        promises.push(updateBandDiagram(results));
    }
    
    if (results.parameters.showWaveFunctions) {
        promises.push(updateWaveFunctionDiagram(results));
    }
    
    if (results.parameters.showElectricField) {
        promises.push(updateElectricFieldDiagram(results));
    }
    
    if (results.parameters.showQuantumStates) {
        promises.push(updateQuantumDiagram(results));
    }
    
    await Promise.all(promises);
}

// Update band diagram
async function updateBandDiagram(results) {
    const container = document.getElementById('band-diagram');
    
    const traces = [
        {
            x: results.positions,
            y: results.conductionBand,
            type: 'scatter',
            mode: 'lines',
            name: 'Conduction Band',
            line: { color: '#2196F3', width: 3 }
        },
        {
            x: results.positions,
            y: results.valenceBand,
            type: 'scatter',
            mode: 'lines',
            name: 'Valence Band',
            line: { color: '#F44336', width: 3 }
        },
        {
            x: [results.positions[0], results.positions[results.positions.length - 1]],
            y: [results.fermiLevel, results.fermiLevel],
            type: 'scatter',
            mode: 'lines',
            name: 'Fermi Level',
            line: { color: '#4CAF50', width: 2, dash: 'dash' }
        }
    ];
    
    const layout = {
        title: {
            text: `Energy Band Diagram - ${results.parameters.gateType.toUpperCase()}-Gate ${results.parameters.material}`,
            font: { size: 16, weight: 'bold' }
        },
        xaxis: {
            title: 'Position (nm)',
            grid: { color: '#e0e0e0' },
            zeroline: { color: '#666' }
        },
        yaxis: {
            title: 'Energy (eV)',
            grid: { color: '#e0e0e0' },
            zeroline: { color: '#666' }
        },
        margin: { t: 50, r: 50, b: 50, l: 60 },
        plot_bgcolor: '#fafafa',
        paper_bgcolor: 'white',
        showlegend: true,
        legend: {
            x: 0.02,
            y: 0.98,
            bgcolor: 'rgba(255,255,255,0.8)',
            bordercolor: '#ddd',
            borderwidth: 1
        }
    };
    
    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['pan2d', 'lasso2d', 'select2d'],
        toImageButtonOptions: {
            format: 'png',
            filename: 'band_diagram',
            height: 600,
            width: 800,
            scale: 2
        }
    };
    
    await Plotly.newPlot(container, traces, layout, config);
}

// Update wave function diagram
async function updateWaveFunctionDiagram(results) {
    const container = document.getElementById('wavefunction-diagram');
    
    const traces = results.waveFunctions.map((wf, index) => ({
        x: results.positions,
        y: wf.probabilityDensity,
        type: 'scatter',
        mode: 'lines',
        name: `n=${wf.n} (E=${wf.energy.toFixed(3)} eV)`,
        line: { width: 2 }
    }));
    
    const layout = {
        title: {
            text: 'Wave Function Probability Density',
            font: { size: 16, weight: 'bold' }
        },
        xaxis: {
            title: 'Position (nm)',
            grid: { color: '#e0e0e0' }
        },
        yaxis: {
            title: '|ψ|²',
            grid: { color: '#e0e0e0' }
        },
        margin: { t: 50, r: 50, b: 50, l: 60 },
        plot_bgcolor: '#fafafa',
        paper_bgcolor: 'white'
    };
    
    await Plotly.newPlot(container, traces, layout);
}

// Update electric field diagram
async function updateElectricFieldDiagram(results) {
    const container = document.getElementById('electric-field-diagram');
    
    const trace = {
        x: results.positions,
        y: results.electricField,
        type: 'scatter',
        mode: 'lines',
        name: 'Electric Field',
        line: { color: '#9C27B0', width: 3 }
    };
    
    const layout = {
        title: {
            text: 'Electric Field Distribution',
            font: { size: 16, weight: 'bold' }
        },
        xaxis: {
            title: 'Position (nm)',
            grid: { color: '#e0e0e0' }
        },
        yaxis: {
            title: 'Electric Field (V/nm)',
            grid: { color: '#e0e0e0' }
        },
        margin: { t: 50, r: 50, b: 50, l: 60 },
        plot_bgcolor: '#fafafa',
        paper_bgcolor: 'white'
    };
    
    await Plotly.newPlot(container, [trace], layout);
}

// Update quantum diagram
async function updateQuantumDiagram(results) {
    const container = document.getElementById('quantum-diagram');
    
    const trace = {
        x: results.quantumStates.map(state => state.n),
        y: results.quantumStates.map(state => state.energy),
        type: 'bar',
        name: 'Energy Levels',
        marker: { 
            color: '#FF9800',
            line: { color: '#F57C00', width: 2 }
        },
        text: results.quantumStates.map(state => `n=${state.n}<br>E=${state.energy.toFixed(3)} eV<br>Occupancy: ${(state.occupancy*100).toFixed(1)}%`),
        textposition: 'outside',
        hoverinfo: 'text'
    };
    
    const layout = {
        title: {
            text: 'Quantum Energy Levels',
            font: { size: 16, weight: 'bold' }
        },
        xaxis: {
            title: 'Quantum Number (n)',
            grid: { color: '#e0e0e0' }
        },
        yaxis: {
            title: 'Energy (eV)',
            grid: { color: '#e0e0e0' }
        },
        margin: { t: 50, r: 50, b: 50, l: 60 },
        plot_bgcolor: '#fafafa',
        paper_bgcolor: 'white'
    };
    
    await Plotly.newPlot(container, [trace], layout);
}

// Update parameters display
function updateParameters(results) {
    const container = document.getElementById('parameter-grid');
    
    const parameters = [
        { name: 'Gate Type', value: results.parameters.gateType.toUpperCase() + '-Gate' },
        { name: 'Material', value: results.parameters.material },
        { name: 'Dielectric', value: results.parameters.dielectric },
        { name: 'Band Gap', value: results.material.bandGap.toFixed(3) + ' eV' },
        { name: 'Electron Affinity', value: results.material.electronAffinity.toFixed(3) + ' eV' },
        { name: 'Effective Mass', value: results.material.effectiveMass.toFixed(3) + ' m₀' },
        { name: 'Fermi Level', value: results.fermiLevel.toFixed(3) + ' eV' },
        { name: 'Barrier Height', value: results.dielectric.barrierHeight.toFixed(2) + ' eV' },
        { name: 'Carrier Concentration', value: results.carrierConcentration.electrons.toExponential(2) + ' cm⁻³' },
        { name: 'Mobility', value: results.mobility.toFixed(1) + ' cm²/V·s' },
        { name: 'Capacitance', value: results.capacitance.toFixed(2) + ' pF' },
        { name: 'Quantum Confinement', value: 'Active' }
    ];
    
    container.innerHTML = parameters.map(param => `
        <div class="parameter-item">
            <span class="parameter-name">${param.name}</span>
            <span class="parameter-value">${param.value}</span>
        </div>
    `).join('');
}

// Tab switching
function switchTab(tabName) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    
    event.target.classList.add('active');
    document.getElementById(tabName + '-tab').classList.add('active');
}

// Export functions
function exportDiagram(format) {
    const activeTab = document.querySelector('.tab-content.active').id;
    const diagramId = activeTab.replace('-tab', '-diagram');
    
    if (format === 'png' || format === 'svg') {
        Plotly.downloadImage(diagramId, {
            format: format,
            width: 1000,
            height: 750,
            filename: `nwfet_${activeTab}_diagram`
        });
    }
}

function exportData(format) {
    if (format === 'csv') {
        exportToCSV();
    } else if (format === 'json') {
        exportToJSON();
    }
}

function exportToCSV() {
    const csv = generateCSVData();
    downloadFile(csv, 'nwfet_band_diagram_data.csv', 'text/csv');
}

function exportToJSON() {
    const json = JSON.stringify(currentResults, null, 2);
    downloadFile(json, 'nwfet_band_diagram_data.json', 'application/json');
}

function generateCSVData() {
    if (!currentResults.positions) return '';
    
    let csv = 'Position,Conduction Band,Valence Band,Fermi Level,Electric Field\n';
    
    for (let i = 0; i < currentResults.positions.length; i++) {
        csv += `${currentResults.positions[i]},${currentResults.conductionBand[i]},${currentResults.valenceBand[i]},${currentResults.fermiLevel},${currentResults.electricField[i]}\n`;
    }
    
    return csv;
}

function downloadFile(content, filename, contentType) {
    const blob = new Blob([content], { type: contentType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Utility functions
function showLoading() {
    const loadingElements = document.querySelectorAll('.loading-overlay');
    loadingElements.forEach(element => {
        element.style.display = 'flex';
    });
}

function hideLoading() {
    const loadingElements = document.querySelectorAll('.loading-overlay');
    loadingElements.forEach(element => {
        element.style.display = 'none';
    });
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 10000;
        animation: slideIn 0.3s ease;
        max-width: 300px;
    `;
    
    // Set background color based on type
    const colors = {
        success: 'linear-gradient(135deg, #27ae60, #2ecc71)',
        error: 'linear-gradient(135deg, #e74c3c, #c0392b)',
        info: 'linear-gradient(135deg, #3498db, #2980b9)',
        warning: 'linear-gradient(135deg, #f39c12, #e67e22)'
    };
    
    notification.style.background = colors[type] || colors.info;
    
    // Add to document
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Form validation
function setupFormValidation() {
    const inputs = document.querySelectorAll('input[type="number"], input[type="range"]');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            validateInput(this);
        });
    });
}

function validateInput(input) {
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    const value = parseFloat(input.value);
    
    if (min && value < min) {
        input.style.borderColor = '#e74c3c';
        showNotification(`${input.id} must be >= ${min}`, 'warning');
    } else if (max && value > max) {
        input.style.borderColor = '#e74c3c';
        showNotification(`${input.id} must be <= ${max}`, 'warning');
    } else {
        input.style.borderColor = '#27ae60';
    }
}

// Keyboard shortcuts
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to calculate
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            calculateBandDiagram();
        }
        
        // Ctrl/Cmd + S to save
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            saveParameters();
        }
        
        // Ctrl/Cmd + L to load
        if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
            e.preventDefault();
            loadParameters();
        }
        
        // Escape to reset
        if (e.key === 'Escape') {
            resetParameters();
        }
    });
}

// Auto-save functionality
function setupAutoSave() {
    // Save parameters every 30 seconds
    setInterval(saveParameters, 30000);
    
    // Save on window unload
    window.addEventListener('beforeunload', saveParameters);
}

function saveParameters() {
    const params = getParameters();
    localStorage.setItem('nwfet_parameters', JSON.stringify(params));
    localStorage.setItem('nwfet_timestamp', new Date().toISOString());
}

function loadSavedParameters() {
    const saved = localStorage.getItem('nwfet_parameters');
    if (saved) {
        try {
            const params = JSON.parse(saved);
            applyParameters(params);
            showNotification('Parameters loaded from saved session', 'info');
        } catch (error) {
            console.error('Error loading saved parameters:', error);
        }
    }
}

function applyParameters(params) {
    // Apply gate type
    document.querySelectorAll('.gate-option').forEach(opt => {
        opt.classList.remove('selected');
        if (opt.dataset.gate === params.gateType) {
            opt.classList.add('selected');
        }
    });
    
    // Apply other parameters
    document.getElementById('material').value = params.material;
    document.getElementById('dielectric').value = params.dielectric;
    document.getElementById('oxide-thickness').value = params.oxideThickness;
    document.getElementById('nanowire-diameter').value = params.nanowireDiameter;
    document.getElementById('channel-length').value = params.channelLength;
    document.getElementById('doping-concentration').value = params.dopingConcentration;
    document.getElementById('gate-voltage').value = params.gateVoltage;
    document.getElementById('drain-voltage').value = params.drainVoltage;
    document.getElementById('temperature').value = params.temperature;
    
    // Update displays
    updateMaterialInfo();
    updateRangeDisplays();
}

function updateRangeDisplays() {
    const rangeInputs = [
        { id: 'oxide-thickness', unit: 'nm' },
        { id: 'nanowire-diameter', unit: 'nm' },
        { id: 'gate-voltage', unit: 'V' }
    ];
    
    rangeInputs.forEach(input => {
        const element = document.getElementById(input.id);
        const display = element.nextElementSibling;
        if (display) {
            display.textContent = element.value + ' ' + input.unit;
        }
    });
}

function resetParameters() {
    if (confirm('Are you sure you want to reset all parameters to default values?')) {
        // Reset to default values
        document.getElementById('material').value = 'Si';
        document.getElementById('dielectric').value = 'SiO2';
        document.getElementById('oxide-thickness').value = 2;
        document.getElementById('nanowire-diameter').value = 10;
        document.getElementById('channel-length').value = 20;
        document.getElementById('doping-concentration').value = 1e18;
        document.getElementById('gate-voltage').value = 0;
        document.getElementById('drain-voltage').value = 0.1;
        document.getElementById('temperature').value = 300;
        
        // Update displays
        updateMaterialInfo();
        updateRangeDisplays();
        
        showNotification('Parameters reset to default values', 'info');
    }
}

// History management
function saveToHistory(action, data) {
    const historyEntry = {
        timestamp: new Date().toISOString(),
        action: action,
        data: data
    };
    
    calculationHistory.push(historyEntry);
    
    // Keep only last 50 entries
    if (calculationHistory.length > 50) {
        calculationHistory = calculationHistory.slice(-50);
    }
    
    localStorage.setItem('nwfet_history', JSON.stringify(calculationHistory));
}

// Material display update
function updateMaterialDisplay(material, dielectric) {
    // Update any material-specific displays
    const materialInfo = document.getElementById('material-info');
    if (materialInfo) {
        materialInfo.innerHTML = `
            <div><strong>Band Gap:</strong> ${material.bandGap} eV</div>
            <div><strong>Electron Affinity:</strong> ${material.electronAffinity} eV</div>
            <div><strong>Effective Mass:</strong> ${material.effectiveMass} m₀</div>
        `;
    }
}

function updateGateDisplay(gateInfo) {
    // Update any gate-specific displays
    const gateInfoDisplay = document.getElementById('gate-info');
    if (gateInfoDisplay) {
        gateInfoDisplay.innerHTML = `
            <div><strong>Description:</strong> ${gateInfo.description}</div>
            <div><strong>Control Factor:</strong> ${gateInfo.controlFactor}</div>
            <div><strong>Field Enhancement:</strong> ${gateInfo.fieldEnhancement}x</div>
        `;
    }
}

// Update calculations preview
function updateCalculationsPreview() {
    // This could show a quick preview of key calculations
    // Implementation depends on requirements
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .notification {
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
`;
document.head.appendChild(style);
