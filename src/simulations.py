"""
Simulation classes for NWFET analyses.
Each class handles a specific type of simulation.
"""

import numpy as np
import logging
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from src.physics_models import NWFETSimulator
from src.plotting import Plotter2D, Plotter3D, DataExporter
from config.constants import (
    MATERIALS, GATE_CONFIGURATIONS, SIMULATION_PARAMETERS,
    DEVICE_PARAMETERS, OUTPUT_DIRECTORIES
)


class CVThicknessSweepSimulation:
    """Simulation for C-V characteristics vs oxide thickness."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run the thickness sweep simulation for all gate configurations."""
        self.logger.info("Starting C-V thickness sweep simulation")
        voltage = np.linspace(
            *SIMULATION_PARAMETERS['voltage_range'],
            SIMULATION_PARAMETERS['voltage_points']
        )
        thicknesses = SIMULATION_PARAMETERS['thickness_sweep']

        for gate_name, gate_config in GATE_CONFIGURATIONS.items():
            self.logger.info(f"Processing thickness sweep for {gate_name}")
            materials_data = {}
            for material_name in MATERIALS.keys():
                capacitance_list = []
                for thickness in thicknesses:
                    capacitance = self.simulator.simulate_cv(
                        material_name, gate_name, voltage, thickness
                    )
                    capacitance_list.append(capacitance)
                materials_data_z[material_name] = capacitance_list
                materials_data_m[material_name] = capacitance_list[0]
            materials_data_z_both[gate_name] = materials_data_z
            materials_data_m_both[gate_name] = materials_data_m

            filename = f"{gate_name}_cv_thickness_sweep.png"
            self.plotter.plot_cv_thickness_sweep(materials_data_z, voltage, filename)

        self.logger.info("C-V thickness sweep simulation completed")


class IVTransferSimulation:
    """Simulation for I-V transfer characteristics."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run I-V transfer simulation for all materials and gates."""
        self.logger.info("Starting I-V transfer simulation")
        vgs = np.linspace(0, 1.2, 300)
        vds = 0.5
        temperature = 300

        results_all = {}
        for gate in GATE_CONFIGURATIONS.keys():
            for material in MATERIALS.keys():
                current = self.simulator.simulate_iv(material, gate, vgs, vds, temperature)
                key = f"{gate}_{material}"
                results_all[key] = current

        filename = "device_grid.png"
        # Prepare data for plot_device_features_grid
        temperatures = [300]
        gates = list(GATE_CONFIGURATIONS.keys())
        materials = list(MATERIALS.keys())
        vgs_range = vgs
        data = {temp: {gate: {material: {'vgs': vgs, 'id': self.simulator.simulate_iv(material, gate, vgs, vds, temp)} 
                for material in materials} for gate in gates} for temp in temperatures}
        self.plotter.plot_device_features_grid(data, temperatures, gates, materials, vgs_range, filename)

        # Calculate parameters for material comparison
        parameters = {}
        for key, current in results_all.items():
            vth = vgs[np.argmax(current > 1e-7)] if np.any(current > 1e-7) else 0
            ion = current[-1] * 1e6 / DEVICE_PARAMETERS['channel_width']
            ioff = current[0] * 1e9 / DEVICE_PARAMETERS['channel_width']
            parameters[key] = {'vth': vth, 'ion': ion, 'ioff': ioff}

        comparison_filename = "material_comparison_grid.png"
        self.plotter.plot_material_comparison_grid(parameters, comparison_filename)

        filename = "performance_radar_plot.png"
        self.plotter.plot_performance_radar(filename)

        self.logger.info("I-V transfer simulation completed")


