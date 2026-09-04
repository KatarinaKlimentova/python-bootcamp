#za podmienkou vzdy:  , s rovnakym odsadenim rovnaky blok
#nemiesat tab a medzeri, tab velkost 4 medzier
body = input("Kolko bodov si mala? ")
body = int(body)

if 100 >= body >= 91:
    print("Hodnotenie: A")
elif 90 >= body >= 81:
    print("Hodnotenie: B")
elif 80 >= body >= 71:
    print("Hodnotenie: C")
elif 70 >= body >= 61:
    print("Hodnotenie: D")
elif 60 >= body >= 51:
    print("Hodnotenie: E")
elif 50 >= body >= 0:
    print("Hodnotenie: Fx")
else:
    print("nespravne zadane")
