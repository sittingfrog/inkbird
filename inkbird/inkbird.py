# https://qiita.com/revsystem/items/4097d0ff447913e2675a
# https://github.com/rockstar2020/Inkbird_IBS-TH2_Scanner/blob/main/Inkbird.py
# coding=UTF-8

from bluepy import btle
import struct


class InkbirdIBSTH():
    
    VALID_SENSOR_TYPES = ['Inkbird_IBSTH1', 'Inkbird_IBSTH2']
    IBSTH1_CHARACTERISTIC = 0x28
    IBSTH1_FORMAT = '<hhBBB'
    IBSTH2_CHARACTERISTIC = 0x24
    IBSTH2_FORMAT = '<hhBBB'
    
    def __init__(self, mac_address, sensor_type):
        self.mac_address = mac_address
        self.sensor_type = sensor_type
        return
    
    def get_ibsth_data(self):
        peripheral = btle.Peripheral(self.mac_address)

        if self.sensor_type == 'Inkbird_IBSTH1':
            characteristic = peripheral.readCharacteristic(self.IBSTH1_CHARACTERISTIC)
            return self._decodeSensorData(self.IBSTH1_FORMAT, characteristic)
        elif self.sensor_type == 'Inkbird_IBSTH2':
            characteristic = peripheral.readCharacteristic(self.IBSTH2_CHARACTERISTIC)
            return self._decodeSensorData(self.IBSTH2_FORMAT, characteristic)
        else:
            return None

    def _decodeSensorData(self, format_binary, valueBinary):
        (temp, humid, unknown1, unknown2, unknown3) = struct.unpack(format_binary, valueBinary)
        temperature_celcius = float(temp) / 100
        sensorValue = {
                'sensor_type': self.sensor_type,
                'temperature_celcius': temperature_celcius,
                'temperature_farenheit': round((temperature_celcius*1.8) + 32, 2),
                'humidity': float(humid) / 100,
                'unknown1': unknown1,
                'unknown2': unknown2,
                'unknown3': unknown3,
            }
        return sensorValue
