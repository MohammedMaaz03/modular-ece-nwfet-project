"""
Unit tests for physics models.
Run with: pytest tests/test_physics_models.py
"""

import numpy as np
import pytest
from src.physics_models import (
    CapacitanceVoltageModel, CurrentVoltageModel,
    MobilityModel, ThresholdVoltageModel, ImpedanceModel
)


@pytest.fixture
def cv_model():
    return CapacitanceVoltageModel()


@pytest.fixture
def iv_model():
    return CurrentVoltageModel()


@pytest.fixture
def mobility_model():
    return MobilityModel()


@pytest.fixture
def vth_model():
    return ThresholdVoltageModel()


@pytest.fixture
def impedance_model():
    return ImpedanceModel()


def test_capacitance_voltage(cv_model):
    """Test C-V calculation."""
    voltage = np.linspace(-5, 5, 10)
    k = 3.9
    tox = 1e-9
    eta = 1.0
    v_shift = 0.0
    d_width = 1.0

    capacitance = cv_model.calculate_capacitance(
        voltage, k, tox, eta, v_shift, d_width
    )

    assert capacitance.shape == voltage.shape
    assert np.all(capacitance > 0)
    # Check approximate max capacitance
    c_max_expected = (8.854e-12 * k) / tox
    assert np.isclose(np.max(capacitance), c_max_expected, rtol=0.1)


def test_current_voltage(iv_model):
    """Test I-V calculation."""
    vgs = np.array([0.5, 1.0, 1.5])
    vds = 0.5
    cox = 1e-2
    eta = 1.0
    w = 10e-9
    l = 10e-9
    mu = 0.05
    vth = 0.35

    current = iv_model.calculate_drain_current(
        vgs, vds, cox, eta, w, l, mu, vth
    )

    assert current.shape == vgs.shape
    assert np.all(current >= 0)


def test_mobility_temperature(mobility_model):
    """Test mobility temperature dependence."""
    mu0 = 0.05
    temp = 300
    mu = mobility_model.calculate_mobility(mu0, temp)
    assert mu == mu0

    temp_high = 600
    mu_high = mobility_model.calculate_mobility(mu0, temp_high)
    assert mu_high < mu0


def test_threshold_voltage_temperature(vth_model):
    """Test Vth temperature dependence."""
    vth0 = 0.35
    temp = 300
    alpha = 0.0005
    vth = vth_model.calculate_threshold_voltage(vth0, temp, alpha)
    assert vth == vth0

    temp_high = 600
    vth_high = vth_model.calculate_threshold_voltage(vth0, temp_high, alpha)
    assert vth_high < vth0


def test_impedance(impedance_model):
    """Test impedance calculation."""
    freq = np.logspace(0, 7, 10)
    temp = 300
    rs = 50
    eta = 1.0
    k = 25.0
    c0 = 1e-9

    real_z, imag_z = impedance_model.calculate_impedance(
        freq, temp, rs, eta, k, c0
    )

    assert real_z.shape == freq.shape
    assert imag_z.shape == freq.shape
    assert np.all(real_z >= rs)  # Real part should be at least series resistance
