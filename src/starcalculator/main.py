import argparse
from datetime import datetime, timedelta

from starcalculator.utils.time import Time
from starcalculator.utils.star import Star
from starcalculator.utils.location import Location
from starcalculator.utils.calculator import Calculator

def main():
    parser = argparse.ArgumentParser(description="Calculate the position of a star or stars")
    parser.add_argument("-b", "--basic", action="store_true", help="Calculate the position of a star one hour from your current time")
    parser.add_argument("-n", "--now", action="store_true", help="Calculate the position of a star at your current time")
    parser.add_argument("-s", "--set-date", action="store_true", help="Calculate the position of a star at a set date for one night (i.e. 20:00-6:00)")
    parser.add_argument("star_name", nargs="?", help="Name of the star")
    parser.add_argument("-d", "--date", type=str, help="A set date (i.e. YYYY-MM-DD)")
    parser.add_argument("-l", "--lat", type=float, help="Your latitude (i.e. 156.20)")
    parser.add_argument("-lo", "--long", type=float, help="Your longitude (i.e. 26.40)")
    parser.add_argument("-tz", "--timezone", type=str, help="Your timezone (i.e. America/Los_Angeles)")

    args = parser.parse_args()

    if args.basic:
        if args.star_name is None or args.lat is None or args.long is None:
            parser.error("the --basic option requires STAR_NAME, LATITUDE, and LONGITUDE to be provided.")
        basic_calculation(args.star_name, args.lat, args.long)
    elif args.now:
        if args.star_name is None or args.lat is None or args.long is None:
            parser.error("the --now option requires STAR_NAME, LATITUDE, and LONGITUDE to be provided.")
        now_calculation(args.star_name, args.lat, args.long)
    elif args.set_date:
        if args.star_name is None or args.lat is None or args.long is None or args.timezone is None or args.date is None:
            parser.error("the --set-date option requires STAR_NAME, LATITUDE, LONGITUDE, TIMEZONE, and DATE to be provided.")
        set_date_calculation(args.star_name, args.lat, args.long, args.timezone, args.date)
    


def basic_calculation(star_name: str, latitude: float, longitude: float):
    now_local = datetime.now()
    now_local += timedelta(hours=1)
    time_object = Time(dt=now_local, tz_name="UTC")
    location_object = Location(lat=latitude, long=longitude)
    star_object = Star(star_name=star_name, dt=time_object.get_utc())
    calculator_object = Calculator(star=star_object, location=location_object, time=time_object)

    print(calculator_object)

def now_calculation(star_name: str, latitude: float, longitude: float):
    now_local = datetime.now()
    time_object = Time(dt=now_local, tz_name="UTC")
    location_object = Location(lat=latitude, long=longitude)
    star_object = Star(star_name=star_name, dt=time_object.get_utc())
    calculator_object = Calculator(star=star_object, location=location_object, time=time_object)

    print(calculator_object)

def set_date_calculation(star_name: str, latitude: float, longitude: float, timezone: str, date: str):
    date_data = date.split("-")
    date_object = datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), 0, 0, 0)

    print("hour,star,altitude,azimuth")

    for i in [20,21,22,23,0,1,2,3,4,5,6]:
        try:
            date_object = date_object.replace(hour=i, minute=0)
            time_object = Time(dt=date_object, tz_name=timezone)
        except:
            raise Exception("Timezone or Date information is incorrect!")
    
        location_object = Location(lat=latitude, long=longitude)
        star_object = Star(star_name=star_name, dt=time_object.get_utc())
        calculator_object = Calculator(star=star_object, location=location_object, time=time_object)

        print(f"{i},{star_object.get_name()},{calculator_object.get_altitude()},{calculator_object.get_azimuth()}")