from alphabet import alphabet

def ceaser(direction, text, shift):

  new_text = ""
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      if direction == 'encode':
        new_position = position + shift
      elif direction == 'decode':
        new_position = position - shift
      new_letter = alphabet[new_position]
      new_text += new_letter
  
    else:
      new_text += char
  
  print(f"The {direction}d text is {new_text}")