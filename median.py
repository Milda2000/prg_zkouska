#incializace seznamu vstupních hodnot
numbers = []
#získání vstupních hodnot od uživatele a jejich ověření
while True:
    try:
        numbers = [float(num) for num in input("Zadejte číselné hodnoty, které chcete setřídit (oddělené mezerou): ").split()]
        if len(numbers) < 2:
            print("Zadejte alespoň dvě hodnoty")
        else:
            break
    except ValueError:
        print("Zadané hodnoty nebyly číselné")
#vypsání vstupních hodnot uživateli   
print(numbers)

#setřídění seznamu
numbers.sort()

#zjištění dálky seznamu a podle ní rozhodnutí o způsobu vyopčítání mediánu
list_lenght = len(numbers)
#pokud je seznam sudý medián bude průměrem dvou prostředních prvkům v seznamu
if list_lenght%2 == 0:
    num1 = numbers[int((list_lenght/2)-1)]
    num2 = numbers[int(list_lenght/2)]
    median = (num1+num2)/2
else:
    #pokud je seznam lichý median bude odpovídat prostřednímu prvku v seznamu
    median = numbers[list_lenght//2]

#vypsání výsledného mediánu vstupních dat pro uživatele do konzole
print(f"Medián vstupních dat je: {median}")