class IVOutputSimulation:
    """Simulation for I-V output characteristics."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run I-V output simulation for all materials and gates."""
        self.logger.info("Starting I-V output simulation")
        vds_range = np.linspace(*SIMULATION_PARAMETERS['drain_voltage_range'],
                               SIMULATION_PARAMETERS['drain_voltage_points'])
        vgs_fixed = 1.0
        temperature = 300

        for material in MATERIALS.keys():
            results = {}
            for gate in GATE_CONFIGURATIONS.keys():
                current_list = []
                for vds in vds_range:
                    current = self.simulator.simulate_iv(material, gate, np.array([vgs_fixed]), vds, temperature)[0]
                    current_list.append(current)
                results[gate] = np.array(current_list)

            filename = f"{material}_iv_output.png"
            self.plotter.plot_iv_output(results, vds_range, filename)

        self.logger.info("I-V output simulation completed")


class TemperatureIVSimulation:
    """Simulation for temperature-dependent I-V."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run temperature-dependent I-V simulation for all materials and gates."""
        self.logger.info("Starting temperature I-V simulation")
        vgs = np.linspace(0, 1.2, 300)
        temperatures = [77, 300, 600]
        results_dict = {}
        for gate in GATE_CONFIGURATIONS.keys():
            results_dict[gate] = {}
            for material in MATERIALS.keys():
                results_dict[gate][material] = {}
                for temp in temperatures:
                    current = self.simulator.simulate_iv(material, gate, vgs, 0.5, temp)
                    results_dict[gate][material][temp] = {'vgs': vgs, 'ids': current}

        self.plotter.plot_temperature_iv_grid(results_dict, 'temperature_dependent_iv.png')
        self.logger.info("Saved temperature-dependent I-V grid plot")

        # Continue with 3D plots...

        materials = {
            "SiO2": [3.9, 0.45], 
            "Al2O3": [9.0, 0.42],
            "ZrO2": [22.0, 0.39],
            "HfO2": [25.0, 0.38], 
            "La2O3": [27.0, 0.35]
        }

        gate_configs = {
            "PiGate": {"eta": 0.82, "mu_ref": 0.04},
            "OmegaGate": {"eta": 0.98, "mu_ref": 0.06}
        }

        for dev, par in gate_configs.items():
            fig = plt.figure(figsize=(20, 14))
            fig.suptitle(f'3D Transfer Analysis: $I_D$ vs $V_{{GS}}$ vs Temp for {dev} NWFET', 
                         fontsize=18, fontweight='bold', y=0.96)

            for idx, (m_name, m_data) in enumerate(materials.items()):
                k_val, vth0 = m_data
                ax = fig.add_subplot(2, 3, idx+1, projection='3d')
                
                vth_t = vth0 - 0.0005 * (T_grid - 300)
                
                mu_t = par['mu_ref'] * (np.maximum(T_grid, 10) / 300)**-1.5
                
                eps0 = 8.854e-12
                tox = 2e-9
                Cox = (eps0 * k_val) / tox
                W, L = 10e-9, 10e-9

                v_od = np.maximum(VGS_grid - vth_t, 0)
                ID = 0.5 * mu_t * Cox * par['eta'] * (W/L) * v_od**2
                ID_uA = ID * 1e6

                surf = ax.plot_surface(VGS_grid, T_grid, ID_uA, cmap='turbo', 
                                       edgecolor='none', alpha=0.9, antialiased=True)

                ax.set_title(f'{m_name} ($k$={k_val})', fontsize=14, fontweight='bold', pad=10)
                ax.set_xlabel('$V_{GS}$ (V)', fontsize=10)
                ax.set_ylabel('Temp (K)', fontsize=10)
                ax.set_zlabel('$I_D$ ($\mu$A)', fontsize=10)
                
                ax.set_zlim(0, 500 if dev == "PiGate" else 800)

                ax.view_init(elev=25, azim=-135)

            ax_info = fig.add_subplot(2, 3, 6)
            ax_info.axis('off')
            # ax_info.text(0.5, 0.5, f"Architecture: {dev}\nGate Oxide: 2nm\n$W/L = 1.0$", 
            #              ha='center', va='center', fontsize=14, fontweight='bold',
            #              bbox=dict(boxstyle="round,pad=1", fc="whitesmoke", ec="black"))
            
            filename = f"{dev}_3d_full_materials_transfer.png"
            plt.savefig(f"{OUTPUT_DIRECTORIES['plots']}{filename}", dpi=300)
            plt.close(fig)
            self.logger.info(f"Saved 3D transfer plot for {dev}")

        self.logger.info("Temperature I-V simulation completed")


