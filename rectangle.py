#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can calculate the area and perimeter of a rectangle


# This function calculates the area and perimeter of the rectangle
def main():

    # These are the input variables
    length = int(input("Enter the length of the rectangle here: "))
    width = int(input("Enter the width of the rectangle here: "))

    # These are the perimeter and area calculations
    area = length*width
    perimeter = 2*(length+width)

    # This is the user output
    print("")
    print("The area of the is: ", area, "cm^2")
    print("The perimeter of the is: ", perimeter, "cm")


if __name__ == "__main__":
    main()
