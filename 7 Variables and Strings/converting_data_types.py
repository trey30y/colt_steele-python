# Lecții Python: Conversia Tipurilor de Date (Type Casting)
# Acest fișier explică cum transformăm valorile dintr-un tip de date în altul în Python.

# --- 1. Conversie Implicită (Automată) ---
# Python face conversia automat atunci când este sigur că nu se pierde informație.
x = 5          # int
y = 2.5        # float
suma = x + y   # Python transformă automat x în 5.0
print(f"Conversie Implicită: {suma} (Tip: {type(suma)})")


# --- 2. Conversie Explicită (Manuală) ---
# Folosim funcții speciale pentru a "forta" transformarea valorilor.

# A. Conversia în String: str()
# Utilă pentru a concatena numere cu text.
num = 100
# print("Rezultatul este: " + num)  # Aceasta ar genera o eroare
print("Rezultatul este: " + str(num)) # Corect: "Rezultatul este: 100"

# B. Conversia în Intreg: int()
# Transformă un float (eliminând virpulă) sau un string (dacă conține doar cifre) în întreg.
float_val = 9.99
print(f"Din float în int (taie virpulă): {int(float_val)}") # Rezultat: 9

string_num = "42"
int_val = int(string_num)
print(f"Din string în int: {int_val + 1}") # Rezultat: 43

# --- Exemplu "Thorough": Gestionarea erorilor cu try...except ---
# Dacă string-ul conține litere (ex: "42ree"), int() va genera un ValueError.
user_input = "42ree"

try:
    num = int(user_input)
    print(f"Rezultat: {num + 1}")
except ValueError:
    print(f"Eroare: '{user_input}' nu este un număr valid. Te rog să introduci doar cifre.")


# C. Conversia în Float: float()
# Transformă un întreg sau un string în număr cu virgulă.
int_val_float = float(10)
print(f"Din int în float: {int_val_float}") # Rezultat: 10.0

string_float = "19.99"
float_val_from_str = float(string_float)
print(f"Din string în float: {float_val_from_str + 1}") # Rezultat: 20.99

# D. Conversia în Colecții
# Transformăm date între structuri diferite.
text = "ABC"
lista = list(text)          # Transformă stringul în listă: ['A', 'B', 'C']
set_unice = set("AABBC")     # Transformă în set (elimină duplicate): {'A', 'B', 'C'}
tuplu = (1, 2, 3)    # Transformă direct în tuplu (corect): (1, 2, 3)

print(f"Listă: {lista}")
print(f"Set unic: {set_unice}")
print(f"Tuplu: {tuplu}")

# --- REGULĂ DE AUR ---
# Python nu poate converti un string în număr dacă acesta conține litere.
# text = "Salut123"
# print(int(text))  # Aceasta va genera un ValueError!

# --- EXEMPLU PRACTIC: Input utilizatorului ---
# Funcția input() returnează întotdeauna un STRING. 
# Pentru calcule, trebuie să convertim manual.
# user_input = input("Câte ani ai? ")  # Imaginăm că utilizatorul scrie "25"
# user_input = int(user_input)       # Convertim stringul "25" în numărul 25
# anul_viitor = user_input + 1
# print(f"Anul viitor vei avea {anul_viitor}")
