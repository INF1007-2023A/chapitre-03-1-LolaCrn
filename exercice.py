#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    root = math.sqrt(a)
    return root


def square(a: float) -> float:
    sqr= math.pow(a,2)
    return sqr


def average(a: float, b: float, c: float) -> float:
    moyenne = (a+b+c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    min = angle_mins/60
    sec= angle_secs/3600
    rad= (angle_degs+min+sec)*(math.pi/180)
    return rad


def to_degrees(angle_rads: float) -> tuple:
    raw_deg = angle_rads*(180/math.pi)
    min = (float(raw_deg%1))*60
    sec=(float(min%1)*60)
    raw_deg=int(raw_deg)
    min=int(min)
    sec=int(sec)
    return raw_deg, min, sec


def to_celsius(temperature: float) -> float:
    tempC=(temperature-32)/1.8
    return tempC


def to_farenheit(temperature: float) -> float:
    temp= (temperature*1.8)+32
    return temp


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
