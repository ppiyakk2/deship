import os
import serial

from deship.lib.logger import Logger, init_logger
from deship.database import rule, monitor

init_logger()


def run():
    pid = os.fork()
    device_id = 'MSIP-CCM-HUW-H1512'

    if pid == 0:
        Logger.common_logger.info('Starting Device Manager')
        ser = serial.Serial('/dev/ttyUSB0')
        while True:
            value = int(ser.read(3))

            if value > 600:
                value = 600

            value_percent = value / 600.0 * 100

            r = rule.get_device_rule(device_id)

            alarm = False
            if value_percent < float(r['alarm_critera']):
                alarm = True

            monitor.save_sensor_data(device_id, value_percent, alarm)

            if value_percent < float(r['criteria']):
                if not monitor.is_ordered(device_id, r['item_id']):
                    monitor.do_order(device_id, r['item_id'])
            else:
                monitor.delete_ordered_record(device_id, r['item_id'])

    else:
        return pid
