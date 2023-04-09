ACCOUNT_BASE_URL = "https://account-fk.niu.com"
LOGIN_URI = "/appv2/login"
API_BASE_URL = "https://app-api-fk.niu.com"
MOTOR_BATTERY_API_URI = "/v3/motor_data/battery_info"
MOTOR_INDEX_API_URI = "/v3/motor_data/index_info"
MOTOINFO_LIST_API_URI = "/motoinfo/list"
MOTOINFO_ALL_API_URI = "/motoinfo/overallTally"
TRACK_LIST_API_URI = "/v5/track/list/v2"
# FIRMWARE_BAS_URL = '/motorota/getfirmwareversion'

DOMAIN = "niu"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_COUNTRY = "country"
CONF_SCOOTER_ID = "scooter_id"
CONF_AUTH = 'conf_auth'
CONF_SENSORS = "sensors_selected"

DEFAULT_SCOOTER_ID = 0
ITALY_COUNTRY_ID = "39"

SENSOR_TYPE_BAT = "BAT"
SENSOR_TYPE_MOTO = "MOTO"
SENSOR_TYPE_DIST = "DIST"
SENSOR_TYPE_OVERALL = "TOTAL"
SENSOR_TYPE_POS = "POSITION"
# SENSOR_TYPE_SYSTEM = 'SYSTEM'
SENSOR_TYPE_TRACK = "TRACK"

AVAILABLE_SENSORS = [
    "BatteryACharge",
    "BatteryBCharge",
    "Isconnected",
    "TimesCharged",
    "temperatureDesc",
    "Temperature",
    "BatteryGrade",
    "CurrentSpeed",
    "ScooterConnected",
    "IsCharging",
    "IsLocked",
    "TimeLeft",
    "EstimatedMileage",
    "centreCtrlBatt",
    "HDOP",
    "Longitude",
    "Latitude",
    "Distance",
    "RidingTime",
    "totalMileage",
    "DaysInUse",
    "LastTrackStartTime",
    "LastTrackEndTime",
    "LastTrackDistance",
    "LastTrackAverageSpeed",
    "LastTrackRidingtime",
    "LastTrackThumb"
]


# Sensors schemas
from homeassistant.const import CONF_MONITORED_VARIABLES
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_COUNTRY): cv.positive_int,
        vol.Optional(CONF_SCOOTER_ID, default=DEFAULT_SCOOTER_ID): cv.positive_int,
        vol.Optional(CONF_MONITORED_VARIABLES, default=["BatteryCharge"]): vol.All(
            cv.ensure_list,
            vol.Length(min=1),
            [
                vol.In(
                    [
                        "BatteryCharge",
                        "Isconnected",
                        "TimesCharged",
                        "temperatureDesc",
                        "Temperature",
                        "BatteryGrade",
                        "CurrentSpeed",
                        "ScooterConnected",
                        "IsCharging",
                        "IsLocked",
                        "TimeLeft",
                        "EstimatedMileage",
                        "centreCtrlBatt",
                        "HDOP",
                        "Longitude",
                        "Latitude",
                        "Distance",
                        "RidingTime",
                        "totalMileage",
                        "DaysInUse",
                        "LastTrackStartTime",
                        "LastTrackEndTime",
                        "LastTrackDistance",
                        "LastTrackAverageSpeed",
                        "LastTrackRidingtime",
                        "LastTrackThumb",
                    ]
                )
            ],
        ),
    }
)

