""" Topic in this Chapter:-
 1) Dictionary- Key: Value Pairs
 2) Working With Dictionaries
 3) Dictionary Function and Method
 """
# Dictionaries = Another type of collection in  python
""" unlike other
dictionaries have = "Key "{Rather than indices}
 and a value of that key
 """
# In Case to find the elements in dictionaries you have to memorize the key.


# To Create A Dictionaries

# its syntax:-
#<Dictionary-name> = {<Key>: <value>,<Key>: <value>,<Key>: <value>,.... }

# Eg:-
"""
Teachers = {"Dimple":"Computer Science", "Karen":"Socialogy","Harpreet":"Mathematics"}
# dimple,Karen,Harpreet = Key and C.S , Socialogy,Maths = Value

# Key (Dictionaries) = Immutable Type
# Dictionaries = associative arrays or mapping or hashes

# Accessing Elements Of a Dictionary:-

#its Syntax:-
#<Dictionary-name> [<keys>]

print(Teachers["Karen"])
"""
# Duplicate Not Allowed
"""
In Dict. 2 items not = same key

if one have key and we add same key with other key value then
new key = other key.
"""
# Dict. Length
""" Use len(Dict_name)"""

# Traversing  = repeating the same program.
"""
student= {1:3,"Name":"Yash"}
eg. for i in student:
    print(i,":", student [i])
    """
# To remove dictionary elements and dictionary
"""using del element
to remove a element or elements 

del.Dict_name.[key_value]

and

for deleting entire dict.
use clear statement

Dict_name.clear

"""
"""
# Program to count the frequency of elements in a list using a dict.

L=[1,2,2,3,3,3,3,3,4,4,4,9]
count ={}
for ele in L:
    if ele in count:
        count[ele]+= 1
    else:
        count[ele] = 1
for key_value in count.items():
    print(L,"{Keys}","{Value}")
"""
# Use of split function
"""text = "This is sample string"
word= text.split()# Split function breaks string into words and create a list out of it.
print(word)"""

"""
aDict ={'Bhavna':1,'Richard':2,'Firoza':10,'Arshoor':20}
temp = 0
for value in aDict.values():
    temp= temp+value
print(temp)
"""
"""# Output of the code
d1 ={5 :[6,7,8], "a": (1,2,3)}
print(d1.keys())# Result = ['a',5]
print(d1.values()) # Result = [(1,2,3),[6,7,8]]
"""
myDict = {"a":27, "b":43, "c":25,"d":30}
valA = ''
for i in myDict:
    if i > valA:
        valA = i
        valB = myDict[i]
#print(valA)
#print(valB)
#print(30 in myDict)
myLst = list(myDict.items())
myLst.sort()
print(myLst)




