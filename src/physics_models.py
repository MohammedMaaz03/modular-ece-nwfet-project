"""
Physics models for NWFET simulations.
Contains classes and methods for analytical calculations.
"""

import numpy as np
import logging
from config.constants import (
    EPS0, ELEMENTARY_CHARGE, BOLTZMANN_CONSTANT,
    DEVICE_PARAMETERS, MATERIALS, GATE_CONFIGURATIONS
)


class CapacitanceVoltageModel:
    """Model for capacitance-voltage characteristics."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_capacitance(
        self,
        voltage: np.ndarray,
        dielectric_constant: float,
        oxide_thickness: float,
        gate_efficiency: float,
        flatband_shift: float,
        dip_width: float
    ) -> np.ndarray:
        """
        Calculate C-V characteristics.

        Args:
            voltage: Gate voltage array (V)
            dielectric_constant: k value of dielectric
            oxide_thickness: tox (m)
            gate_efficiency: eta factor
            flatband_shift: V_fb shift (V)
            dip_width: Width parameter for dip

        Returns:
            Capacitance array (F/m²)
        """
        self.logger.debug("Calculating capacitance-voltage characteristics")
        c_max = (EPS0 * dielectric_constant) / oxide_thickness
        dip_depth = 0.5 * (dielectric_constant / 3.9) ** 0.1
        flatband_voltage = flatband_shift
        capacitance = c_max * gate_efficiency * (
            1 - dip_depth * np.exp(-(voltage - flatband_voltage) ** 2 / dip_width)
        )
        return capacitance


class CurrentVoltageModel:
    """Model for current-voltage characteristics."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_drain_current(
        self,
        gate_voltage: np.ndarray,
        drain_voltage: float,
        oxide_capacitance: float,
        gate_efficiency: float,
        channel_width: float,
        channel_length: float,
        mobility: float,
        threshold_voltage: float,
        channel_modulation: float = 0.05
    ) -> np.ndarray:
        """
        Calculate drain current using MOSFET model.

        Args:
            gate_voltage: V_GS array (V)
            drain_voltage: V_DS (V)
            oxide_capacitance: C_ox (F/m²)
            gate_efficiency: eta
            channel_width: W (m)
            channel_length: L (m)
            mobility: μ (m²/V·s)
            threshold_voltage: V_th (V)
            channel_modulation: λ

        Returns:
            Drain current array (A)
        """
        self.logger.debug("Calculating drain current")
        drain_current = np.zeros_like(gate_voltage)
        aspect_ratio = channel_width / channel_length
        beta = mobility * oxide_capacitance * gate_efficiency * aspect_ratio

        for i, vgs in enumerate(gate_voltage):
            if vgs <= threshold_voltage:
                # Subthreshold current
                vt = BOLTZMANN_CONSTANT * 300 / ELEMENTARY_CHARGE  # ~0.0259V at 300K
                drain_current[i] = 1e-12 * np.exp((vgs - threshold_voltage) / (1.5 * vt))
            else:
                overdrive_voltage = vgs - threshold_voltage
                if drain_voltage < overdrive_voltage:
                    # Linear region
                    drain_current[i] = beta * (overdrive_voltage * drain_voltage - 0.5 * drain_voltage ** 2)
                else:
                    # Saturation region
                    drain_current[i] = 0.5 * beta * overdrive_voltage ** 2 * (1 + channel_modulation * drain_voltage)

        return drain_current


class ImpedanceModel:
    """Model for electrochemical impedance spectroscopy."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_impedance(
        self,
        frequency: np.ndarray,
        temperature: float,
        series_resistance: float,
        gate_efficiency: float,
        dielectric_constant: float,
        capacitance_factor: float,
        reference_temperature: float = 300
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Calculate EIS impedance components.

        Args:
            frequency: Frequency array (Hz)
            temperature: T (K)
            series_resistance: R_s (Ω)
            gate_efficiency: eta
            dielectric_constant: k
            capacitance_factor: C0
            reference_temperature: T_ref (K)

        Returns:
            Tuple of real and imaginary impedance (Ω)
        """
        self.logger.debug("Calculating impedance")
        angular_frequency = 2 * np.pi * frequency
        relaxation_time = (1e-6 / (dielectric_constant ** 0.5)) * np.exp(500 / temperature)
        parallel_resistance = 1e6 * (reference_temperature / temperature)

        real_impedance = series_resistance + parallel_resistance / (
            1 + (angular_frequency * relaxation_time) ** 2
        )
        imaginary_impedance = parallel_resistance * (angular_frequency * relaxation_time) / (
            1 + (angular_frequency * relaxation_time) ** 2
        )

        return real_impedance, imaginary_impedance / gate_efficiency


