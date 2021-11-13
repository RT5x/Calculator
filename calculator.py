print("Simple Calculator")




def prompt_operator():
  print("select an option")
  print("1: Addition, 2: Subtraction, 3: Multiplication, 4: Division, 5: Exponents, 6: Square Root, 0: Quit")

  x = input("Type a number for your selection: ")
  try: 
    x = (int)(x)
    if(x < 0 or x > 6):
      print("INVALID")
    x = 0
  except ValueError:
    print("INVALID")
    x = 0

  
  return x


def prompt_number():
  number = input("Please enter a number")
  try:
    number = (float)(number)

  except ValueError:
    print("INVALID")
    return None
  return number


def calculate_result(operator, num1, num2):
  if(operator == 1):
    return num1 + num2
  if(operator == 2):
    return num1 - num2
  if(operator == 3):
    return num1 * num2
  if(operator == 4):
    try:
      return num1 / num2
    except ZeroDivisionError:
      print("Can't divide by Zero")
      return None
  if(operator == 5):
    return num1 ** num2
  if(operator == 6):
    return num1 ** 0.5




