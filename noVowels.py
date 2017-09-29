#remove vowels from input string and print outthe string without vowels
vowels_array=["a","e","i","o","u"]
input_str="welcome to geeksforgeeks"
output_str=""
for characters in input_str:
	#if the characters is not in vowel array then add to output string
  if characters not in vowels_array:
    output_str +=characters
    
print (output_str)

#using try and except to check if the input_string has value from the 
#vowel_array
for characters in input_str:
  try:
  	#check if the vowel_array consists the character 
    vowels_array.index(characters)
  except ValueError:
  	#if character does not exists then append to output string
    output_str +=characters
  #else:
  # print("no value error occured neither can be found in the vowels_array")
    
print (output_str)

