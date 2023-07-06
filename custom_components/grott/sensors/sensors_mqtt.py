"""Sensor descriptions for Growatt systems - Raw MQTT values."""
from __future__ import annotations

import datetime

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.helpers.entity import DeviceInfo, EntityCategory
from homeassistant.util import dt

from ..const import (
    BATTERY_TYPES
)

def battery_type_lookup(mqtt_data):
  batt_type=mqtt_data['values']['batterytype']
  if batt_type > 1:
    batt_type = 2
  return BATTERY_TYPES[int(batt_type)]

def datetime_formatter(mqtt_data):
  last_updated_time_string = mqtt_data['time']
  last_updated_date_time = dt.parse_datetime(last_updated_time_string)
  return datetime.datetime.combine(last_updated_date_time.date(), last_updated_date_time.time(), dt.DEFAULT_TIME_ZONE)

SENSORS_LABEL="raw_mqtt_sensors"

SENSORS = [
  {
    "name": "PV Serial",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["pvserial"],
    "unique_name": "mqtt_001",
  },
  {
    "name": "Datalog Serial",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["datalogserial"],
    "unique_name": "mqtt_002",
  },
  {
    "name": "PV Status",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["pvstatus"],
    "unique_name": "mqtt_003",
  },
  {
    "name": "PV-All Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvpowerin"],
    "divider": 10,
    "unique_name": "mqtt_004",
  },
  {
    "name": "PV1 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1voltage"],
    "divider": 10,
    "unique_name": "mqtt_005",
  },
  {
    "name": "PV1 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1current"],
    "divider": 10,
    "unique_name": "mqtt_006",
  },
  {
    "name": "PV1 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1watt"],
    "divider": 10,
    "unique_name": "mqtt_007",
  },
  {
    "name": "PV2 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2voltage"],
    "divider": 10,
    "unique_name": "mqtt_008",
  },
  {
    "name": "PV2 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2current"],
    "divider": 10,
    "unique_name": "mqtt_009",
  },
  {
    "name": "PV2 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2watt"],
    "divider": 10,
    "unique_name": "mqtt_010",
  },
  {
    "name": "PV3 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv3voltage"],
    "divider": 10,
    "unique_name": "mqtt_066",
  },
  {
    "name": "PV3 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv3current"],
    "divider": 10,
    "unique_name": "mqtt_067",
  },
  {
    "name": "PV3 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv3watt"],
    "divider": 10,
    "unique_name": "mqtt_068",
  },
  {
    "name": "PV4 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv4voltage"],
    "divider": 10,
    "unique_name": "mqtt_072",
  },
  {
    "name": "PV4 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv4current"],
    "divider": 10,
    "unique_name": "mqtt_073",
  },
  {
    "name": "PV4 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv4watt"],
    "divider": 10,
    "unique_name": "mqtt_074",
  },
  {
    "name": "Output Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvpowerout"],
    "divider": 10,
    "unique_name": "mqtt_011",
  },

  {
    "name": "Grid Frequency",
    "device_class": SensorDeviceClass.FREQUENCY,
    "unit_of_measurement": UnitOfFrequency.HERTZ,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:sine-wave",
    "func": lambda js: js['values']["pvfrequentie"],
    "divider": 100,
    "unique_name": "mqtt_012",
  },

  {
    "name": "Inverter Output Voltage (Single/First Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage"],
    "divider": 10,
    "unique_name": "mqtt_013",
  },
  {
    "name": "Inverter Output Current (Single/First Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent"],
    "divider": 10,
    "unique_name": "mqtt_014",
  },
  {
    "name": "Inverter Output Power (Single/First Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower"],
    "divider": 10,
    "unique_name": "mqtt_015",
  },
  {
    "name": "Inverter Output Voltage (Second Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage2"],
    "divider": 10,
    "unique_name": "mqtt_016",
  },
  {
    "name": "Inverter Output Current (Second Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent2"],
    "divider": 10,
    "unique_name": "mqtt_017",
  },
  {
    "name": "Inverter Output Power (Second Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower2"],
    "divider": 10,
    "unique_name": "mqtt_018",
  },
  {
    "name": "Inverter Output Voltage (Third Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage3"],
    "divider": 10,
    "unique_name": "mqtt_019",
  },
  {
    "name": "Inverter Output Current (Third Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent3"],
    "divider": 10,
    "unique_name": "mqtt_020",
  },
  {
    "name": "Inverter Output Power (Third Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower3"],
    "divider": 10,
    "unique_name": "mqtt_021",
  },

  {
    "name": "Time Since Commissioned",
    "device_class": SensorDeviceClass.DURATION,
    "unit_of_measurement": UnitOfTime.HOURS,
    "state_class": SensorStateClass.TOTAL,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:clock",
    "func": lambda js: js['values']["totworktime"],
    "divider": 7200,
    "unique_name": "mqtt_022",
  },
 
  {
    "name": "Power Geneartion - Today (eactoday)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactoday"],
    "divider": 10,
    "unique_name": "mqtt_023",
  },
  {
    "name": "Power Generation - Today (pvenergytoday)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvenergytoday"],
    "divider": 10,
    "unique_name": "mqtt_024",
  },
  {
    "name": "Power Generation - Total (eactotal)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactotal"],
    "divider": 10,
    "unique_name": "mqtt_025",
  },
  {
    "name": "Power Generation - Total (pvenergytotal)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvenergytotal"],
    "divider": 10,
    "unique_name": "mqtt_071",
  },

  {
    "name": "PV1 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1today"],
    "divider": 10,
    "unique_name": "mqtt_026",
  },
  {
    "name": "PV1 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1total"],
    "divider": 10,
    "unique_name": "mqtt_027",
  },
  {
    "name": "PV2 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2today"],
    "divider": 10,
    "unique_name": "mqtt_028",
  },
  {
    "name": "PV2 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2total"],
    "divider": 10,
    "unique_name": "mqtt_029",
  },
  {
    "name": "PV3 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv3today"],
    "divider": 10,
    "unique_name": "mqtt_069",
  },
  {
    "name": "PV3 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv3total"],
    "divider": 10,
    "unique_name": "mqtt_070",
  },
  {
    "name": "PV4 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv4today"],
    "divider": 10,
    "unique_name": "mqtt_075",
  },
  {
    "name": "PV4 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv4total"],
    "divider": 10,
    "unique_name": "mqtt_076",
  },

  {
    "name": "PV-All Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epvtotal"],
    "divider": 10,
    "unique_name": "mqtt_030",
  },

  {
    "name": "Inverter Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvtemperature"],
    "divider": 10,
    "unique_name": "mqtt_031",
  },
  {
    "name": "IPM Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvipmtemperature"],
    "divider": 10,
    "unique_name": "mqtt_032",
  },
  {
    "name": "Boost Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvboosttemp"],
    "divider": 10,
    "unique_name": "mqtt_033",
  },
  {
    "name": "Bat DSP",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["bat_dsp"],
    "divider": 10,
    "unique_name": "mqtt_034",
  },

  {
    "name": "Battery AC Charge Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eacharge_today"],
    "divider": 10,
    "unique_name": "mqtt_035",
  },
  {
    "name": "Battery AC Charge Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eacharge_total"],
    "divider": 10,
    "unique_name": "mqtt_036",
  },

  {
    "name": "Battery Type",
    "device_class": SensorDeviceClass.ENUM,
    "options": BATTERY_TYPES,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": battery_type_lookup,
    "unique_name": "mqtt_037",
  },

  #TODO - Convert to an ENUM
  #0x00:waiting module 
  #0x01: Self-test mode,
  #      optional
  #0x02: Reserved
  #0x03：SysFault module 
  #0x04: Flash module
  #0x05：PVBATOnline module, 
  #0x06：BatOnline module 
  #0x07：PVOfflineMode module, 
  #0x08：BatOfflineMode module,
  {
    "name": "System Work Mode",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["uwsysworkmode"],
    "unique_name": "mqtt_038",
  },


  {
    "name": "System Fault Word 0",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword0"],
    "unique_name": "mqtt_039",
  },
  {
    "name": "System Fault Word 1",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword1"],
    "unique_name": "mqtt_040",
  },
  {
    "name": "System Fault Word 2",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword2"],
    "unique_name": "mqtt_041",
  },
  {
    "name": "System Fault Word 3",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword3"],
    "unique_name": "mqtt_042",
  },
  {
    "name": "System Fault Word 4",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword4"],
    "unique_name": "mqtt_043",
  },
  {
    "name": "System Fault Word 5",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword5"],
    "unique_name": "mqtt_044",
  },
  {
    "name": "System Fault Word 6",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword6"],
    "unique_name": "mqtt_045",
  },
  {
    "name": "System Fault Word 7",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword7"],
    "unique_name": "mqtt_046",
  },

  {
    "name": "Battery Discharging Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["pdischarge1"],
    "divider": 10,
    "unique_name": "mqtt_047",
  },
  {
    "name": "Battery Charging Power", #SPH systems
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["p1charge1"],
    "divider": 10,
    "unique_name": "mqtt_048",
  },
  {
    "name": "Battery Charging Power", #SPA/AC Couple systems
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["pcharge1"],
    "divider": 10,
    "unique_name": "mqtt_086",
  },

  {
    "name": "Battery Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["vbat"],
    "divider": 10,
    "unique_name": "mqtt_049",
  },
  {
    "name": "State of Charge",
    "device_class": SensorDeviceClass.BATTERY,
    "unit_of_measurement": PERCENTAGE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["SOC"],
    "divider": 1,
    "unique_name": "mqtt_050",
  },

  {
    "name": "Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["pactouserr"],
    "divider": 10,
    "unique_name": "mqtt_051",
  },
