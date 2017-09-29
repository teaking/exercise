#two string s1 ans s2 provided, merge these two string alternatively
string1="hello"
string2="bye"
string3="abc" 
string4="def"

def mergeAlternative(string1, string2):
  output_string=""
  for i in range(len(string1)):
    if len(string1) > i:
      output_string += string1[i]
    if len(string2) > i:
      output_string += string2[i]
  return output_string  

print(mergeAlternative(string3,string4))    