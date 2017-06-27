#!/usr/bin/env python
#-*- coding: utf-8 -*-

first_input = int(raw_input("Entrez un nombre: "))
second_input = int(raw_input("Entrez un nombre: "))
third_input = int(raw_input("Entrez un nombre: "))

order_input = raw_input("Entrez 'croissant' ou 'décroissant' pour afficher les nombres dans l'ordre voulu: ")

if first_input >= second_input and second_input >= third_input:
    highest_number = first_input
    medium_number = second_input
    lowest_number = third_input

if first_input >= third_input and third_input >= second_input:
    highest_number = first_input
    medium_number = third_input
    lowest_number = second_input

if second_input >= first_input and first_input >= third_input:
    highest_number = second_input
    medium_number = first_input
    lowest_number = third_input

if second_input >= third_input and third_input >= first_input:
    highest_number = second_input
    medium_number = third_input
    lowest_number = first_input

if third_input >= first_input and first_input >= second_input:
    highest_number = third_input
    medium_number = first_input
    lowest_number = second_input

if third_input >= second_input and second_input >= first_input:
    highest_number = third_input
    medium_number = second_input
    lowest_number = first_input

if order_input == "croissant":
    print lowest_number, "<", medium_number, "<", highest_number
else:
    print highest_number, ">", medium_number, ">", lowest_number
