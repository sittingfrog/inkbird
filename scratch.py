import os
import json
import yaml

from inkbird import InkbirdIBSTH

print(f'pwd is: {os.getcwd()}\n')
class THMonitor():
    def __init__(self, config_yaml='sensors.yaml'):
        with open(config_yaml) as file:
            yaml_content = yaml.safe_load(file)
        for d in yaml_content['sensors']:
            d['device'] = InkbirdIBSTH(d['mac_address'], d['sensor_type'])
        self.sensors = yaml_content['sensors']
        

    def get_sensor_data(self):
        for d in self.sensors:
            d['last_reading'] = d['device'].get_ibsth_data()
            
thm = THMonitor()
thm.get_sensor_data()

print(json.dumps(thm.sensors, indent=2, default=str))
    
