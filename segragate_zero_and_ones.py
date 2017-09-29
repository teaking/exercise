#segragate 0s and 1s
#given arrays of 0s and 1s in random order
#segragate 0s on the left side and 1s on the right side of the array
input_array=[0,1,1,0,0,1,0,1,1,1,1]
input_array_len=len(input_array)
index=0;
for i in range(input_array_len):
  if(input_array[i] == 1):
    index=i
    for j in range(index,input_array_len):
      if (input_array[j] == 0):
        input_array[i],input_array[j]=input_array[j],input_array[i]
        #when found break the loop, do not required to loop through to the end
        break
         
      
print (input_array)      
  