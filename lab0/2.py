def check_password(password: str) -> bool:
    if len(password) < 16:
        return False
    
    numbers = False
    symbols = False
    for i in password:
        if (i.isalpha()):
            symbols = True
        if (i.isdigit()):
            numbers = True
    

    return symbols and  numbers
    
    

password = input("Input Password: ")
if check_password(password):
    print("all good")
else:
    print("wrong")




