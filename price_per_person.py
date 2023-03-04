#!/usr/bin/env python3

"""
Author: Luis D. Santiago
Created: xx/yy/2017
Last Edited: 02/28/2023

todo:
- Refactor processes into functions
- Create a class structure

"""

"""
USE AT YOUR OWN RISK!
"""


# People staying in the hotel and their night counts
#
Sdot = 9
Hdot = 9
Kdot = 7
Ldot = 1
Jdot = 1
Cdot = 3

# Total Price for the stay
#
tt = 893.07

# Total Price per night for NINE nights
#
TOTAL = round(tt/9, 2)

# Breakdown of Total price per night
#  Accounts for the number of people who stay per night
x2 = TOTAL/2
x3 = TOTAL/3
x4 = TOTAL/4
x5 = TOTAL/5

# Breakdown of the price per night stretch
#  Accounts for the number of people who stay during that stretch
night1 = x3
night2_4 = x4*3
night5_6 = x3*2
night7 = x5
night8_9 = x2 *2

# Breakdown of the amount each person pays during their stay
#
Sdot = night1 + night2_4 + night5_6 + night7 + night8_9
Hdot = night1 + night2_4 + night5_6 + night7 + night8_9
Kdot = night1 + night2_4 + night5_6 + night7
Ldot = night7
Jdot = night7
Cdot = night2_4

print(f"Sdot pays: {Sdot}")
print(f"Hdot pays: {Hdot}")
print(f"Kdot pays: {Kdot}")
print(f"Ldot pays: {Ldot}")
print(f"Jdot pays: {Jdot}")
print(f"Cdot pays: {Cdot}")

TOTAL = Sdot + Hdot + Kdot + Ldot + Jdot + Cdot

print(f"Total Price for the stay: {TOTAL}")

print(f"First night price per person {night1}")
print(f"2nd thru 4th night price per person {night2_4}")
print(f"5th thru 6th night price per person {night5_6}")
print(f"7th night price per person {night7}")
print(f"8th thru 9th night price per person {night8_9}")