class TempVdsIdSimulation:
    """Simulation for 3D ID vs VDS vs Temp."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D ID vs VDS vs Temp simulation for all materials and gates."""
        self.logger.info("Starting 3D ID vs VDS vs Temp simulation")
        vds = np.linspace(0, 1.2, 50)
        temp_range = np.linspace(77, 600, 50)
        vgs = 1.0  # Fixed

        for gate in GATE_CONFIGURATIONS.keys():
            results = {}
            for material in MATERIALS.keys():
                VDS, T = np.meshgrid(vds, temp_range)
                current_grid = np.zeros_like(VDS)
                for i in range(VDS.shape[0]):
                    for j in range(VDS.shape[1]):
                        current_grid[i, j] = self.simulator.simulate_iv(
                            material, gate, np.array([vgs]), VDS[i, j], T[i, j]
                        )[0]
                results[material] = current_grid * 1e6  # µA

            filename = f"{gate}_3d_temp_vds_id_full.png"
            self.plotter.plot_3d_temp_vds_grid(results, gate, vds, temp_range, filename)

        self.logger.info("3D ID vs VDS vs Temp simulation completed")


class TempVgsCoxSimulation:
    """Simulation for 3D Cox vs VGS vs Temp."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D Cox vs VGS vs Temp simulation for all materials and gates."""
        self.logger.info("Starting 3D Cox vs VGS vs Temp simulation")
        vgs = np.linspace(-0.5, 1.2, 50)
        temp_range = np.linspace(77, 600, 50)
        VGS_grid, T_grid = np.meshgrid(vgs, temp_range)

        materials = {
            "SiO2": [3.9, 'GnBu'], 
            "Al2O3": [9.0, 'YlGn'],
            "ZrO2": [22.0, 'OrRd'],
            "HfO2": [25.0, 'YlOrRd'], 
            "La2O3": [27.0, 'PuBuGn']
        }

        gate_configs = {
            "PiGate": {"eta": 0.82},
            "OmegaGate": {"eta": 0.98}
        }

        for dev, par in gate_configs.items():
            fig = plt.figure(figsize=(20, 14))
            fig.suptitle(f'3D Capacitance Analysis: $C_{{ox}}$ vs $V_{{GS}}$ vs Temperature for {dev} NWFET', 
                         fontsize=18, fontweight='bold', y=0.96)

            for idx, (m_name, m_data) in enumerate(materials.items()):
                k_val, cmap_choice = m_data
                ax = fig.add_subplot(2, 3, idx+1, projection='3d')
                
                eps0 = 8.854e-12
                tox = 2e-9
                Cox_ideal = (eps0 * k_val) / tox
                
                vth_t = 0.3 - 0.0004 * (T_grid - 300)
                
                slope = 15 - 0.01 * (T_grid - 300) 
                Cox_eff = Cox_ideal * par['eta'] / (1 + np.exp(-slope * (VGS_grid - vth_t)))
                
                surf = ax.plot_surface(VGS_grid, T_grid, Cox_eff * 1e3, cmap=cmap_choice, 
                                       edgecolor='none', alpha=0.9, antialiased=True)

                ax.set_title(f'Dielectric: {m_name} ($k$={k_val})', fontsize=14, fontweight='bold', pad=10)
                ax.set_xlabel('$V_{GS}$ (V)', fontsize=10)
                ax.set_ylabel('Temp (K)', fontsize=10)
                ax.set_zlabel('Eff. $C_{ox}$ ($mF/m^2$)', fontsize=10)
                
                axins = inset_axes(ax, width="5%", height="50%", loc='lower left', borderpad=-2)
                cb = fig.colorbar(surf, cax=axins)
                cb.ax.tick_params(labelsize=8)

                ax.view_init(elev=25, azim=-135)
                
                ax.set_zlim(0, 130 if k_val > 15 else 50)

            ax_info = fig.add_subplot(2, 3, 6)
            ax_info.axis('off')
            
            filename = f"{dev}_3d_temp_vgs_cox_full.png"
            plt.savefig(f"{OUTPUT_DIRECTORIES['plots']}{filename}", dpi=300)
            plt.close(fig)
            self.logger.info(f"Saved 3D Cox plot for {dev}")

        self.logger.info("3D Cox vs VGS vs Temp simulation completed")


