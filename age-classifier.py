# Take user input for age.
age = int(input ("Enter your age: "))


# output a variety of responses based on what the user enters.
if age < 13:
   print("You qualify for the kiddie account.")

elif age == 21:
    print("Congrats on your 21st!")

elif age >= 40 :
    print("You're over the hill.")

elif age >= 65:
    print ("Enjoy your retirement!")

elif 65 < age < 100:
    print ("Enjoy retirement.")

elif age >= 100:
    print("Sorry, you're dead.")
    
else:
    print ("Age is but a number.")


