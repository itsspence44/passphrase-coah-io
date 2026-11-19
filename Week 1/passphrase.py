password = input("What is your password:")
print(password )

if password == "password":   
    print(" \nPassword is to simple, plase enter a a new password that is 15 characters")

else: 
    print("Enter a longer password that is over 15 charchters") 

user = input("Enter new password:")
print(user)

password = input("Enter a passphrase: ")

if len(password) < 15:
    print("Your passphrase is too short. Please use at least 15 characters.")

else:
    print("Your passphrase meets the length requirement.")





