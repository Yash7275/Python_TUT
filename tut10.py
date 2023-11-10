d1 = {}
d2={"Yash":"Pizza", "Kiyotaka": "Noodles"}
#print(d2["Kiyotaka"])

#too add new words in dictionary write like this
"""d2["Senku"] = "Ramen"
#print(d2)
d2["Tsukasa"]= "Paper"
#print(d2)
del d2["Tsukasa"]
print(d2)"""

"""we use this add new copy of same dictionary without old ones gets changed"""
d4=d2.copy()
del d4["Kiyotaka"]
#print(d2)
#print(d4)

 # to get the value of keyword use this
#print(d2.get("Yash"))

# to update new keyword in dictionary use this
d2.update({"Gabimaru":"Maggi"})
#print(d2)

#print(d2.keys())

print(d2.items())
