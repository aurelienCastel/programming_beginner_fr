#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_input = raw_input("Entrez le nom d'un jour de la semaine (en minuscules): ")

if user_input == "lundi":
    print "lundi est le premier jour de la semaine"
elif user_input == "mardi":
    print "mardi est le deuxième jour de la semaine"
elif user_input == "mercredi":
    print "mercredi est le troisième jour de la semaine"
elif user_input == "jeudi":
    print "jeudi est le quatrième jour de la semaine"
elif user_input == "vendredi":
    print "vendredi est le cinquième jour de la semaine"
elif user_input == "samedi":
    print "samedi est le sixième jour de la semaine"
elif user_input == "dimanche":
    print "dimanche est le septième jour de la semaine"
else:
    print "Veuillez saisir un jour de la semaine, en minuscules."
