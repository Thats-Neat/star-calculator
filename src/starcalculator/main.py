import argparse
from datetime import datetime
from starcalculator.utils.startime import TimeSwitch
from starcalculator.utils.starcalc import Star

def main():
    parser = argparse.ArgumentParser(description="Calculate the position of a star or stars")
    parser.add_argument("-b", "--basic", action="store_true", help="Calculate the position of a star one hour from your current time")
    parser.add_argument("star_name", nargs="?", help="Name of the star")
    parser.add_argument("timezone", nargs="?", help="Your timezone (i.e. America/Los_Angeles)")

    args = parser.parse_args()

    if args.basic:
        if args.star_name is None is None:
            parser.error("the --basic option requires STAR_NAME to be provided.")

        now_local = datetime.now()
        time_object = TimeSwitch(now_local, "UTC")

        star_object = Star(args.star_name, time_object.get_utc())

        print(star_object)


