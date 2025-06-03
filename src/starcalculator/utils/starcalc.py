import pandas as pd
from datetime import datetime

class Star():
    def __init__(self, star_name: str, dt: datetime):
        self.name = star_name

        self.data = pd.read_csv("src/starcalculator/data/j2000.csv", sep=",")

        if not self._star_exists():
            raise Exception(f"The star {self.name.upper()} wasn't found!")
        
        self.date_object = dt
        
        self.ra = self._get_ra()
        self.dec = self._get_dec()

    def _star_exists(self):
        return not self.data[self.data["star"] == self.name.lower()].empty
        
    def _get_ra(self):
        search_result = self.data[self.data["star"] == self.name.lower()]

        ra = search_result["ra"].values[0]
        ra_pm = search_result["ra_pm"].values[0]
        ra_pm_deg = ra_pm / 3_600_000
        years_since_epoch = self.date_object.year - 2000

        adjusted_ra = (ra + ra_pm_deg * years_since_epoch) % 360

        return round(adjusted_ra, 2)


    def _get_dec(self):
        search_result = self.data[self.data["star"] == self.name.lower()]

        dec = search_result["dec"].values[0]
        dec_pm = search_result["dec_pm"].values[0]
        dec_pm_deg = dec_pm / 3_600_000
        years_since_epoch = self.date_object.year - 2000

        adjusted_dec = dec + dec_pm_deg * years_since_epoch

        return round(adjusted_dec, 2)
    
    def __str__(self):
        return f"Star: {self.name.upper()}, RA: {self.ra}, DEC: {self.dec}"
    