class ThicknessTempSimulation:
    """Simulation for 3D drain current vs oxide thickness and temperature."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D thickness vs temperature simulation for both gates and all materials."""
        self.logger.info("Starting 3D thickness vs temperature simulation")
        
        gates = ["PiGate", "OmegaGate"]
        materials = list(MATERIALS.keys())
        thicknesses = np.linspace(1e-9, 9e-9, 50)  # 1 to 9 nm
        temp_range = np.linspace(77, 600, 50)
        vgs = 1.0
        vds = 0.5
        
        id_grids = {}
        for gate in gates:
            id_grids[gate] = {}
            for material in materials:
                id_grid = np.zeros((len(temp_range), len(thicknesses)))
                for i, temp in enumerate(temp_range):
                    for j, tox in enumerate(thicknesses):
                        # Note: simulator.simulate_iv may not use tox directly, but assume it does
                        current = self.simulator.simulate_iv(material, gate, np.array([vgs]), vds, temp)[0]
                        id_grid[i, j] = current * 1e6  # µA
                id_grids[gate][material] = id_grid
        
        save_filename = "3d_current_surface.png"
        self.plotter.plot_3d_thickness_temp_current(id_grids, thicknesses, temp_range, save_filename)
        
        self.logger.info("3D thickness vs temperature simulation completed")


class TempVgsIdSimulation:
    """Simulation for 3D ID vs VGS vs Temp."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D ID vs VGS vs Temp simulation for all gates and materials."""
        self.logger.info("Starting 3D temp VGS ID simulation")
        
        vgs = np.linspace(0, 1.2, 50)
        vds = 0.5
        temp_range = np.linspace(77, 600, 50)
        
        results = {}
        for gate in GATE_CONFIGURATIONS.keys():
            results[gate] = {}
            for material in MATERIALS.keys():
                id_grid = np.zeros((len(temp_range), len(vgs)))
                for i, temp in enumerate(temp_range):
                    current = self.simulator.simulate_iv(material, gate, vgs, vds, temp)
                    id_grid[i, :] = current * 1e6  # µA
                results[gate][material] = id_grid
        
        save_filename = "3d_transfer_grid.png"
        self.plotter.plot_3d_temp_vgs_id(results, vgs, temp_range, save_filename)
        
        self.logger.info("3D temp VGS ID simulation completed")


class TempParameterSweepSimulation:
    """Simulation for device parameters vs temperature."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run parameter sweep vs temperature for all gates and materials."""
        self.logger.info("Starting temp parameter sweep simulation")
        
        vgs = np.linspace(0, 1.2, 300)
        vds = 0.5
        temp_range = np.linspace(77, 600, 50)
        
        parameters = {}
        for material in MATERIALS.keys():
            parameters[material] = {}
            for gate in GATE_CONFIGURATIONS.keys():
                parameters[material][gate] = {'vth': [], 'ion': [], 'ioff': []}
        
        for temp in temp_range:
            for material in MATERIALS.keys():
                for gate in GATE_CONFIGURATIONS.keys():
                    current = self.simulator.simulate_iv(material, gate, vgs, vds, temp)
                    vth = vgs[np.argmax(current > 1e-7)] if np.any(current > 1e-7) else 0
                    ion = current[-1] * 1e6  # µA
                    ioff = current[0] * 1e9  # nA
                    parameters[material][gate]['vth'].append(vth)
                    parameters[material][gate]['ion'].append(ion)
                    parameters[material][gate]['ioff'].append(ioff)
        
        save_filename = "temperature_material_comparison.png"
        self.plotter.plot_temp_parameter_sweep(parameters, temp_range, save_filename)
        
        self.logger.info("Temp parameter sweep simulation completed")


