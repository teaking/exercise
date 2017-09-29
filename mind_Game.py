#mind game
#step1: choose the number range from 1 to 10
chosen_no=input("Enter chosen number from range 1 to 10")
chosen_no=int(chosen_no)
original_chosen_no=chosen_no
#step2: Double the chosen number 
chosen_no*=2
#step3: Add even number got from user to step2 result
even_number=input("Enter chosen even number to add to the new number after doubling the initial chosen no")
even_number = int(even_number)
chosen_no = chosen_no + even_number
#step4: Divide the result from step3 by 2
chosen_no /= 2
#step5: Subtract step4 with original_chosen_no
chosen_no -= original_chosen_no
print (chosen_no)