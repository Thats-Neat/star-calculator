from datetime import datetime
from zoneinfo import ZoneInfo

class TimeSwitch():
    def __init__(self, dt: datetime, tz_name: str):
        self.original_tz = tz_name
        self.local_dt = dt.replace(tzinfo=ZoneInfo(tz_name))
        self.utc_dt = self.local_dt.astimezone(ZoneInfo("UTC"))

    def get_utc(self) -> datetime:
        return self.utc_dt
    
    def __str__(self):
        return f"{self.local_dt.isoformat()} -> {self.utc_dt.isoformat()}"
