def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Errore: divisione per zero"

if __name__ == "__main__":
    print("Calcolatrice Python")
    print("1. Addizione\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione")
    choice = input("Scegli un'opzione: ")

    x = float(input("Inserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))

    if choice == "1":
        print("Risultato:", add(x, y))
    elif choice == "2":
        print("Risultato:", subtract(x, y))
    elif choice == "3":
        print("Risultato:", multiply(x, y))
    elif choice == "4":
        print("Risultato:", divide(x, y))
    else:
        print("Scelta non valida.")
