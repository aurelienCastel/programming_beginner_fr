#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_input = raw_input("Entrez votre age:")

if int(user_input) >= 21:
    print "Vous êtes majeur partout dans le monde."
elif int(user_input) >= 18:
    print "Vous êtes majeur dans la plupart des pays."
else:
    print "Vous êtes mineur dans la plupart des pays."
