# coding=UTF-8

import logging
from bluepy import btle
import struct


class InkbirdIBSTH():
    
    VALID_SENSOR_TYPES = ['Inkbird_IBSTH1', 'Inkbird_IBSTH2']
    IBSTH1_CHARACTERISTIC = 0x28
    IBSTH1_FORMAT = '<hhBBB'
    IBSTH2_CHARACTERISTIC = 0x24
    IBSTH2_FORMAT = '<hhBBB'
    
    def __init__(self, mac_address, sensor_type, humidity_offset=0):
        self.mac_address = mac_address
        self.sensor_type = sensor_type
        self.humidity_offset = humidity_offset
        return
    
    def _peripheral(self):
        return btle.Peripheral(self.mac_address)
    
    def read_sensor(self):
        try:
            peripheral = self._peripheral()
            if self.sensor_type == 'Inkbird_IBSTH1':
                characteristic = peripheral.readCharacteristic(self.IBSTH1_CHARACTERISTIC)
                return self._decode_sensor_data(self.IBSTH1_FORMAT, characteristic)
            elif self.sensor_type == 'Inkbird_IBSTH2':
                characteristic = peripheral.readCharacteristic(self.IBSTH2_CHARACTERISTIC)
                return self._decode_sensor_data(self.IBSTH2_FORMAT, characteristic)
            else:
                error_message = f'Sensor type must be one of: {self.VALID_SENSOR_TYPES}'
                logging.error(error_message)
                raise(error_message)
        except:
            logging.warning(f'Failed to read sensor for {self.mac_address}')

    def _decode_sensor_data(self, format_binary, valueBinary):
        (temp, humid, unknown1, unknown2, unknown3) = struct.unpack(format_binary, valueBinary)
        temperature_celcius = float(temp) / 100
        sensorValue = {
                'sensor_type': self.sensor_type,
                'temperature_celcius': temperature_celcius,
                'temperature_farenheit': round((temperature_celcius*1.8) + 32, 2),
                'humidity': round((float(humid) / 100) + self.humidity_offset, 2),
            }
        return sensorValue
    
    def _read_sensor_characteristics(self):
        try:
            peripheral = self._peripheral()
            characteristics = peripheral.getCharacteristics()
            peripheral.disconnect()
            return characteristics
        except:
            logging.warning(f'Failed to read characteristics for {self.mac_address}')
