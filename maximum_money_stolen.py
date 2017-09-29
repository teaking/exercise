#Maximum money stolen 
#Each house having some amount of money
#Thief is going to steal this money but has a constraint/rule 
#he cannot steal two adjacent houses. 
#Find the maximum money he can rob.
no_houses=50
money_holds=10

def maximum_money(house, money):
  maximum_stolen=(house//2 + house % 2) * money
  return maximum_stolen
  
print (maximum_money(no_houses, money_holds))  
  