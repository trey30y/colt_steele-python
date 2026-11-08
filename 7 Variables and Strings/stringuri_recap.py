# Lecții Python: Stringuri - Recapitulare completă (Colt Steele Bootcamp)

# 1. Escape Sequences - TOATE
# \"  Double Quote
# \'  Single Quote
# \\  Backslash
# \n  New Line
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
print("New Line: \nTest")
print("Tab:\tTabbed")
print("Backspace: 12\b3")
print("Carriage Return (resetează linia): 12345\rAB")
print("Octal (ASCII 101): \101")
print("Hex (ASCII 41): \x41")

# 2. String Concatenation
nume = "John"
prenume = "Doe"
nume_complet = nume + " " + prenume
print(f"\nConcatenare: {nume_complet}")

# 3. String Formatting (F-Strings)
print(f"Salut, {nume_complet}!")

# 4. String Indexing
s = "Python"
print(f"\nIndexare: '{s[0]}', '{s[-1]}'")

# 5. Converting Data Types
age = 25
print(f"Conversie: {age!s}")

# 6. Metode uzuale de string (Multe altele)
text = "  invat sa programez in python  "
print("\nMetode:")
print(f"strip(): '{text.strip()}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"replace(): '{text.replace('python', 'Python')}'")
print(f"split(): {text.split()}")
print(f"startswith(): {text.strip().startswith('i')}")
print(f"endswith(): {text.strip().endswith('n')}")
print(f"find(): {text.find('programez')}")
print(f"count(): {text.count('a')}")
print(f"isalnum(): {'Python3'.isalnum()}")
print(f"isalpha(): {'Python'.isalpha()}")
print(f"isdigit(): {'123'.isdigit()}")
parts = ['a', 'b', 'c']
print(f"join(): {'-'.join(parts)}")
