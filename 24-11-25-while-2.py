usr_int = "bob"
psw_int = "bobby"

usr = input("Enter your Username: ").lower()
psw = input("Enter your Password: ").lower()

while usr != usr_int and psw != psw_int:
    print("incorrect") 
    usr = input("Enter your Username: ").lower()
    psw = input("Enter your Password: ").lower()
print("Welcome to the system")
