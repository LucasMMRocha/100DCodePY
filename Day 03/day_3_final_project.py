# Final Project

print("Wellcome to my choice game!")

choice_1 = input('''Voce esta dentro de uma taverna,
voce quer sair ou continuar dentro? Dentro ou sair\n''')

choice_1.lower()

if choice_1 == "dentro":
  
  choice_2 = input('''Voce descobriu uma porta curiosa dentro da taverna, o que quer
  fazer? Entrar ou sair\n''')
  
  choice_2.lower()
  
  if choice_2 == "entrar":
    print("Parabens voce chegou no mundo misterioso, parabens!!!\n")
    
  else:
    print("Voce foi morto por bandidos. Game over...\n")
    
else:
  print("Voce foi morto por bandidos. Game over...\n")