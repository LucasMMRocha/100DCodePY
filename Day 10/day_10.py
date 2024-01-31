#Functions with Outputs

def fomrat_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs!"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  
  return f"{formated_f_name} {formated_l_name}"

print(fomrat_name(input("What's your name? "), input("What's your last name? ")))

#Already useded functions with outputs.

length = len(fomrat_name)


#Return as an early exit.

def fomrat_name(f_name, l_name):
  """Take a first and last name and format it to
  return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs!"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  
  return f"{formated_f_name} {formated_l_name}"