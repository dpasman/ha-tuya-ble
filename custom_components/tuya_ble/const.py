"""The Tuya BLE integration."""
from __future__ import annotations

from dataclasses import dataclass
from typing_extensions import Final

DOMAIN: Final = "tuya_ble"

DEVICE_METADATA_UUIDS: Final = "uuids"

DEVICE_DEF_MANUFACTURER: Final = "Tuya"
SET_DISCONNECTED_DELAY = 10 * 60

CONF_UUID: Final = "uuid"
CONF_LOCAL_KEY: Final = "local_key"
CONF_CATEGORY: Final = "category"
CONF_PRODUCT_ID: Final = "product_id"
CONF_DEVICE_NAME: Final = "device_name"
CONF_PRODUCT_MODEL: Final = "product_model"
CONF_PRODUCT_NAME: Final = "product_name"

TUYA_API_DEVICES_URL: Final = "/v1.0/users/%s/devices"
TUYA_API_FACTORY_INFO_URL: Final = "/v1.0/iot-03/devices/factory-infos?device_ids=%s"
TUYA_FACTORY_INFO_MAC: Final = "mac"

BATTERY_STATE_LOW: Final = "low"
BATTERY_STATE_NORMAL: Final = "normal"
BATTERY_STATE_HIGH: Final = "high"

BATTERY_NOT_CHARGING: Final = "not_charging"
BATTERY_CHARGING: Final = "charging"
BATTERY_CHARGED: Final = "charged"

CO2_LEVEL_NORMAL: Final = "normal"
CO2_LEVEL_ALARM: Final = "alarm"

FINGERBOT_MODE_PUSH: Final = "push"
FINGERBOT_MODE_SWITCH: Final = "switch"
FINGERBOT_MODE_PROGRAM: Final = "program"
FINGERBOT_BUTTON_EVENT: Final = "fingerbot_button_pressed"

# Tuya cloud constants (previously imported from homeassistant.components.tuya.const)
TUYA_DOMAIN: Final = "tuya"
CONF_ACCESS_ID: Final = "access_id"
CONF_ACCESS_SECRET: Final = "access_secret"
CONF_AUTH_TYPE: Final = "auth_type"
CONF_APP_TYPE: Final = "tuya_app_type"
CONF_ENDPOINT: Final = "endpoint"
CONF_COUNTRY_CODE: Final = "country_code"
TUYA_RESPONSE_SUCCESS: Final = "success"
TUYA_RESPONSE_RESULT: Final = "result"
TUYA_RESPONSE_CODE: Final = "code"
TUYA_RESPONSE_MSG: Final = "msg"
TUYA_SMART_APP: Final = "tuyaSmart"
SMARTLIFE_APP: Final = "smartlife_app"

TUYA_EU_ENDPOINT: Final = "https://openapi.tuyaeu.com"
TUYA_US_ENDPOINT: Final = "https://openapi.tuyaus.com"
TUYA_CN_ENDPOINT: Final = "https://openapi.tuyacn.com"
TUYA_IN_ENDPOINT: Final = "https://openapi.tuyain.com"


@dataclass
class TuyaCountry:
    name: str
    country_code: str
    endpoint: str


