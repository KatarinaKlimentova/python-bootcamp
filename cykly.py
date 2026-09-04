#aj cykly ako podmienky koncit dvojbodkou, rovnake odsedednie miesto {}
"""
for i in "Python":
    print(i)

for i in range(5):
    print(i)
"""

x = 1
for i in range(10):
    print (f" 7 x {x} = {7 * x}")
    x+= 1

sucet = 0
for i in range(101):
    sucet+= i
    i+=1
print(f"{sucet}")

i = 1
for i in range (21):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


faktorial = input("Zadaj cislo: ")
faktorial = int(faktorial)
povodne_cislo = faktorial

print(f"{i} i pred cyklom")
for i in range(faktorial - 1, 0, -1):
    faktorial = faktorial * i

    
    

print(f"{povodne_cislo}! = {faktorial}")