#  {
#    "name": "Import from Grid Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-import-outline",
#    "func": lambda js: js['values']["pactousertot"],
#    "divider": 10
#  },

  {
    "name": "Export to Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-export-outline",
    "func": lambda js: js['values']["pactogridr"],
    "divider": 10,
    "unique_name": "mqtt_052",
  },
#  {
#    "name": "Export to Grid Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-export-outline",
#    "func": lambda js: js['values']["pactogridtot"],
#    "divider": 10
#  },

  {
    "name": "Load Consumption Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["plocaloadr"],
    "divider": 10,
    "unique_name": "mqtt_053",
  },
#  {
#    "name": "Load Consumption Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-lightning-bolt",
#    "func": lambda js: js['values']["plocaloadtot"],
#    "divider": 10
#  },


  #TODO - This might be an enum
  {
    "name": "SP State",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["spdspstatus"],
    "unique_name": "mqtt_054",
  },

  {
    "name": "SP Bus Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["spbusvolt"],
    "divider": 10,
    "unique_name": "mqtt_055",
  },

  {
    "name": "Import from Grid Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etouser_tod"],
    "divider": 10,
    "unique_name": "mqtt_056",
  },
  {
    "name": "Import from Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etouser_tot"],
    "divider": 10,
    "unique_name": "mqtt_057",
  },
  {
    "name": "Export to Grid Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-export-outline",
    "func": lambda js: js['values']["etogrid_tod"],
    "divider": 10,
    "unique_name": "mqtt_058",
  },
  {
    "name": "Export to Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etogrid_tot"],
    "divider": 10,
    "unique_name": "mqtt_059",
  },

  {
    "name": "Battery Discharged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischarge1_tod"],
    "divider": 10,
    "unique_name": "mqtt_060",
  },
  {
    "name": "Battery Discharged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischarge1_tot"],
    "divider": 10,
    "unique_name": "mqtt_061",
  },

  {
    "name": "Battery Charged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eharge1_tod"],
    "divider": 10,
    "unique_name": "mqtt_062",
  },
  {
    "name": "Battery Charged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eharge1_tot"],
    "divider": 10,
    "unique_name": "mqtt_063",
  },

  {
    "name": "Load Consumption Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["elocalload_tod"],
    "divider": 10,
    "unique_name": "mqtt_064",
  },
  {
    "name": "Load Consumption Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["elocalload_tot"],
    "divider": 10,
    "unique_name": "mqtt_065",
  },

  #BMS values, relevant for 'min' systems
  {
    "name": "State of Charge",
    "device_class": SensorDeviceClass.BATTERY,
    "unit_of_measurement": PERCENTAGE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["bms_soc"],
    "divider": 1,
    "unique_name": "mqtt_078",
  },
  {
    "name": "Battery Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["bms_batteryvolt"],
    "divider": 100,
    "unique_name": "mqtt_079",
  },
  {
    "name": "Battery Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["bms_batterycurr"],
    "divider": 100,
    "unique_name": "mqtt_080",
  },
  {
    "name": "Battery Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["bms_batterytemp"],
    "divider": 10,
    "unique_name": "mqtt_081",
  },
  {
    "name": "Battery Discharged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischrtoday"],
    "divider": 10,
    "unique_name": "mqtt_082",
  },
  {
    "name": "Battery Discharged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischrtotal"],
    "divider": 10,
    "unique_name": "mqtt_083",
  },
  {
    "name": "Battery Charged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["echrtoday"],
    "divider": 10,
    "unique_name": "mqtt_084",
  },
  {
    "name": "Battery Charged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["echrtotal"],
    "divider": 10,
    "unique_name": "mqtt_085",
  },


  #SDM systems/meters
  {
    "name": "Phase1 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["voltage_l1"],
    "divider": 10,
    "unique_name": "mqtt_087",
  },
  {
    "name": "Phase2 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["voltage_l1"],
    "divider": 10,
    "unique_name": "mqtt_088",
  },
  {
    "name": "Phase3 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["voltage_l1"],
    "divider": 10,
    "unique_name": "mqtt_089",
  },

  {
    "name": "Phase1 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["Current_l1"],
    "divider": 10,
    "unique_name": "mqtt_090",
  },
  {
    "name": "Phase2 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["Current_l2"],
    "divider": 10,
    "unique_name": "mqtt_091",
  },
  {
    "name": "Phase3 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["Current_l3"],
    "divider": 10,
    "unique_name": "mqtt_092",
  },

  {
    "name": "Phase1 Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["act_power_l1"],
    "divider": 10,
    "unique_name": "mqtt_093",
  },
  {
    "name": "Phase2 Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["act_power_l2"],
    "divider": 10,
    "unique_name": "mqtt_094",
  },
  {
    "name": "Phase3 Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["act_power_l3"],
    "divider": 10,
    "unique_name": "mqtt_095",
  },
  {
    "name": "Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["pos_rev_act_power"],
    "divider": 10,
    "unique_name": "mqtt_096",
  },
  {
    "name": "Import from Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["pos_act_energy"],
    "divider": 10,
    "unique_name": "mqtt_097",
  },
  {
    "name": "Export to Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-export-outline",
    "func": lambda js: js['values']["rev_act_energy"],
    "divider": 10,
    "unique_name": "mqtt_098",
  },

  {
    "name": "Last data update",
    "device_class": SensorDeviceClass.TIMESTAMP,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": datetime_formatter,
    "unique_name": "mqtt_099",
  },


  #The following entries are out-of-order in the above list, be sure to check for the latest value for unique_name from both lists
  #mqtt_066 - PV3 Voltage
  #mqtt_067 - PV3 Current
  #mqtt_068 - PV3 Power
  #mqtt_069 - PV3 Energy - Today
  #mqtt_070 - PV3 Energy - Total
  #mqtt_071 - Power Generation - Total (pvenergytotal)
  #mqtt_072 - PV4 Voltage
  #mqtt_073 - PV4 Current
  #mqtt_074 - PV4 Power
  #mqtt_075 - PV4 Energy - Today
  #mqtt_076 - PV4 Energy - Total
  #mqtt_086 - Battery Charging Power (AC Coupled)
]