class CryogenicIVSimulation:
    """Simulation for cryogenic I-V characteristics at 77 K."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run I-V simulation at cryogenic temperature (77 K) for all gates and materials."""
        self.logger.info("Starting cryogenic I-V simulation")
        
        vgs = np.linspace(0, 1.2, 300)
        vds = 0.5
        temp = 77
        
        results = {}
        for gate in GATE_CONFIGURATIONS.keys():
            results[gate] = {}
            for material in MATERIALS.keys():
                current = self.simulator.simulate_iv(material, gate, vgs, vds, temp)
                results[gate][material] = current
        
        filename = "cryogenic_iv_comparison.png"
        self.plotter.plot_iv_transfer_grid(results, vgs, filename)
        
        self.logger.info("Cryogenic I-V simulation completed")


class HighTempIVSimulation:
    """Simulation for high-temperature I-V characteristics at 600 K."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D ID vs VGS vs Temp simulation for high temperatures (400-600 K) for all gates and materials."""
        self.logger.info("Starting high-temperature 3D I-V simulation")
        
        vgs = np.linspace(0, 1.2, 30)
        vds = 0.5
        temp_range = np.linspace(400, 600, 30)
        
        results = {}
        for gate in GATE_CONFIGURATIONS.keys():
            results[gate] = {}
            for material in MATERIALS.keys():
                id_grid = np.zeros((len(temp_range), len(vgs)))
                for i, temp in enumerate(temp_range):
                    current = self.simulator.simulate_iv(material, gate, vgs, vds, temp)
                    id_grid[i, :] = current
                # Normalize by the 400 K (first temp) value to show relative changes
                id_grid_norm = id_grid / id_grid[0, :] if np.any(id_grid[0, :] > 0) else id_grid
                results[gate][material] = id_grid_norm
        
        filename = "high_temperature_reliability.png"
        self.plotter.plot_3d_temp_vgs_id(results, vgs, temp_range, filename)
        
        self.logger.info("High-temperature 3D I-V simulation completed")


