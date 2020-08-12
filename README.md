# Solar Heat Transfer Simulation

This simulation builds a model for Solar Panel, Storage Tank and Pump to simulate the heat 
transfer from the Panel to the Tank by means of solar radiation. 
The simulation prints out the information at each timestep. 
To run the simulation with default values: 
```
> python simulation.py
```

Provide inputs in the path to simulate various conditions.
```
> python simulation.py -h
usage: simulation.py [-h] [-ca COLLECTOR_AREA_SQM]
                     [-ce {COLLECTOR_EFFICIENCY [0.0,1.0]}]
                     [-tf TRANSMISSION_FRICTION_M] [-pp PUMP_POWER_HP]
                     [-pe {PUMP_EFFICIENCY [0.0,1.0]}] [-tv TANK_VOL_L]
                     [-ti TANK_IN_FLOW_HEIGHT_M] [-to TANK_OUT_FLOW_HEIGHT_M]
                     [-tl {TANK_HEAT_LOSS_FACTOR [0.0,1.0]}] [-it INIT_TEMP_K]
                     [-s STEPS]

User Input for the Simulation of Solar water heater

optional arguments:
  -h, --help            show this help message and exit
  -ca COLLECTOR_AREA_SQM, --collector_area_sqm COLLECTOR_AREA_SQM
                        Area of the Solar Panel in Sq.Mt.
  -ce {COLLECTOR_EFFICIENCY [0.0,1.0]}, --collector_efficiency {COLLECTOR_EFFICIENCY [0.0,1.0]}
                        Efficiency of the Solar Panel
  -tf TRANSMISSION_FRICTION_M, --transmission_friction_m TRANSMISSION_FRICTION_M
                        Friction of the pipe in Mt.
  -pp PUMP_POWER_HP, --pump_power_hp PUMP_POWER_HP
                        Power of pump in HP
  -pe {PUMP_EFFICIENCY [0.0,1.0]}, --pump_efficiency {PUMP_EFFICIENCY [0.0,1.0]}
                        Efficiency of the Pump
  -tv TANK_VOL_L, --tank_vol_l TANK_VOL_L
                        Volume of Tank in Lit
  -ti TANK_IN_FLOW_HEIGHT_M, --tank_in_flow_height_m TANK_IN_FLOW_HEIGHT_M
                        Inflow height for tank in Mt
  -to TANK_OUT_FLOW_HEIGHT_M, --tank_out_flow_height_m TANK_OUT_FLOW_HEIGHT_M
                        Outflow height for tank in Mt
  -tl {TANK_HEAT_LOSS_FACTOR [0.0,1.0]}, --tank_heat_loss_factor {TANK_HEAT_LOSS_FACTOR [0.0,1.0]}
                        Heat Loss Per Second factor for tank
  -it INIT_TEMP_K, --init_temp_k INIT_TEMP_K
                        Initial temp in Kelvin
  -s STEPS, --steps STEPS
                        Number of steps to run the simulation
```