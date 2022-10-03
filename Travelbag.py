travelbag = ["Robert"]

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program \n")

   if menyval == "1":
    for i, nej in enumerate (travelbag, start=1):
      print(i, nej,)

   elif menyval == "2":
     tillägg = input("Vad vill du lägga till? ").capitalize()
     travelbag.append(tillägg)

   elif menyval == "3":
    tabort = input("Vad vill du ta bort? ").capitalize()
    travelbag.remove(tabort)

   elif menyval == "4":
       break