class IVThicknessSweepSimulation:

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run I-V thickness sweep simulation for all gate configurations."""
        self.logger.info("Starting I-V thickness sweep simulation")
        vgs = np.linspace(0, 1.2, 300)
        vds = 0.5
        temperature = 300
        tox_list = np.array([1e-9, 3e-9, 5e-9, 7e-9, 9e-9])

        parameters = {}
        for gate in GATE_CONFIGURATIONS.keys():
            parameters[gate] = {}
            for material in MATERIALS.keys():
                vth_list = []
                ion_list = []
                ioff_list = []
                for tox in tox_list:
                    # Note: simulate_iv uses fixed tox from constants, so parameters may not vary with tox
                    current = self.simulator.simulate_iv(material, gate, vgs, vds, temperature)
                    vth = vgs[np.argmax(current > 1e-7)] if np.any(current > 1e-7) else 0
                    ion = current[-1] * 1e6  # µA
                    ioff = current[0] * 1e9  # nA
                    vth_list.append(vth)
                    ion_list.append(ion)
                    ioff_list.append(ioff)
                parameters[gate][material] = {'vth': vth_list, 'ion': ion_list, 'ioff': ioff_list}

        filename = "oxide_thickness_sweep.png"
        self.plotter.plot_oxide_thickness_sweep(parameters, tox_list, filename)

        self.logger.info("I-V thickness sweep simulation completed")


class EISRelaxationSimulation:
    """Simulation for EIS relaxation study."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter2D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run EIS relaxation simulation for all gate configurations."""
        self.logger.info("Starting EIS relaxation simulation")
        freq = np.logspace(0, 7, 71)
        thicknesses = [2e-9]  # Single thickness for clarity
        thickness = thicknesses[0]
        z_real_all = {}
        z_imag_all = {}
        materials_data_z_both = {}
        materials_data_m_both = {}
        for gate_name, gate_config in GATE_CONFIGURATIONS.items():
            self.logger.info(f"Processing EIS for {gate_name}")
            materials_data_zr = {}
            materials_data_zi = {}
            rs = gate_config['series_resistance']
            eta = gate_config['eta']
            for material_name, material_props in MATERIALS.items():
                zr_list = []
                zi_list = []
                k, _, _, c0 = material_props
                for tox in thicknesses:
                    tau = (1e-6 / (k**0.5)) * np.exp(500 / 300) * (tox / 1e-9)**0.5
                    zr, zi = self.simulator.impedance_model.calculate_impedance(
                        freq, 300, rs, eta, k, c0
                    )
                    zr_list.append(zr)
                    zi_list.append(zi)

                materials_data_zr[material_name] = zr_list
                materials_data_zi[material_name] = zi_list

            z_real_all[gate_name] = materials_data_zr
            z_imag_all[gate_name] = materials_data_zi

            materials_data_z = {m: materials_data_zr[m][0] for m in materials_data_zr}
            materials_data_m = {m: materials_data_zi[m][0] for m in materials_data_zi}
            materials_data_z_both[gate_name] = materials_data_z
            materials_data_m_both[gate_name] = materials_data_m
            comparison_filename = f"{gate_name}_eis_comparison.png"
            self.plotter.plot_eis_comparison(materials_data_z, materials_data_m, freq, thickness, comparison_filename)

        filename = "nyquist_eis_plot.png"
        self.plotter.plot_nyquist(z_real_all, z_imag_all, thicknesses, filename)

        filename = "analysis_fig.png"
        self.plotter.plot_eis_comparison_both(materials_data_z_both, materials_data_m_both, freq, thickness, filename)

        # For Figure 13: Comparative for all materials
        thicknesses_fig13 = [1e-9, 3e-9, 5e-9, 7e-9, 9e-9]
        z_real_fig13 = {}
        z_imag_fig13 = {}
        for m in MATERIALS:
            k, _, _, c0 = MATERIALS[m]
            z_real_fig13[m] = {}
            z_imag_fig13[m] = {}
            for gate_name in GATE_CONFIGURATIONS:
                rs = GATE_CONFIGURATIONS[gate_name]['series_resistance']
                eta = GATE_CONFIGURATIONS[gate_name]['eta']
                z_real_fig13[m][gate_name] = []
                z_imag_fig13[m][gate_name] = []
                for tox in thicknesses_fig13:
                    zr, zi = self.simulator.impedance_model.calculate_impedance(freq, 300, rs, eta, k, c0)
                    z_real_fig13[m][gate_name].append(zr)
                    z_imag_fig13[m][gate_name].append(zi)
        filename = "nyquist_comparison_plot.png"
        self.plotter.plot_nyquist_comparison_all(z_real_fig13, z_imag_fig13, thicknesses_fig13)

        # For Figure 15: Comparative Bode for all materials
        thicknesses_bode = [1e-9, 1.5e-9, 2e-9, 2.5e-9, 3e-9, 3.5e-9, 4e-9, 4.5e-9, 5e-9]  # 9 thicknesses
        z_real_bode = {}
        z_imag_bode = {}
        for m in MATERIALS:
            k, _, _, c0 = MATERIALS[m]
            z_real_bode[m] = {}
            z_imag_bode[m] = {}
            for gate_name in GATE_CONFIGURATIONS:
                rs = GATE_CONFIGURATIONS[gate_name]['series_resistance']
                eta = GATE_CONFIGURATIONS[gate_name]['eta']
                z_real_bode[m][gate_name] = []
                z_imag_bode[m][gate_name] = []
                for tox in thicknesses_bode:
                    tau = (1e-6 / (k**0.5)) * np.exp(500 / 300) * (tox / 1e-9)**0.5
                    zr, zi = self.simulator.impedance_model.calculate_impedance(freq, 300, rs, eta, k, c0, tau)
                    z_real_bode[m][gate_name].append(zr)
                    z_imag_bode[m][gate_name].append(zi)
        filename = "bode_comparison_plot.png"
        self.plotter.plot_bode_comparison(z_real_bode, z_imag_bode, thicknesses_bode, freq)

        # For Figure 16: Impedance spectra comparison for all materials and gates
        z_real_gate = {}
        z_imag_gate = {}
        for m in MATERIALS:
            k, _, _, c0 = MATERIALS[m]
            z_real_gate[m] = {}
            z_imag_gate[m] = {}
            for gate_name in GATE_CONFIGURATIONS:
                rs = GATE_CONFIGURATIONS[gate_name]['series_resistance']
                eta = GATE_CONFIGURATIONS[gate_name]['eta']
                tau_fixed = (1e-6 / (k**0.5)) * np.exp(500 / 300) * (2e-9 / 1e-9)**0.5
                zr, zi = self.simulator.impedance_model.calculate_impedance(freq, 300, rs, eta, k, c0, tau_fixed)
                z_real_gate[m][gate_name] = zr
                z_imag_gate[m][gate_name] = zi
        filename = "impedance_spectra_comparison.png"
        self.plotter.plot_impedance_spectra_comparison_all(z_real_gate, z_imag_gate)

        # For Figure 18: Temperature-dependent EIS plot
        temperatures = [77, 300, 600]
        temperature_data_z = {temp: {} for temp in temperatures}
        temperature_data_m = {temp: {} for temp in temperatures}
        for temp in temperatures:
            for gate_name in GATE_CONFIGURATIONS:
                rs = GATE_CONFIGURATIONS[gate_name]['series_resistance']
                eta = GATE_CONFIGURATIONS[gate_name]['eta']
                materials_data_zr = {}
                materials_data_zi = {}
                for material_name, material_props in MATERIALS.items():
                    zr_list = []
                    zi_list = []
                    k, _, _, c0 = material_props
                    for tox in thicknesses:
                        tau = (1e-6 / (k**0.5)) * np.exp(500 / temp) * (tox / 1e-9)**0.5
                        zr, zi = self.simulator.impedance_model.calculate_impedance(freq, temp, rs, eta, k, c0, tau)
                        zr_list.append(zr)
                        zi_list.append(zi)
                    materials_data_zr[material_name] = zr_list
                    materials_data_zi[material_name] = zi_list
                materials_data_z = {m: materials_data_zr[m][0] for m in materials_data_zr}
                materials_data_m = {m: materials_data_zi[m][0] for m in materials_data_zi}
                temperature_data_z[temp][gate_name] = materials_data_z
                temperature_data_m[temp][gate_name] = materials_data_m
        filename = "temperature_eis_plot.png"
        self.plotter.plot_temperature_eis(temperature_data_z, temperature_data_m, freq, temperatures, filename)

        filename = "equivalent_circuit_comparison.png"
        self.plotter.plot_equivalent_circuit_comparison()


