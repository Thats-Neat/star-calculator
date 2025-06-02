import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the position of a star or stars")
    parser.add_argument("-b", "--basic", action="store_true", help="Calculate the position of a star one hour from your current time")
    parser.add_argument("star_name", nargs="?", help="Name of the star")

    args = parser.parse_args()

    if args.basic:
        if args.star_name is None:
            parser.error("the --basic options requires STAR_NAME to be provided.")

        print("running basic")    


