#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_input = raw_input("Entrez votre age:")
converted_user_input = int(user_input)

if converted_user_input < 18:
    message = "Vous êtes mineur dans la plupart des pays."
elif converted_user_input < 21:
    message = "Vous êtes majeur dans la plupart des pays."
else:
    message = "Vous êtes majeur partout dans le monde."

print message