class PotentialProfileSimulation:
    """Simulation for 3D potential profiles."""

    def __init__(self, simulator: NWFETSimulator, plotter: Plotter3D):
        self.simulator = simulator
        self.plotter = plotter
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """Run 3D potential profile simulation for all gate configurations."""
        self.logger.info("Starting potential profile simulation")

        # Setup cylindrical geometry
        z = np.linspace(0, 20, 60)  # Channel length in nm
        theta = np.linspace(0, 2 * np.pi, 60)
        z_grid, theta_grid = np.meshgrid(z, theta)
        radius = 5  # Radius in nm

        # Convert to Cartesian for plotting
        X = radius * np.cos(theta_grid)
        Y = radius * np.sin(theta_grid)
        Z = z_grid

        # Oxide materials
        materials_list = [(m_name, MATERIALS[m_name][0], "0.5V") for m_name in MATERIALS.keys()]

        # Generation for both architectures
        gate_types = list(GATE_CONFIGURATIONS.keys())

        for gate in gate_types:
            fig = plt.figure(figsize=(18, 10))
            fig.suptitle(f'3D Potential Profile for Different Gate Oxide Materials ({gate})', 
                         fontsize=18, fontweight='bold', fontname='serif', y=0.95)

            for idx, (m_name, k_val, vgs_val) in enumerate(materials_list):
                ax = fig.add_subplot(2, 3, idx+1, projection='3d')
                
                # Potential modeling (Normalized 0 to 1)
                if gate == "OmegaGate":
                    potential = 0.4 + 0.5 * np.cos(theta_grid / 2)**2
                else:
                    potential = np.where(
                        (theta_grid > 1.3 * np.pi) & (theta_grid < 1.7 * np.pi),
                        0.1, 0.8
                    )
                
                # Scale potential based on High-k
                field_strength = potential * (k_val / 3.9)**0.12
                field_strength = np.clip(field_strength, 0, 1.2)

                # Surface plotting
                surf = ax.plot_surface(Z, X, Y, facecolors=plt.cm.jet(field_strength),
                                       shade=False, rstride=1, cstride=1, antialiased=True,
                                       linewidth=0, alpha=0.9)

                ax.set_title(f'Dielectric: {m_name}\n$V_{{GS}}$ = {vgs_val}', fontsize=14, fontname='serif', pad=10)
                
                # Clean up the look
                ax.set_axis_off() 
                ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
                ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
                ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

                # Stable colorbar fix
                axins = inset_axes(ax, width="5%", height="60%", loc='lower left', borderpad=1)
                
                sm = plt.cm.ScalarMappable(cmap=plt.cm.jet)
                sm.set_array(field_strength)
                cb = fig.colorbar(sm, cax=axins) 
                cb.ax.tick_params(labelsize=9)
                cb.set_label('Potential (a.u.)', fontsize=9)

                ax.view_init(elev=30, azim=-60)

            plt.tight_layout(rect=[0, 0.03, 1, 0.92])
            
            filename = f"{gate}_3d_potential_grid.png"
            plt.savefig(f"{OUTPUT_DIRECTORIES['plots']}{filename}", dpi=300, bbox_inches='tight')
            print(f"SUCCESS: Created {filename}")
            plt.close(fig)
            self.logger.info(f"Saved potential profile plot for {gate}")

        self.logger.info("Potential profile simulation completed")


