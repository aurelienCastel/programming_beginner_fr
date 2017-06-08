#!/usr/bin/env python
# -*- coding: utf-8 -*-

biggest_country = "Russie"
smallest_country = "Vatican"
most_populated_country = "Chine"
second_most_populated_country = "Inde"

most_populated_country, second_most_populated_country = second_most_populated_country, most_populated_country

print "Le plus grand pays du monde est", biggest_country + "."
print "Le plus petit pays du monde est", smallest_country + "."
print "Le pays le plus peuplé du monde est", most_populated_country + "."
print "Le deuxième pays le plus peuplé du monde est", second_most_populated_country + "."
