import random

karty = []

class Karta:
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa
        self.wartosc = wartosc

    def __str__(self):
        return f"{self.nazwa} (wartość: {self.wartosc})"

karta1 = Karta("1", 1)
karty.append(karta1)
karta2 = Karta("2", 2)
karty.append(karta2)
karta3 = Karta("3", 3)
karty.append(karta3)
karta4 = Karta("4", 4)
karty.append(karta4)
karta5 = Karta("5", 5)
karty.append(karta5)
karta6 = Karta("6", 6)
karty.append(karta6)
karta7 = Karta("7", 7)
karty.append(karta7)
karta8 = Karta("8", 8)
karty.append(karta8)
karta9 = Karta("9", 9)
karty.append(karta9)
karta10 = Karta("10", 10)
karty.append(karta10)
karta11 = Karta("Dama", 10)
karty.append(karta11)
karta12 = Karta("Jopek", 10)
karty.append(karta12)
karta13 = Karta("Król", 10)
karty.append(karta13)
karta14 = Karta("As", 11)
karty.append(karta14)

kartaGracza1 = random.choice(karty)
kartaGracza2 = random.choice(karty)
kartaGracza3 = random.choice(karty)
kartaBota1 = random.choice(karty)
kartaBota2 = random.choice(karty)

print(f"Twoje karty to {kartaGracza1.nazwa} i {kartaGracza2.nazwa}")
wybor = input("Hit/Stand? (h/s)")
if(wybor == "s"):
    sumaUzytkownika = kartaGracza1.wartosc + kartaGracza2.wartosc