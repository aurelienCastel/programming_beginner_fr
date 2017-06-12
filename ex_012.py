#!/usr/bin/env python
# -*- coding: utf-8 -*-

first_input = int(raw_input("Entrez un nombre: "))
second_input = int(raw_input("Entrez un nombre: "))
third_input = int(raw_input("Entrez un nombre: "))

order_input = raw_input("Entrez 'croissant' ou 'décroissant' pour afficher les nombres dans l'ordre voulu: ")

if first_input > second_input:
    highest_number = first_input
    lowest_number = second_input
else:
    highest_number = second_input
    lowest_number = first_input

if third_input > highest_number:
    medium_number = highest_number
    highest_number = third_input
elif third_input > lowest_number:
    medium_number = third_input
else:
    medium_number = lowest_number
    lowest_number = third_input

# Second solution

# if first_input > second_input:
#     if third_input > first_input:
#         highest_number = third_input
#         medium_number = first_input
#         lowest_number = second_input
#     elif third_input > second_input:
#         highest_number = first_input
#         medium_number = third_input
#         lowest_number = second_input
#     else:
#         highest_number = first_input
#         medium_number = second_input
#         lowest_number = third_input
# else:
#     if third_input > second_input:
#         highest_number = third_input
#         medium_number = second_input
#         lowest_number = first_input
#     elif third_input > first_input:
#         highest_number = second_input
#         medium_number = third_input
#         lowest_number = first_input
#     else:
#         highest_number = second_input
#         medium_number = first_input
#         lowest_number = third_input

# Third solution
# 
# if first_input > second_input:
#     if first_input > third_input:
#         highest_number = first_input
#         if second_input > third_input:
#             medium_number = second_input
#             lowest_number = third_input
#         else:
#             medium_number = third_input
#             lowest_number = second_number
#     else:
#         medium_number = first_input
#         highest_number = third_input
#         lowest_number = second_input
# else:
#     if first_input > third_input:
#         medium_number = first_input
#         highest_number = second_input
#         lowest_number = third_input

if order_input == "croissant":
