nombredenote = 0
total = 0
note = 0
while note != "stop":
    note = input("Entrez une note ou stop pour arrêter: ")
    if note != "stop":
        coef = input("Entrez le coefficient de la note: ")
        noteaveccoef = int(note) * int(coef)
        coef = int(coef)  # Convert coef to an integer
        nombredenote = nombredenote + 1
        total = int(noteaveccoef)+ total
        print("La moyenne est de: ", total / nombredenote)
