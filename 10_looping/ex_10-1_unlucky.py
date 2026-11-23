# loop through 1-20
# for 4, 13 print "x is unlucky"
# x is even, or x is odd for the rest

for num in range(1, 21):
  if num == 4 or num == 13:
    print(f"{num} is unlucky")
    continue
  if num % 2 == 0:
    print(f"{num} is even")
  print(f"{num} is odd")
