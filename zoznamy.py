#basic zoznam 
cisla = [1,2,3,4,5]
mix_zoznam = [1, "ahoj", True, 3.14]
#dlzka zoznamu
"""
print(cisla)
print(len(cisla))
print(cisla[0])                       # 1 (prvý prvok — index od 0)
print(cisla[-1])                      # 5 (posledný — záporné indexy z konca!)
print(cisla[-2])                      # 4 (predposledný)

cisla = [10, 20, 30, 40, 50]

cisla[1:4]       # [20, 30, 40]     — od indexu 1 po 4 (vylučne)
cisla[:3]        # [10, 20, 30]     — od začiatku po 3
cisla[2:]        # [30, 40, 50]     — od indexu 2 po koniec
cisla[::2]       # [10, 30, 50]     — každý druhý
cisla[::-1]      # [50, 40, 30, 20, 10]  — obráti list!

cisla = [1, 2, 3]
cisla.append(4)       # [1, 2, 3, 4]     — pridá na koniec
cisla.insert(0, 0)    # [0, 1, 2, 3, 4]  — pridá na pozíciu 0
cisla.remove(2)       # [0, 1, 3, 4]     — odstráni PRVÝCH výskyt hodnoty 2
cisla.pop()           # [0, 1, 3]        — odstráni posledný a vráti ho
cisla.pop(0)          # [1, 3]           — odstráni na indexe 0

cisla = [3, 1, 4, 1, 5, 9, 2, 6]
cisla.sort()          # zoradí na mieste (in-place)
cisla.reverse()       # obráti na mieste
sorted(cisla)         # vráti NOVÝ zoradený, pôvodný nezmení

len(cisla)            # dĺžka
sum(cisla)            # súčet (len pre čísla!)
min(cisla)            # minimum
max(cisla)            # maximum
"""

"""
for c in cisla:
    print(c)

for i,c in enumerate(cisla):
    print(f"na indexe cislo {i} je cislo {c}")
"""

teploty = [12.5, 15.0, 8.3, 20.1, 22.4, 18.7, 14.2, 25.5, 19.0, 11.8]
print(f"Pocet merani {len(teploty)}")
print(f"priemer: {sum(teploty)/len(teploty)}")
print(f"Najnizsia teplota: {min(teploty)}")
print(f"Najvyssia teplota: {max(teploty)}")
print(f"{(max(teploty)-min(teploty))}")
print(f"{sorted(teploty)}")
print(f"{sorted(teploty)[:3]}")
print(f"{teploty[-1]}")
k = 0
print(f"pred cyklom {k}")
#range je funkcia, potrebuje ()
for i in teploty:
    if i > 20:
        k+=1

print(f"po cykle: pocet teplot nad 20 je:{k}")