SENSOR_TYPES = {
    "Battery Charge (A)": [
        "battery_a_charge",
        "%",
        "batteryCharging",
        SENSOR_TYPE_BAT,
        "battery",
        "mdi:battery-charging-50",
    ],
    "Battery Charge (B)": [
        "battery_b_charge",
        "%",
        "batteryCharging",
        SENSOR_TYPE_BAT,
        "battery",
        "mdi:battery-charging-50",
    ],
    "Is Connected": [
        "is_connected",
        "",
        "isConnected",
        SENSOR_TYPE_BAT,
        "connectivity",
        "mdi:connection",
    ],
    "Times Charged": [
        "times_charged",
        "x",
        "chargedTimes",
        SENSOR_TYPE_BAT,
        "none",
        "mdi:battery-charging-wireless",
    ],
    "Temperature Desc": [
        "temp_descr",
        "",
        "temperatureDesc",
        SENSOR_TYPE_BAT,
        "none",
        "mdi:thermometer-alert",
    ],
    "Temperature": [
        "temperature",
        "°C",
        "temperature",
        SENSOR_TYPE_BAT,
        "temperature",
        "mdi:thermometer",
    ],
    "Battery Grade": [
        "battery_grade",
        "%",
        "gradeBattery",
        SENSOR_TYPE_BAT,
        "battery",
        "mdi:car-battery",
    ],
    "Current Speed": [
        "current_speed",
        "km/h",
        "nowSpeed",
        SENSOR_TYPE_MOTO,
        "none",
        "mdi:speedometer",
    ],
    "Scooter Connected": [
        "scooter_connected",
        "",
        "isConnected",
        SENSOR_TYPE_MOTO,
        "connectivity",
        "mdi:motorbike-electric",
    ],
    "Is Charging": [
        "is_charging",
        "",
        "isCharging",
        SENSOR_TYPE_MOTO,
        "power",
        "mdi:battery-charging",
    ],
    "Is Locked": ["is_locked", "", "lockStatus", SENSOR_TYPE_MOTO, "lock", "mdi:lock"],
    "Time Left": [
        "time_left",
        "h",
        "leftTime",
        SENSOR_TYPE_MOTO,
        "none",
        "mdi:av-timer",
    ],
    "Estimated Mileage": [
        "estimated_mileage",
        "km",
        "estimatedMileage",
        SENSOR_TYPE_MOTO,
        "none",
        "mdi:map-marker-distance",
    ],
    "Centre Ctrl Batt": [
        "centre_ctrl_batt",
        "%",
        "centreCtrlBattery",
        SENSOR_TYPE_MOTO,
        "battery",
        "mdi:car-cruise-control",
    ],
    "HDOP": ["hdp", "", "hdop", SENSOR_TYPE_MOTO, "none", "mdi:map-marker"],
    "Longitude": ["long", "", "lng", SENSOR_TYPE_POS, "none", "mdi:map-marker"],
    "Latitude": ["lat", "", "lat", SENSOR_TYPE_POS, "none", "mdi:map-marker"],
    "Distance": [
        "distance",
        "m",
        "distance",
        SENSOR_TYPE_DIST,
        "none",
        "mdi:map-marker-distance",
    ],
    "Riding Time": [
        "riding_time",
        "s",
        "ridingTime",
        SENSOR_TYPE_DIST,
        "none",
        "mdi:map-clock",
    ],
    "Total Mileage": [
        "total_mileage",
        "km",
        "totalMileage",
        SENSOR_TYPE_OVERALL,
        "none",
        "mdi:map-marker-distance",
    ],
    "Days In Use": [
        "bind_days_count",
        "days",
        "bindDaysCount",
        SENSOR_TYPE_OVERALL,
        "none",
        "mdi:calendar-today",
    ],
    "Last Track Start Time": [
        "last_track_start_time",
        "",
        "startTime",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:clock-start",
    ],
    "Last Track End Time": [
        "last_track_end_time",
        "",
        "endTime",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:clock-end",
    ],
    "Last Track Distance": [
        "last_track_distance",
        "m",
        "distance",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:map-marker-distance",
    ],
    "Last Track Average Speed": [
        "last_track_average_speed",
        "km/h",
        "avespeed",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:speedometer",
    ],
    "Last Track Riding Time": [
        "last_track_riding_time",
        "",
        "ridingtime",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:timelapse",
    ],
    "Last Track Thumb": [
        "last_track_thumb",
        "",
        "track_thumb",
        SENSOR_TYPE_TRACK,
        "none",
        "mdi:map",
    ]
}