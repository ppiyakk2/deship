import json

from .models import Device


def addDeviceInfo(info):
    device = Device(info['SN'], info['device_name'], info['device_type'],
                    info['productive_date'])
    device.save()


def getAllDevice():
    return Device.select_all()
