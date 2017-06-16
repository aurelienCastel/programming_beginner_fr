#!/usr/bin/env python
# -*- coding: utf-8 -*-

order_input = raw_input("Entrez 'croissant' ou 'décroissant' pour afficher les nombres dans l'ordre voulu: ")

if order_input == "croissant":
    first_input = int(raw_input("Entrez un nombre: "))
    second_input = int(raw_input("Entrez un nombre (plus grand que le précédent): "))
    if second_input > first_input:
        third_input = int(raw_input("Entrez un nombre (plus grand que le précédent): "))
        if third_input > second_input:
            print "Félicitation vous avez entré trois nombres croissants."
        else:
            print "Vous devez entrer des nombres dans un ordre croissant."
    else:
        print "Vous devez entrer des nombres dans un ordre croissant."

elif order_input == "décroissant":
    first_input = int(raw_input("Entrez un nombre: "))
    second_input = int(raw_input("Entrez un nombre (plus petit que le précédent): "))
    if second_input < first_input:
        third_input = int(raw_input("Entrez un nombre (plus petit que le précédent): "))
        if third_input < second_input:
            print "Félicitation vous avez entré trois nombres décroissants."
        else:
            print "Vous devez entrer des nombres dans un ordre décroissant."
    else:
        print "Vous devez entrer des nombres dans un ordre décroissant."
else:
    print "Veuillez choisir 'croissant' ou 'décroissant'."
