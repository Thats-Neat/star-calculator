from datetime import datetime
from zoneinfo import ZoneInfo

class Time():
    def __init__(self, dt: datetime, tz_name: str):
        self._original_tz = tz_name
        self._local_dt = dt.replace(tzinfo=ZoneInfo(tz_name))
        self._utc_dt = self._local_dt.astimezone(ZoneInfo("UTC"))

    def get_utc(self) -> datetime:
        return self._utc_dt
    
    def __str__(self):
        return f"{self._local_dt.isoformat()} -> {self._utc_dt.isoformat()}"
