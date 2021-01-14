
import bcrypt
Password = input("Enter Password here: ")
hashAndSalt = bcrypt.hashpw(Password.encode(), bcrypt.gensalt())

print("Your Encrypted Password is :",hashAndSalt)

