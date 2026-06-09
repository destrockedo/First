name = input("What is your name?")
print("Hello" , name)
print("You must 18 in order to aceess this content")
age = int(input("What is your age?"))
if age >= 18: 
    print("Welcome", name)
else: print("Your are not permitted access to this content")