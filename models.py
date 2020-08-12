from utils import convert_mt_to_ft


# TODO: add assertions for the parameters
class SolarPanel:
    # assuming the panel as fixed orientation
    def __init__(self, area_sqm, efficiency, liq_heat_capacity=4179.6):
        # assuming water for default
        self._area = area_sqm
        self._eff = efficiency
        self._capacity = liq_heat_capacity

    def heat_generated(self, rad_w_msq):
        return self._area * rad_w_msq * self._eff

    def temp_out(self, solar_heat_j, temp_k, volume_l):
        return temp_k + solar_heat_j / (volume_l * self._capacity)


class Pump:
    def __init__(self, power_hp, efficiency, friction_loss, flow=249.837192):
        self._power = power_hp
        self._eff = efficiency
        self._f_loss = friction_loss
        self._flow = flow

    def flow_quantity(self, dist_m):
        return self._flow * self._power * self._eff / convert_mt_to_ft(dist_m + self._f_loss)


class StorageTank:
    def __init__(self, tank_vol_l, tank_in_h_m, tank_out_h_m, tank_temp_k, tank_in_heat_loss_p_sec,
                 liq_heat_capacity=4179.6, init_tank_energy=0):
        assert tank_in_h_m > tank_out_h_m, "Input must be above the output"
        self._tank_vol = tank_vol_l
        self._liq_vol = tank_vol_l  # assuming full occupancy at reset
        self._pumping_h = tank_in_h_m - tank_out_h_m
        self._tank_temp = tank_temp_k
        self._init_temp = tank_temp_k
        self._tank_energy = init_tank_energy
        self._tank_heat_loss = tank_in_heat_loss_p_sec
        self._liq_capacity = liq_heat_capacity

    def get_pumping_h(self):
        return self._pumping_h

    def get_tank_temp(self):
        return self._tank_temp

    def get_tank_energy(self):
        return self._tank_energy

    def get_volume_liq(self):
        return self._liq_vol

    def reset(self):
        self._tank_temp = self._init_temp
        self._tank_energy = 0
        self._liq_vol = self._tank_vol

    def heat_loss_step(self):
        loss = max(0, 0.0 * self._tank_heat_loss * self._tank_energy)
        self._tank_energy -= loss
        self._tank_temp += (-1 * loss) / (self._liq_vol * self._liq_capacity)

    def heat_loss_out(self, vol_out):
        self._tank_energy -= ((self._tank_energy / self._liq_vol) * vol_out)
        self._liq_vol -= vol_out

    def heat_gain_in(self, vol_in, heat_in_j):
        self._tank_energy += heat_in_j
        self._liq_vol += min(vol_in, self._tank_vol)
        self._tank_temp += heat_in_j / (self._liq_vol * self._liq_capacity)
