#Good or bad string 
#rules if 3 consonents together bad or more than 5 vowel then string is bad 
#else string is good 
#input string consists of wild card for this program ? is hardcoded and does not work for
#other wild cards. 
#this does not consider numericals as well 
input_str="ppaeioup?"
existing_vwl_char=0
existing_cons_char=0
vowel=["a","e","i","o","u"]

def validate_string(input_arr):
	global existing_cons_char
	global existing_vwl_char
	for c in input_str:
		#looping through input and compare if the character is vowel or string
		#print("character %c" % c) # debug purpose
		if c in vowel:
			existing_vwl_char += 1
			#from rules 3 or more consonents required to be together otherwise it does not
			#count hence reducing it back to zero
			existing_cons_char = 0
			#print ("existing vowel char %d, existing_cons_char %d " % (existing_vwl_char, existing_cons_char)) # debug purpose
		elif(existing_cons_char == 0 and c == "?"):
			#previous character was not consonent
			existing_vwl_char += 1
			#print (existing_vwl_char) # debug purpose
		elif existing_cons_char != 0 and c == "?":
			#previous character was consonent
			existing_cons_char += 1
			#print(existing_cons_char) # debug
		else:
			existing_cons_char += 1
			#print("exising cons char %d " % (existing_cons_char)) # debug purpose
	
	return "Bad" if existing_cons_char >= 3 or existing_vwl_char > 5 else "Good"  

print (input_str + " : "+validate_string(input_str))
 