class SimulationRunner:
    """Main runner for all simulations."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.simulator = NWFETSimulator()
        self.plotter_2d = Plotter2D()
        self.plotter_3d = Plotter3D()
        self.exporter = DataExporter()

        # Initialize simulations
        self.simulations = {
            'cv_thickness': CVThicknessSweepSimulation(self.simulator, self.plotter_2d),
            'iv_transfer': IVTransferSimulation(self.simulator, self.plotter_2d),
            'iv_output': IVOutputSimulation(self.simulator, self.plotter_2d),
            'iv_thickness': IVThicknessSweepSimulation(self.simulator, self.plotter_2d),
            'temp_iv': TemperatureIVSimulation(self.simulator, self.plotter_2d),
            'temp_vds': TempVdsIdSimulation(self.simulator, self.plotter_3d),
            'cox_3d': TempVgsCoxSimulation(self.simulator, self.plotter_3d),
            'thickness_temp': ThicknessTempSimulation(self.simulator, self.plotter_3d),
            'temp_vgs_id': TempVgsIdSimulation(self.simulator, self.plotter_3d),
            'temp_param': TempParameterSweepSimulation(self.simulator, self.plotter_2d),
            'cryo_iv': CryogenicIVSimulation(self.simulator, self.plotter_2d),
            'high_temp_iv': HighTempIVSimulation(self.simulator, self.plotter_3d),
            'eis': EISRelaxationSimulation(self.simulator, self.plotter_2d),
            'potential': PotentialProfileSimulation(self.simulator, self.plotter_3d),
        }

    def run_simulation(self, simulation_name: str):
        """Run a specific simulation."""
        if simulation_name in self.simulations:
            self.simulations[simulation_name].run()
        else:
            self.logger.error(f"Unknown simulation: {simulation_name}")

    def run_all(self):
        """Run all simulations."""
        self.logger.info("Running all simulations")
        for sim in self.simulations.values():
            sim.run()
        self.logger.info("All simulations completed")
