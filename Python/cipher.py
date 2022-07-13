#harshal cipher
letters=input("Enter the text to be converted into ciphertext : ")
z=26
numbers = []
for letter in letters:
  number = ord(letter) - 97
  numbers.append(number)
  
for number in numbers:
    number=number + 3 #additive cipher
    a=number % z + 65
    print(chr(a))






