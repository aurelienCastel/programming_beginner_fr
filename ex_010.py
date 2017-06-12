#!/usr/bin/env python
# -*- coding: utf-8 -*-

first_input = raw_input("Entrez une lettre de l'alphabet: ")
print "Vous avez entré la lettre " + first_input + "."

second_input = raw_input("Entrez une lettre de l'alphabet: ")
print "Vous avez entré la lettre " + second_input + "."

if first_input > second_input:
    print "La première lettre est plus proche de la fin de l'alphabet."
elif first_input < second_input:
    print "La deuxième lettre est plus proche de la fin de l'alphabet."
else:
    print "Les deux lettres sont identiques."
