import pandas as pd
from datetime import datetime

class Star():
    def __init__(self, star_name: str, dt: datetime):
        self.name = star_name

        self.data = pd.read_csv("src/starcalculator/data/j2000.csv", sep=",")

        if not self._star_exists():
            raise Exception(f"The star {self.name.upper()} wasn't found!")
        
        self.date_object = dt
        
        self.sha = self._get_sha()
        self.dec = self._get_dec()

    def _star_exists(self):
        return not self.data[self.data["star"] == self.name.lower()].empty
        
    def _get_sha(self):
        # need to be using RA and DEC and sha, should convert with function, needs to be SHA for later formulas

        search_result = self.data[self.data["star"] == self.name.lower()]

        sha = search_result["sha"].values[0]
        sha_pm = search_result["sha_pm"].values[0]
        
        years_since_epoch = self.date_object.year - 2000
        pm_sha_deg = sha_pm / 3_600_000

        new_sha = (sha + pm_sha_deg * years_since_epoch) % 360

        return round(new_sha, 3)

    def _get_dec(self):
        return 0
    
    def __str__(self):
        return f"Star: {self.name.upper()}, SHA: {self.sha}, DEC: {self.dec}"
    