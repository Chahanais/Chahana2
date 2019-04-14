#Program author- Chahana Regmi
#Exercise-3
#----------------------
#Step 1: (I) Ask the user to input a number
user_input1=int(input('input a number 1, 2, 3='))
print('Debug Step 1', user_input1)

#Step 2: (P) If the number is 1
if user_input1==1:
    #Step 3: (O) Display “Green")
    print('Green')

#Step 4: (P) If the number is 2
elif user_input1==2:
        #Step 5: (O) Display “Yellow”
        print('Yellow')

#Step 6: (P) If the number is 3
elif user_input1==3:
        #Step 7: (O) Display “Red”
        print('Red')
        
#Step 8: (P) If the number is other than 1, 2, 3
else:
        #Step 9: (O) Display “invalid number”
        print('invalid number')
