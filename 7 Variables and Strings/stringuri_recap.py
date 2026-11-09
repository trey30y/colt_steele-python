# Lecții Python: Stringuri - Recapitulare completă (Colt Steele Bootcamp)

# 1. Escape Sequences - TOATE
# \"  Double Quote
# \'  Single Quote
# \\  Backslash
#   New Line
# \t  Tab
# \b  Backspace
# \r  Carriage Return
# \f  Form Feed
# \v  Vertical Tab
# \ooo Octal value
# \xhh Hex value

print("Escape Sequences complete:")
print("Double Quote: \"")
print("Single Quote: \'")
print("Backslash: \\")
print("New Line: Test")
print("Tab:\tTabbed")
print("Backspace: 12\b3")
print("Carriage Return (resetează linia): 12345\rAB")
print("Octal (ASCII 101): \101")
print("Hex (ASCII 41): \x41")

# 2. String Concatenation
nume = "John"
prenume = "Doe"
nume_complet = nume + " " + prenume
print(f"Concatenare: {nume_complet}")

# 3. String Formatting (F-Strings)
print(f"Salut, {nume_complet}!")

# 4. String Indexing
s = "Python"
print(f"Indexare: '{s[0]}', '{s[-1]}'")

# 5. Converting Data Types
age = 25
print(f"Conversie: {age!s}")

# 6. Metode uzuale de string (Multe altele)
text = "  invat sa programez in python  "
print("Metode:")

# strip() - sterge spatiile goale de la inceput si sfarsit
print("Explicatie: strip() elimină spațiile albe de la începutul și sfârșitul șirului")
print(f"Rezultat: '{text.strip()}'")

# upper() - converteste totul in majuscule
print("Explicatie: upper() convertește toate caracterele în majuscule")
print(f"Rezultat: '{text.upper()}'")

# lower() - converteste totul in minuscule
print("Explicatie: lower() convertește toate caracterele în minuscule")
print(f"Rezultat: '{text.lower()}'")

# capitalize() - pune prima litera a stringului cu majuscula
print("Explicatie: capitalize() pune majusculă doar la prima literă din șir")
print(f"Rezultat: '{text.capitalize()}'")

# title() - pune prima litera a fiecarui cuvant cu majuscula
print("Explicatie: title() pune majusculă la prima literă a fiecărui cuvânt")
print(f"Rezultat: '{text.title()}'")

# replace() - inlocuieste o secventa de caractere cu alta
print("Explicatie: replace() înlocuiește o sub-secvență cu alta")
print(f"Rezultat: '{text.replace('python', 'Python')}'")

# split() - imparte stringul intr-o lista (implicit dupa spatii)
print("Explicatie: split() împarte șirul într-o listă bazată pe un separator")
print(f"Rezultat: {text.split()}")

# startswith() - returneaza True daca string-ul incepe cu caracterul dat
print("Explicatie: startswith() verifică prefixul șirului (returnează boolean)")
print(f"Rezultat: {text.strip().startswith('i')}")

# endswith() - returneaza True daca string-ul se termina cu caracterul dat
print("Explicatie: endswith() verifică sufixul șirului (returnează boolean)")
print(f"Rezultat: {text.strip().endswith('n')}")

# find() - returneaza indexul primei aparitii a substring-ului
print("Explicatie: find() returnează indexul (poziția) primei apariții")
print(f"Rezultat: {text.find('programez')}")

# count() - numara de cate ori apare o secventa in string
print("Explicatie: count() numără aparițiile unui sub-șir")
print(f"Rezultat: {text.count('a')}")

# isalnum() - verifica daca contine doar litere si cifre
print("Explicatie: isalnum() verifică dacă șirul este alfanumeric")
print(f"Rezultat: {'Python3'.isalnum()}")

# isalpha() - verifica daca contine doar litere
print("Explicatie: isalpha() verifică dacă șirul conține doar litere")
print(f"Rezultat: {'Python'.isalpha()}")

# isdigit() - verifica daca contine doar cifre
print("Explicatie: isdigit() verifică dacă șirul conține doar cifre")
print(f"Rezultat: {'123'.isdigit()}")

# join() - uneste elementele unei liste intr-un singur string folosind un separator
parts = ['a', 'b', 'c']
print("Explicatie: join() combină elementele unei liste într-un șir folosind un separator")
print(f"Rezultat: {'-'.join(parts)}")
