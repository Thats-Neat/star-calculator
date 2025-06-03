import argparse
from datetime import datetime

from starcalculator.utils.time import Time
from starcalculator.utils.star import Star
from starcalculator.utils.location import Location
from starcalculator.utils.calculator import Calculator

def main():
    parser = argparse.ArgumentParser(description="Calculate the position of a star or stars")
    parser.add_argument("-b", "--basic", action="store_true", help="Calculate the position of a star one hour from your current time")
    parser.add_argument("star_name", nargs="?", help="Name of the star")
    parser.add_argument("-l", "--lat", type=float, help="Your latitude (i.e. 156.20)")
    parser.add_argument("-lo", "--long", type=float, help="Your longitude (i.e. 26.20)")
    parser.add_argument("-tz", "--timezone", type=str, help="Your timezone (i.e. America/Los_Angeles)")

    args = parser.parse_args()

    if args.basic:
        if args.star_name is None or args.lat is None or args.long is None:
            parser.error("the --basic option requires STAR_NAME, LATITUDE, and LONGITUDE to be provided.")

        basic_calculation(args.star_name, args.lat, args.long)


def basic_calculation(star_name: str, latitude: float, longitude: float):
    now_local = datetime.now()
    time_object = Time(dt=now_local, tz_name="UTC")
    location_object = Location(lat=latitude, long=longitude)
    star_object = Star(star_name=star_name, dt=time_object.get_utc())
    calculator_object = Calculator(star=star_object, location=location_object, time=time_object)

    print(calculator_object)

