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
print(f"Seznam vstuních prvků:\n{numbers}")

#použití algoritmu bubble sort k setřídění seznamu
#zjištění délky seznamu
lenght = len(numbers)
#průchod všech prvků v seznamu tolikrát kolik jich v seznamu je (mínus poslední)
for i in range(lenght-1):
    #průchod všech prvků v seznamu (kromě posledního), jejich porovnání vůčí prvku napravo a popř. prohození
    for j in range(lenght-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
#vypsání setříděného seznamu uživateli
print(f"Setřízené prvky:\n{numbers}")

