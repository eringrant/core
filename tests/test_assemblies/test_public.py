import numpy as np
import pytest

from brainscore.assemblies.public import load_assembly


@pytest.mark.private_access
@pytest.mark.memory_intense
class TestMajaj2015Temporal:
    def test_majaj2015TemporalLowvar(self):
        assembly = load_assembly('dicarlo.Majaj2015.temporal.public')
        assert assembly.attrs['stimulus_set_name'] == 'dicarlo.hvm-public'
        assert len(assembly['presentation']) == 3200
        assert len(assembly['neuroid']) == 256
        assert len(assembly.sel(region='IT')['neuroid']) == 168
        assert len(assembly.sel(region='V4')['neuroid']) == 88
        assert len(assembly['time_bin']) == 39
        np.testing.assert_array_equal(assembly['time_bin_start'], list(range(-100, 281, 10)))
        np.testing.assert_array_equal(assembly['time_bin_end'], list(range(-80, 301, 10)))

    def test_majaj2015ITTemporalLowvar(self):
        assembly = load_assembly('dicarlo.Majaj2015.temporal.public.IT')
        assert assembly.attrs['stimulus_set_name'] == 'dicarlo.hvm-public'
        assert set(assembly['region'].values) == {'IT'}
        assert len(assembly['presentation']) == 3200
        assert len(assembly['neuroid']) == 168
        assert len(assembly['time_bin']) == 39
        np.testing.assert_array_equal(assembly['time_bin_start'], list(range(-100, 281, 10)))
        np.testing.assert_array_equal(assembly['time_bin_end'], list(range(-80, 301, 10)))

    def test_majaj2015V4TemporalLowvar(self):
        assembly = load_assembly('dicarlo.Majaj2015.temporal.public.V4')
        assert assembly.attrs['stimulus_set_name'] == 'dicarlo.hvm-public'
        assert set(assembly['region'].values) == {'V4'}
        assert len(assembly['presentation']) == 3200
        assert len(assembly['neuroid']) == 88
        assert len(assembly['time_bin']) == 39
        np.testing.assert_array_equal(assembly['time_bin_start'], list(range(-100, 281, 10)))
        np.testing.assert_array_equal(assembly['time_bin_end'], list(range(-80, 301, 10)))


@pytest.mark.private_access
@pytest.mark.memory_intense
class TestFreemanZiemba2013Temporal:
    def test_v1(self):
        assembly = load_assembly('movshon.FreemanZiemba2013.temporal.public.V1')
        assert len(assembly['presentation']) == 135
        assert len(assembly['neuroid']) == 102
        np.testing.assert_array_equal(assembly['time_bin_start'], list(range(0, 291, 10)))
        np.testing.assert_array_equal(assembly['time_bin_end'], list(range(10, 301, 10)))

    def test_v2(self):
        assembly = load_assembly('movshon.FreemanZiemba2013.temporal.public.V2')
        assert len(assembly['presentation']) == 135
        assert len(assembly['neuroid']) == 103
        np.testing.assert_array_equal(assembly['time_bin_start'], list(range(0, 291, 10)))
        np.testing.assert_array_equal(assembly['time_bin_end'], list(range(10, 301, 10)))
