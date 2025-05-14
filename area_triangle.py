#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program uses a function to calculate the area of a triangle with user input

def main():
    # This function calculates the area of a triangle
    def area_of_triangle(base, height):
        return (base * height) / 2

    # Get and validate input from user
    try:
        base = float(input("Enter the base of the triangle (cm): "))
        height = float(input("Enter the height of the triangle (cm): "))
    except ValueError:
        print("Error, you entered a string.")
        return

    # Validate if values are positive
    if base <= 0 or height <= 0:
        print("Enter positive decimal numbers.")
        return

    # Calculate area
    area = area_of_triangle(base, height)

    # Output result
    print(f"The area of the triangle is {area} cm^2.")

if __name__ == "__main__":
    main()
