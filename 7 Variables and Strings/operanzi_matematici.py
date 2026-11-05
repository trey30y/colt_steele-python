"""
Acest fișier demonstrează principalii operatori matematici în Python.
Fiecare secțiune este documentată pentru claritate.
"""

import math

# Definim variabilele de bază
a = 10
b = 3

# ==========================================
# 1. Adunarea (+)
# Adună cele două valori
# ==========================================
rezultat_adunare = a + b

# 2. Scăderea (-)
# Scade valoarea lui b din a
rezultat_scadere = a - b

# 3. Înmulțirea (*)
# Înmulțește cele două valori
rezultat_inmultire = a * b

# 4. Împărțirea (/)
# Returnează rezultatul sub formă de float (număr cu virgulă)
rezultat_impartire = a / b

# 5. Împărțirea întreagă (//)
# Returnează doar partea întreagă a împărțirii (ignoră restul)
rezultat_impartire_intreaga = a // b

# 6. Modulo (%)
# Returnează restul împărțirii
rezultat_modulo = a % b

# 7. Exponențierea (**)
# Ridică valoarea lui a la puterea lui b
rezultat_putere = a ** b
# 8. Radical (Putere fracționară)
# Radicalul dintr-un număr este egal cu ridicarea acelui număr la puterea (1/n)
# Exemplu: radical din a (a ** 0.5)
rezultat_radical = a ** 0.5

# Alternativ, folosind biblioteca 'math' pentru mai multă precizie:
rezultat_radical_math = math.sqrt(a)


