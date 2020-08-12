from models import *
from utils import get_radiation_data, get_user_input


# assuming radiation is part of the environment. If needed, it can be moved out of the environment and input to step()
class SolarHeaterEnv:

    def __init__(self, collector, pump, tank):
        self.collector = collector
        self.pump = pump
        self.tank = tank
        self.rad_iterator = get_radiation_data()

    def step(self, time_step):
        rad = next(self.rad_iterator)
        if rad is None:  # this would not be required if the data keeps flowing from TMY file.
            self.rad_iterator = get_radiation_data()
            rad = next(self.rad_iterator)

        self.tank.heat_loss_step()
        water_flow = self.pump.flow_quantity(self.tank.get_pumping_h())
        self.tank.heat_loss_out(water_flow)
        heat_gen = self.collector.heat_generated(rad)
        # temp_out = self.collector.temp_out(heat_gen, self.tank.get_tank_temp(), water_flow)
        self.tank.heat_gain_in(water_flow, heat_gen)
        print("At {} - Radiation: {:.3f} Tank_Heat_Energy_J: {:.3f} Tank_Temp: {:.3f} Vol_Liq: {:.1f}"
              .format(time_step, rad, self.tank.get_tank_energy(), self.tank.get_tank_temp(), self.tank.get_volume_liq()))

    def reset(self):
        self.rad_iterator = get_radiation_data()
        self.tank.reset()


if __name__ == '__main__':
    parameters = get_user_input()

    collector_model = SolarPanel(parameters.collector_area_sqm, parameters.collector_efficiency)
    pump_model = Pump(parameters.pump_power_hp, parameters.pump_efficiency, parameters.transmission_friction_m)
    tank_model = StorageTank(parameters.tank_vol_l, parameters.tank_in_flow_height_m, parameters.tank_out_flow_height_m,
                             parameters.tank_heat_loss_factor, parameters.init_temp_k)

    print("Initiating a simulation environment with the provided values - {}".format(parameters))
    env = SolarHeaterEnv(collector_model, pump_model, tank_model)
    print("Environment Initialized. Simulating the Environment for {} steps".format(parameters.steps))

    for t in range(parameters.steps):
        env.step(t)
# TODO: add logger and change print()
