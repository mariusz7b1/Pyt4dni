
from os import system
system('cls')


def liczby(*args):
    assert args, "Brak parametrów"
    for arg in args:
        assert isinstance(arg, int), "Tylko int"
    return sum(args), min(args), max(args)


suma, minimum, maximum = liczby(1, 34, 4, 4, 4, 46, 6, 6)
print(suma, minimum, maximum)

# suma, minimum, maximum = liczby()
suma, minimum, maximum = liczby(1, '4', 4, 4, 4, 46, 6, 6)
