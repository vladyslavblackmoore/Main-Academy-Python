import math
import sys

data_dict = {"Mercury": {'Radius': 58, 'Speed': 47.87}, "Venus": {'Radius': 108, 'Speed': 35.02},
             "Earth": {'Radius': 150, 'Speed': 29.78}, "Mars": {'Radius': 228, 'Speed': 24.13},
             "Jupiter": {'Radius': 778, 'Speed': 13.07}, "Saturn": {'Radius': 1429, 'Speed': 9.69},
             "Uranus": {'Radius': 2871, 'Speed': 6.81}, "Neptune": {'Radius': 4504, 'Speed': 5.43}}


def planet_year(planet):
    return 2 * math.pi * data_dict[planet]['Radius'] * 1000000 / data_dict[planet]['Speed'] / (60 * 60 * 24)


def bigger_planet(year1, year2):
    if year1 > year2:
        return planet1
    else:
        return planet2


while True:
    try:
        planet1 = input('Planet 1: ')
        planet_year1 = planet_year(planet1)
    except KeyError:
        print('Error name planet')
        continue

    try:
        planet2 = input('Planet 2: ')
        planet_year2 = planet_year(planet2)
    except KeyError:
        print('Error name planet')
        continue

    print(f"The year is {int(planet_year1)} days on {planet1}")
    print(f"The year is {int(planet_year2)} days on {planet2}")
    print(f"The {bigger_planet(planet_year1, planet_year2)} year is bigger")
    break
