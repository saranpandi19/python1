import random
print("Welcome to randm password generator!")
randomchars="1234567890asdfghjkl;zxcvbnm!@#$%^&*()"
noofpass=int(input("please enter a no of password: "))
lenpass=int(input("Length of password: "))
print("Here are your random passwords: ")

for x in range (noofpass):
    x = ""
    for chars in range (lenpass):
        x = x + random.choice(randomchars)
    print(x)
