password = input("")

password = list(password)

for i in range(0, len(password)):
    if (password[i] == 'i'):
        password[i] = '!'
    elif (password[i] == 'a'):
        password[i] = '@'
    elif (password[i] == 'm'):
        password[i] = 'M'
    elif (password[i] == 'B'):
        password[i] = '8'
    elif (password[i] == 'o'):
        password[i] = '.'

good_password = ""

good_password = good_password.join(password)

good_password = good_password + "q*s"

print(good_password)