TUYA_COUNTRIES: list[TuyaCountry] = [
    TuyaCountry("Afghanistan", "93", TUYA_EU_ENDPOINT),
    TuyaCountry("Albania", "355", TUYA_EU_ENDPOINT),
    TuyaCountry("Algeria", "213", TUYA_EU_ENDPOINT),
    TuyaCountry("American Samoa", "1-684", TUYA_US_ENDPOINT),
    TuyaCountry("Andorra", "376", TUYA_EU_ENDPOINT),
    TuyaCountry("Angola", "244", TUYA_EU_ENDPOINT),
    TuyaCountry("Anguilla", "1-264", TUYA_US_ENDPOINT),
    TuyaCountry("Antigua and Barbuda", "1-268", TUYA_US_ENDPOINT),
    TuyaCountry("Argentina", "54", TUYA_US_ENDPOINT),
    TuyaCountry("Armenia", "374", TUYA_EU_ENDPOINT),
    TuyaCountry("Aruba", "297", TUYA_US_ENDPOINT),
    TuyaCountry("Australia", "61", TUYA_EU_ENDPOINT),
    TuyaCountry("Austria", "43", TUYA_EU_ENDPOINT),
    TuyaCountry("Azerbaijan", "994", TUYA_EU_ENDPOINT),
    TuyaCountry("Bahamas", "1-242", TUYA_US_ENDPOINT),
    TuyaCountry("Bahrain", "973", TUYA_EU_ENDPOINT),
    TuyaCountry("Bangladesh", "880", TUYA_IN_ENDPOINT),
    TuyaCountry("Barbados", "1-246", TUYA_US_ENDPOINT),
    TuyaCountry("Belarus", "375", TUYA_EU_ENDPOINT),
    TuyaCountry("Belgium", "32", TUYA_EU_ENDPOINT),
    TuyaCountry("Belize", "501", TUYA_US_ENDPOINT),
    TuyaCountry("Benin", "229", TUYA_EU_ENDPOINT),
    TuyaCountry("Bermuda", "1-441", TUYA_US_ENDPOINT),
    TuyaCountry("Bhutan", "975", TUYA_IN_ENDPOINT),
    TuyaCountry("Bolivia", "591", TUYA_US_ENDPOINT),
    TuyaCountry("Bosnia and Herzegovina", "387", TUYA_EU_ENDPOINT),
    TuyaCountry("Botswana", "267", TUYA_EU_ENDPOINT),
    TuyaCountry("Brazil", "55", TUYA_US_ENDPOINT),
    TuyaCountry("British Virgin Islands", "1-284", TUYA_US_ENDPOINT),
    TuyaCountry("Brunei", "673", TUYA_EU_ENDPOINT),
    TuyaCountry("Bulgaria", "359", TUYA_EU_ENDPOINT),
    TuyaCountry("Burkina Faso", "226", TUYA_EU_ENDPOINT),
    TuyaCountry("Burundi", "257", TUYA_EU_ENDPOINT),
    TuyaCountry("Cambodia", "855", TUYA_EU_ENDPOINT),
    TuyaCountry("Cameroon", "237", TUYA_EU_ENDPOINT),
    TuyaCountry("Canada", "1", TUYA_US_ENDPOINT),
    TuyaCountry("Cape Verde", "238", TUYA_EU_ENDPOINT),
    TuyaCountry("Cayman Islands", "1-345", TUYA_US_ENDPOINT),
    TuyaCountry("Central African Republic", "236", TUYA_EU_ENDPOINT),
    TuyaCountry("Chad", "235", TUYA_EU_ENDPOINT),
    TuyaCountry("Chile", "56", TUYA_US_ENDPOINT),
    TuyaCountry("China", "86", TUYA_CN_ENDPOINT),
    TuyaCountry("Colombia", "57", TUYA_US_ENDPOINT),
    TuyaCountry("Comoros", "269", TUYA_EU_ENDPOINT),
    TuyaCountry("Cook Islands", "682", TUYA_US_ENDPOINT),
    TuyaCountry("Costa Rica", "506", TUYA_US_ENDPOINT),
    TuyaCountry("Croatia", "385", TUYA_EU_ENDPOINT),
    TuyaCountry("Cuba", "53", TUYA_US_ENDPOINT),
    TuyaCountry("Curacao", "599", TUYA_US_ENDPOINT),
    TuyaCountry("Cyprus", "357", TUYA_EU_ENDPOINT),
    TuyaCountry("Czech Republic", "420", TUYA_EU_ENDPOINT),
    TuyaCountry("Democratic Republic of the Congo", "243", TUYA_EU_ENDPOINT),
    TuyaCountry("Denmark", "45", TUYA_EU_ENDPOINT),
    TuyaCountry("Djibouti", "253", TUYA_EU_ENDPOINT),
    TuyaCountry("Dominica", "1-767", TUYA_US_ENDPOINT),
    TuyaCountry("Dominican Republic", "1-809", TUYA_US_ENDPOINT),
    TuyaCountry("East Timor", "670", TUYA_EU_ENDPOINT),
    TuyaCountry("Ecuador", "593", TUYA_US_ENDPOINT),
    TuyaCountry("Egypt", "20", TUYA_EU_ENDPOINT),
    TuyaCountry("El Salvador", "503", TUYA_US_ENDPOINT),
    TuyaCountry("Equatorial Guinea", "240", TUYA_EU_ENDPOINT),
    TuyaCountry("Eritrea", "291", TUYA_EU_ENDPOINT),
    TuyaCountry("Estonia", "372", TUYA_EU_ENDPOINT),
    TuyaCountry("Ethiopia", "251", TUYA_EU_ENDPOINT),
    TuyaCountry("Falkland Islands", "500", TUYA_US_ENDPOINT),
    TuyaCountry("Faroe Islands", "298", TUYA_EU_ENDPOINT),
    TuyaCountry("Fiji", "679", TUYA_US_ENDPOINT),
    TuyaCountry("Finland", "358", TUYA_EU_ENDPOINT),
    TuyaCountry("France", "33", TUYA_EU_ENDPOINT),
    TuyaCountry("French Polynesia", "689", TUYA_US_ENDPOINT),
    TuyaCountry("Gabon", "241", TUYA_EU_ENDPOINT),
    TuyaCountry("Gambia", "220", TUYA_EU_ENDPOINT),
    TuyaCountry("Georgia", "995", TUYA_EU_ENDPOINT),
    TuyaCountry("Germany", "49", TUYA_EU_ENDPOINT),
    TuyaCountry("Ghana", "233", TUYA_EU_ENDPOINT),
    TuyaCountry("Gibraltar", "350", TUYA_EU_ENDPOINT),
    TuyaCountry("Greece", "30", TUYA_EU_ENDPOINT),
    TuyaCountry("Greenland", "299", TUYA_US_ENDPOINT),
    TuyaCountry("Grenada", "1-473", TUYA_US_ENDPOINT),
    TuyaCountry("Guam", "1-671", TUYA_US_ENDPOINT),
    TuyaCountry("Guatemala", "502", TUYA_US_ENDPOINT),
    TuyaCountry("Guinea", "224", TUYA_EU_ENDPOINT),
    TuyaCountry("Guinea-Bissau", "245", TUYA_EU_ENDPOINT),
    TuyaCountry("Guyana", "592", TUYA_US_ENDPOINT),
    TuyaCountry("Haiti", "509", TUYA_US_ENDPOINT),
    TuyaCountry("Honduras", "504", TUYA_US_ENDPOINT),
    TuyaCountry("Hong Kong", "852", TUYA_EU_ENDPOINT),
    TuyaCountry("Hungary", "36", TUYA_EU_ENDPOINT),
    TuyaCountry("Iceland", "354", TUYA_EU_ENDPOINT),
    TuyaCountry("India", "91", TUYA_IN_ENDPOINT),
    TuyaCountry("Indonesia", "62", TUYA_EU_ENDPOINT),
    TuyaCountry("Iran", "98", TUYA_EU_ENDPOINT),
    TuyaCountry("Iraq", "964", TUYA_EU_ENDPOINT),
    TuyaCountry("Ireland", "353", TUYA_EU_ENDPOINT),
    TuyaCountry("Israel", "972", TUYA_EU_ENDPOINT),
    TuyaCountry("Italy", "39", TUYA_EU_ENDPOINT),
    TuyaCountry("Ivory Coast", "225", TUYA_EU_ENDPOINT),
    TuyaCountry("Jamaica", "1-876", TUYA_US_ENDPOINT),
    TuyaCountry("Japan", "81", TUYA_EU_ENDPOINT),
    TuyaCountry("Jordan", "962", TUYA_EU_ENDPOINT),
    TuyaCountry("Kazakhstan", "7", TUYA_EU_ENDPOINT),
    TuyaCountry("Kenya", "254", TUYA_EU_ENDPOINT),
    TuyaCountry("Kiribati", "686", TUYA_US_ENDPOINT),
    TuyaCountry("Kosovo", "383", TUYA_EU_ENDPOINT),
    TuyaCountry("Kuwait", "965", TUYA_EU_ENDPOINT),
    TuyaCountry("Kyrgyzstan", "996", TUYA_EU_ENDPOINT),
    TuyaCountry("Laos", "856", TUYA_EU_ENDPOINT),
    TuyaCountry("Latvia", "371", TUYA_EU_ENDPOINT),
    TuyaCountry("Lebanon", "961", TUYA_EU_ENDPOINT),
    TuyaCountry("Lesotho", "266", TUYA_EU_ENDPOINT),
    TuyaCountry("Liberia", "231", TUYA_EU_ENDPOINT),
    TuyaCountry("Libya", "218", TUYA_EU_ENDPOINT),
    TuyaCountry("Liechtenstein", "423", TUYA_EU_ENDPOINT),
    TuyaCountry("Lithuania", "370", TUYA_EU_ENDPOINT),
    TuyaCountry("Luxembourg", "352", TUYA_EU_ENDPOINT),
    TuyaCountry("Macau", "853", TUYA_EU_ENDPOINT),
    TuyaCountry("Macedonia", "389", TUYA_EU_ENDPOINT),
    TuyaCountry("Madagascar", "261", TUYA_EU_ENDPOINT),
    TuyaCountry("Malawi", "265", TUYA_EU_ENDPOINT),
    TuyaCountry("Malaysia", "60", TUYA_EU_ENDPOINT),
    TuyaCountry("Maldives", "960", TUYA_IN_ENDPOINT),
    TuyaCountry("Mali", "223", TUYA_EU_ENDPOINT),
    TuyaCountry("Malta", "356", TUYA_EU_ENDPOINT),
    TuyaCountry("Marshall Islands", "692", TUYA_US_ENDPOINT),
    TuyaCountry("Mauritania", "222", TUYA_EU_ENDPOINT),
    TuyaCountry("Mauritius", "230", TUYA_EU_ENDPOINT),
    TuyaCountry("Mexico", "52", TUYA_US_ENDPOINT),
    TuyaCountry("Micronesia", "691", TUYA_US_ENDPOINT),
    TuyaCountry("Moldova", "373", TUYA_EU_ENDPOINT),
    TuyaCountry("Monaco", "377", TUYA_EU_ENDPOINT),
    TuyaCountry("Mongolia", "976", TUYA_EU_ENDPOINT),
    TuyaCountry("Montenegro", "382", TUYA_EU_ENDPOINT),
    TuyaCountry("Montserrat", "1-664", TUYA_US_ENDPOINT),
    TuyaCountry("Morocco", "212", TUYA_EU_ENDPOINT),
    TuyaCountry("Mozambique", "258", TUYA_EU_ENDPOINT),
    TuyaCountry("Myanmar", "95", TUYA_EU_ENDPOINT),
    TuyaCountry("Namibia", "264", TUYA_EU_ENDPOINT),
    TuyaCountry("Nauru", "674", TUYA_US_ENDPOINT),
    TuyaCountry("Nepal", "977", TUYA_IN_ENDPOINT),
    TuyaCountry("Netherlands", "31", TUYA_EU_ENDPOINT),
    TuyaCountry("New Caledonia", "687", TUYA_US_ENDPOINT),
    TuyaCountry("New Zealand", "64", TUYA_EU_ENDPOINT),
    TuyaCountry("Nicaragua", "505", TUYA_US_ENDPOINT),
    TuyaCountry("Niger", "227", TUYA_EU_ENDPOINT),
    TuyaCountry("Nigeria", "234", TUYA_EU_ENDPOINT),
    TuyaCountry("Niue", "683", TUYA_US_ENDPOINT),
    TuyaCountry("North Korea", "850", TUYA_EU_ENDPOINT),
    TuyaCountry("Northern Mariana Islands", "1-670", TUYA_US_ENDPOINT),
    TuyaCountry("Norway", "47", TUYA_EU_ENDPOINT),
    TuyaCountry("Oman", "968", TUYA_EU_ENDPOINT),
    TuyaCountry("Pakistan", "92", TUYA_IN_ENDPOINT),
    TuyaCountry("Palau", "680", TUYA_US_ENDPOINT),
    TuyaCountry("Palestine", "970", TUYA_EU_ENDPOINT),
    TuyaCountry("Panama", "507", TUYA_US_ENDPOINT),
    TuyaCountry("Papua New Guinea", "675", TUYA_US_ENDPOINT),
    TuyaCountry("Paraguay", "595", TUYA_US_ENDPOINT),
    TuyaCountry("Peru", "51", TUYA_US_ENDPOINT),
    TuyaCountry("Philippines", "63", TUYA_EU_ENDPOINT),
    TuyaCountry("Poland", "48", TUYA_EU_ENDPOINT),
    TuyaCountry("Portugal", "351", TUYA_EU_ENDPOINT),
    TuyaCountry("Puerto Rico", "1-787", TUYA_US_ENDPOINT),
    TuyaCountry("Qatar", "974", TUYA_EU_ENDPOINT),
    TuyaCountry("Republic of the Congo", "242", TUYA_EU_ENDPOINT),
    TuyaCountry("Romania", "40", TUYA_EU_ENDPOINT),
    TuyaCountry("Russia", "7", TUYA_EU_ENDPOINT),
    TuyaCountry("Rwanda", "250", TUYA_EU_ENDPOINT),
    TuyaCountry("Saint Kitts and Nevis", "1-869", TUYA_US_ENDPOINT),
    TuyaCountry("Saint Lucia", "1-758", TUYA_US_ENDPOINT),
    TuyaCountry("Saint Vincent and the Grenadines", "1-784", TUYA_US_ENDPOINT),
    TuyaCountry("Samoa", "685", TUYA_US_ENDPOINT),
    TuyaCountry("San Marino", "378", TUYA_EU_ENDPOINT),
    TuyaCountry("Sao Tome and Principe", "239", TUYA_EU_ENDPOINT),
    TuyaCountry("Saudi Arabia", "966", TUYA_EU_ENDPOINT),
    TuyaCountry("Senegal", "221", TUYA_EU_ENDPOINT),
    TuyaCountry("Serbia", "381", TUYA_EU_ENDPOINT),
    TuyaCountry("Seychelles", "248", TUYA_EU_ENDPOINT),
    TuyaCountry("Sierra Leone", "232", TUYA_EU_ENDPOINT),
    TuyaCountry("Singapore", "65", TUYA_EU_ENDPOINT),
    TuyaCountry("Sint Maarten", "1-721", TUYA_US_ENDPOINT),
    TuyaCountry("Slovakia", "421", TUYA_EU_ENDPOINT),
    TuyaCountry("Slovenia", "386", TUYA_EU_ENDPOINT),
    TuyaCountry("Solomon Islands", "677", TUYA_US_ENDPOINT),
    TuyaCountry("Somalia", "252", TUYA_EU_ENDPOINT),
    TuyaCountry("South Africa", "27", TUYA_EU_ENDPOINT),
    TuyaCountry("South Korea", "82", TUYA_EU_ENDPOINT),
    TuyaCountry("South Sudan", "211", TUYA_EU_ENDPOINT),
    TuyaCountry("Spain", "34", TUYA_EU_ENDPOINT),
    TuyaCountry("Sri Lanka", "94", TUYA_IN_ENDPOINT),
    TuyaCountry("Sudan", "249", TUYA_EU_ENDPOINT),
    TuyaCountry("Suriname", "597", TUYA_US_ENDPOINT),
    TuyaCountry("Swaziland", "268", TUYA_EU_ENDPOINT),
    TuyaCountry("Sweden", "46", TUYA_EU_ENDPOINT),
    TuyaCountry("Switzerland", "41", TUYA_EU_ENDPOINT),
    TuyaCountry("Syria", "963", TUYA_EU_ENDPOINT),
    TuyaCountry("Taiwan", "886", TUYA_EU_ENDPOINT),
    TuyaCountry("Tajikistan", "992", TUYA_EU_ENDPOINT),
    TuyaCountry("Tanzania", "255", TUYA_EU_ENDPOINT),
    TuyaCountry("Thailand", "66", TUYA_EU_ENDPOINT),
    TuyaCountry("Togo", "228", TUYA_EU_ENDPOINT),
    TuyaCountry("Tonga", "676", TUYA_US_ENDPOINT),
    TuyaCountry("Trinidad and Tobago", "1-868", TUYA_US_ENDPOINT),
    TuyaCountry("Tunisia", "216", TUYA_EU_ENDPOINT),
    TuyaCountry("Turkey", "90", TUYA_EU_ENDPOINT),
    TuyaCountry("Turkmenistan", "993", TUYA_EU_ENDPOINT),
    TuyaCountry("Turks and Caicos Islands", "1-649", TUYA_US_ENDPOINT),
    TuyaCountry("Tuvalu", "688", TUYA_US_ENDPOINT),
    TuyaCountry("U.S. Virgin Islands", "1-340", TUYA_US_ENDPOINT),
    TuyaCountry("Uganda", "256", TUYA_EU_ENDPOINT),
    TuyaCountry("Ukraine", "380", TUYA_EU_ENDPOINT),
    TuyaCountry("United Arab Emirates", "971", TUYA_EU_ENDPOINT),
    TuyaCountry("United Kingdom", "44", TUYA_EU_ENDPOINT),
    TuyaCountry("United States", "1", TUYA_US_ENDPOINT),
    TuyaCountry("Uruguay", "598", TUYA_US_ENDPOINT),
    TuyaCountry("Uzbekistan", "998", TUYA_EU_ENDPOINT),
    TuyaCountry("Vanuatu", "678", TUYA_US_ENDPOINT),
    TuyaCountry("Vatican", "379", TUYA_EU_ENDPOINT),
    TuyaCountry("Venezuela", "58", TUYA_US_ENDPOINT),
    TuyaCountry("Vietnam", "84", TUYA_EU_ENDPOINT),
    TuyaCountry("Western Sahara", "212", TUYA_EU_ENDPOINT),
    TuyaCountry("Yemen", "967", TUYA_EU_ENDPOINT),
    TuyaCountry("Zambia", "260", TUYA_EU_ENDPOINT),
    TuyaCountry("Zimbabwe", "263", TUYA_EU_ENDPOINT),
]
