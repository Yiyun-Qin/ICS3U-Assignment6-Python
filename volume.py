#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in June 2022
# This is the math program, calculating the volume of circular truncated cone

import math


def volume(radius_top, radius_bottom, height):
    # This function calculates the volume
    shape_volume = (
        1
        / 3
        * math.pi
        * height
        * (pow(radius_top, 2) + radius_top * radius_bottom + pow(radius_bottom, 2))
    )
    return shape_volume


def main():
    # This function does try and catch, input and output

    # input
    print(
        "A circular truncated cone is a solid figure that looks like a cone with the tip straight cut off."
    )
    print("This function calculates its volume.")
    radius_top_string = input("Enter the radius of the circle at the top (cm): ")
    radius_bottom_string = input("Enter the radius of the circle at the top (cm): ")
    height_string = input("Enter the height (cm): ")

    # process & output
    print("")
    try:
        radius_top_float = float(radius_top_string)
        radius_bottom_float = float(radius_bottom_string)
        height_float = float(height_string)
        # call functions
        if radius_top_float > 0 and radius_bottom_float > 0 and height_float > 0:
            shape_volume = volume(
                radius_top=radius_top_float,
                radius_bottom=radius_bottom_float,
                height=height_float,
            )
            print(
                "The volume of this circular truncated cone is {:,.2f} cm³.".format(
                    shape_volume
                )
            )
        else:
            print("Please enter a positive number!")
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
