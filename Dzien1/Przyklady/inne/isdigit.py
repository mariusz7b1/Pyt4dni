while True:
    liczba = input("Podaj liczbę ")
    if liczba.isdigit():
        liczba = int(liczba)
        break
print(liczba)
