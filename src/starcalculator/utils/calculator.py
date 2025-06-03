import math
from datetime import datetime

from starcalculator.utils.star import Star
from starcalculator.utils.location import Location
from starcalculator.utils.time import Time

class Calculator():
    def __init__(self, star: Star, location: Location, time: Time):
        self._star = star
        self._location = location
        self._time = time
        self._lst = self._calc_lst()
        self._altitude = self._calc_altitude()
        self._azimuth = self._calc_azimuth()

    def _julian_date(self):
        time_data = self._time.get_utc()

        year = time_data.year
        month = time_data.month
        day = time_data.day
        hour = time_data.hour
        minute = time_data.minute
        second = time_data.second + time_data.microsecond / 1e6

        if month <= 2:
            year -= 1
            month += 12

        A = year // 100
        B = 2 - A + A // 4

        day_frac = (hour + minute / 60 + second / 3600) / 24
        JD = int(365.25 * (year + 4716) + int(30.6001 * (month + 1)) + day + day_frac + B - 1524.5)

        return JD

    def _calc_lst(self):
        JD = self._julian_date()
        time_data = self._time.get_utc()

        T = (JD - 2451545.0) / 36525.0

        gmst = (24110.54841 + 8640184.812866 * T + 0.093104 * T*T - 6.2e-6 * T*T*T) / 3600.0

        UT = time_data.hour + time_data.minute / 60 + time_data.second / 3600
        gmst += 1.00273790935 * UT
        gmst %= 24

        LST = gmst + self._location.get_long() / 15.0
        LST %= 24

        LST_degrees = LST * 15
        return round(LST_degrees % 360, 4)

    def _calc_altitude(self):
        ha = (self._calc_lst() - self._star.get_ra())

        ha = math.radians(ha)
        dec = math.radians(self._star.get_dec())
        lat = math.radians(self._location.get_lat())

        sin_alt = math.sin(dec) * math.sin(lat) + math.cos(dec) * math.cos(lat) * math.cos(ha)
        alt = math.asin(sin_alt)

        return round(math.degrees(alt), 4)

    def _calc_azimuth(self):
        ha = (self._calc_lst() - self._star.get_ra())

        ha = math.radians(ha)
        dec = math.radians(self._star.get_dec())
        lat = math.radians(self._location.get_lat())
        alt = math.radians(self.get_altitude())

        cos_az = (math.sin(dec) - math.sin(alt) * math.sin(lat)) / (math.cos(alt) * math.cos(lat))
        sin_az = (math.cos(dec) * math.sin(ha)) / math.cos(alt)

        az_rad = math.atan2(sin_az, cos_az)
        az_deg = (360 - math.degrees(az_rad)) % 360

        return round(az_deg, 4)

    def get_altitude(self):
        return self._altitude

    def get_azimuth(self):
        return self._azimuth   

    def __str__(self):
        return f"Star: {self._star.get_name().upper()}, Altitude: {self._altitude}, Azimuth: {self._azimuth}"