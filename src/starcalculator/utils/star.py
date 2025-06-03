import pandas as pd
from datetime import datetime

class Star():
    def __init__(self, star_name: str, dt: datetime):
        self._name = star_name

        self._data = pd.read_csv("src/starcalculator/data/j2000.csv", sep=",")

        if not self._star_exists():
            raise Exception(f"The star {self._name.upper()} wasn't found!")
        
        self._date_object = dt
        
        self._ra = self._get_ra()
        self._dec = self._get_dec()

    def _star_exists(self):
        return not self._data[self._data["star"] == self._name.lower()].empty
        
    def _get_ra(self):
        search_result = self._data[self._data["star"] == self._name.lower()]

        ra = search_result["ra"].values[0]
        ra_pm = search_result["ra_pm"].values[0]
        ra_pm_deg = ra_pm / 3_600_000
        years_since_epoch = self._date_object.year - 2000

        adjusted_ra = (ra + ra_pm_deg * years_since_epoch) % 360

        return round(adjusted_ra, 2)


    def _get_dec(self):
        search_result = self._data[self._data["star"] == self._name.lower()]

        dec = search_result["dec"].values[0]
        dec_pm = search_result["dec_pm"].values[0]
        dec_pm_deg = dec_pm / 3_600_000
        years_since_epoch = self._date_object.year - 2000

        adjusted_dec = dec + dec_pm_deg * years_since_epoch

        return round(adjusted_dec, 2)
    
    def __str__(self):
        return f"Star: {self._name.upper()}, RA: {self._ra}, DEC: {self._dec}"
    