class MobilityModel:
    """Model for temperature-dependent mobility."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_mobility(
        self,
        reference_mobility: float,
        temperature: float,
        reference_temperature: float = 300
    ) -> float:
        """
        Calculate temperature-dependent mobility.

        Args:
            reference_mobility: μ0 at T_ref
            temperature: T (K)
            reference_temperature: T_ref (K)

        Returns:
            Mobility (m²/V·s)
        """
        self.logger.debug("Calculating mobility")
        return reference_mobility * (temperature / reference_temperature) ** (-1.5)


class ThresholdVoltageModel:
    """Model for temperature-dependent threshold voltage."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_threshold_voltage(
        self,
        reference_threshold: float,
        temperature: float,
        temperature_coefficient: float,
        reference_temperature: float = 300
    ) -> float:
        """
        Calculate temperature-dependent V_th.

        Args:
            reference_threshold: V_th0 at T_ref
            temperature: T (K)
            temperature_coefficient: α
            reference_temperature: T_ref (K)

        Returns:
            Threshold voltage (V)
        """
        self.logger.debug("Calculating threshold voltage")
        return reference_threshold - temperature_coefficient * (temperature - reference_temperature)


class NWFETSimulator:
    """Main simulator class integrating all models."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.cv_model = CapacitanceVoltageModel()
        self.iv_model = CurrentVoltageModel()
        self.impedance_model = ImpedanceModel()
        self.mobility_model = MobilityModel()
        self.vth_model = ThresholdVoltageModel()

        self.logger.info("NWFET Simulator initialized")

    def get_material_properties(self, material_name: str) -> list:
        """Get material properties."""
        return MATERIALS[material_name]

    def get_gate_properties(self, gate_name: str) -> dict:
        """Get gate configuration."""
        return GATE_CONFIGURATIONS[gate_name]

    def simulate_cv(
        self,
        material_name: str,
        gate_name: str,
        voltage: np.ndarray,
        oxide_thickness: float = None
    ) -> np.ndarray:
        """
        Simulate C-V characteristics.

        Args:
            material_name: Material key
            gate_name: Gate key
            voltage: Voltage array
            oxide_thickness: tox (uses default if None)

        Returns:
            Capacitance array
        """
        self.logger.info(f"Simulating C-V for {material_name} on {gate_name}")
        material_props = self.get_material_properties(material_name)
        gate_props = self.get_gate_properties(gate_name)

        k, v_shift, d_width, _ = material_props
        eta = gate_props['eta']
        tox = oxide_thickness or DEVICE_PARAMETERS['oxide_thickness']

        return self.cv_model.calculate_capacitance(voltage, k, tox, eta, v_shift, d_width)

    def simulate_iv(
        self,
        material_name: str,
        gate_name: str,
        gate_voltage: np.ndarray,
        drain_voltage: float,
        temperature: float = 300
    ) -> np.ndarray:
        """
        Simulate I-V characteristics.

        Args:
            material_name: Material key
            gate_name: Gate key
            gate_voltage: V_GS array
            drain_voltage: V_DS
            temperature: T (K)

        Returns:
            Drain current array
        """
        self.logger.info(f"Simulating I-V for {material_name} on {gate_name} at {temperature}K")
        material_props = self.get_material_properties(material_name)
        gate_props = self.get_gate_properties(gate_name)

        k = material_props[0]
        eta = gate_props['eta']
        mu_ref = gate_props['mobility_reference']

        eps0 = EPS0
        tox = DEVICE_PARAMETERS['oxide_thickness']
        w = DEVICE_PARAMETERS['channel_width']
        l = DEVICE_PARAMETERS['channel_length']
        mu0 = DEVICE_PARAMETERS['reference_mobility']
        alpha = DEVICE_PARAMETERS['temperature_coefficient']
        vth0 = DEVICE_PARAMETERS['threshold_voltage_reference']
        lambda_ch = DEVICE_PARAMETERS['channel_length_modulation']

        cox = (eps0 * k) / tox
        mu = self.mobility_model.calculate_mobility(mu0, temperature)
        vth = self.vth_model.calculate_threshold_voltage(vth0, temperature, alpha)

        return self.iv_model.calculate_drain_current(
            gate_voltage, drain_voltage, cox, eta, w, l, mu, vth, lambda_ch
        )
