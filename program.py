#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is program


def main():
    # this function uses a try statement

    # input
    integer = input("Please enter the year: ")
    print("")

    # process & output
    try:
        year = int(integer)
        if year % 400 == 0:
            print("{0} is defenetly a leap year".format(year))
        elif year % 100 == 0:
            print("{0} isn't a leap year".format(year))
        elif year % 4 == 0:
            print("{0} is defenetly a leap year".format(year))
        else:
            print("{0} isn't a leap year".format(year))

    except Exception:
        print("Invalid input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
