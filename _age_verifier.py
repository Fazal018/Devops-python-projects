#Ask the user for their name and age. If they are 18 or older, print a welcome message. Otherwise, print a rejection message
name=input("Enter your name : ")
age=int(input("Enter your age : "))

if age>= 18:
    print (f"welcome {name} to Devops")
    
else:
    print(f"Sorry {name} , You are not valid at !")
    
    
