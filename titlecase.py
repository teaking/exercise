
#Program to title case every first letter of words in string
str="i love python, python is love, python is 4 lyf"
strArr=str.split()
tile_case=""
for words in strArr:
  word=words[:1].upper() + words[1:]
  tile_case += word + " "

print (tile_case)

#using python moudle capitalize to capitalized first character of string
strArr=str.split()
tile_case=""
for words in strArr:
  word=words.capitalize()
  tile_case += word + " "

print (tile_case)

# using python module titlecase 
from titlecase import titlecase
print (titlecase(str))

#output - I Love Python, Python Is Love, Python Is 4 Lyf. 

