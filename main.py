from art import logo
from list import alphabet

def caeser(start_text, shift_amount, cipher_direction):
  end_text = ""
  if direction == "decode":
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {direction}d text is {end_text}")

print(logo)

should_end = False
while not should_end:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caeser(start_text = text, shift_amount = shift, cipher_direction = direction)

  try_again = input("Do you want to try again? Type 'y' for Yes or 'n' for No: \n")
  if try_again == "n":
    should_end = True
    print("Goodbye")