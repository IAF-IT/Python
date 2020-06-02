import re

mytext = '"Geraldine", "Kitzbühel" "Egestas Aliquam Institute" "enim.non.nisi@mattissemperdui.org" "Daryl" "Ahmadpur East", "Nunc Commodo Auctor Limited", "vitae@amet.co.uk" "Blythe", "Fort Resolution", "Non Bibendum Sed LLP", "molestie.in@lectus.org" "Veda", "Calco", "Enim Diam PC", "nunc.sed@porttitorvulputateposuere.org" "Hayley", "Bansberia", "A PC", "cursus@magnaetipsum.org""Driscoll", "Rajkot", "Quis Company",	"elit@turpisnonenim.net" "Walter", "Chandler",	"Phasellus Consulting",	"mauris.erat.eget@sedfacilisisvitae.edu" "Gwendolyn", "Korba", '

"""
\d    = 0-9
\D    = non DIGGIT
\w    = [A-Z][a-z]
\W    = not wolds
\s    = space
\S    non space
"""


textlookfor = r"\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)