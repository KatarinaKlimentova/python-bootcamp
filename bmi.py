"""
meno = input("ako sa volas? ")
print(f"Ahoj, {meno}")

meno = input("ako sa volas? ")
print(f"ako sa mas? {meno}")
nalada = input()
print(f"{meno} sa ma {nalada}")
"""

#input berie ako str, musi sa pretypovat nech sa s tym moze potom inak robit
#vek = int(input("vek: "))
#priemer = float(input("priemer je:"))
#str najprv na float potom na int
#pi = "3.14"
#print(f"pi pred zmenou je {pi}")
#ked chcem pretypovat musim ulozit aj naspat do tej premennej 
#pi = int(float(pi))
#print(f"{pi + 2}")

meno = input("Ako sa volas? ")
vaha = input("Kolko vazis? ")
vyska = input("Aka si vysoka? ")

vaha = float(vaha)
vyska = float(vyska)


print(f"Ahoj, {meno}!")
print(f"Tvoje BMI je {vaha/ (vyska*vyska):.2f}")