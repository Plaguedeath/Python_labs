list_names = []
while(True):
    fullname = input("Введите ФИО:")
    if not fullname.strip():
        break

    second_name, first_name, surname = fullname.split(" ")

    # second_name = second_name.capitalize()
    # f = first_name[0].upper()
    # s = surname[0].upper()

    list_names.append(f"{second_name.capitalize()} {first_name[0].upper()}.{surname[0].upper()}.")

print(list_names)

    







