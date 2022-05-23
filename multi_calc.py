#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line

import math


def energy_calc(mass):
    c = 3 * (10**8)
    energy = mass * c
    return energy


def area_calc(side):
    s = (side[0] + side[1] + side[2]) / 2
    area = math.sqrt(s * (s - side[0]) * (s - side[1]) * (s - side[2]))
    return area


def perimeter_calc(side):
    perimeter = side[0] + side[1] + side[2]
    return perimeter


def main():
    while True:
        calc = input(
            "What would you like to calculate(E = Energy/A = Area of Triangle/P = Perimeter of Triangle: "
        ).upper()
        try:
            if calc == "E" or calc == "ENERGY":
                mass_u = int(input("What is the mass of your object: "))
                answer = energy_calc(mass_u)
                print("The energy in this object is: {:.2e}".format(answer))
            elif calc == "A" or calc == "AREA":
                side_u = list(
                    map(
                        int,
                        input("Input the 3 sides of the triangle\n").strip().split(),
                    )
                )
                if len(side_u) != 3:
                    print("you have to input 3 sides")
                else:
                    answer = area_calc(side_u)
                    print("Your triangle's area is: {:.2f}".format(answer))
            elif calc == "P" or calc == "PERIMETER":
                side_u = list(
                    map(
                        int,
                        input("Input the 3 sides of the triangle\n").strip().split(),
                    )
                )
                if len(side_u) > 3:
                    print("you have to input 3 sides")
                else:
                    answer = perimeter_calc(side_u)
                    print("The perimeter of your triangle is: {}".format(answer))
            else:
                print("You have to enter a valid calculator")
        except:
            print("You have to input a valid number")
        input("Press <enter> to restart: ")


if __name__ == "__main__":
    main()
