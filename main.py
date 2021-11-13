def main():
  print("Welcome to Calculator")
  while(True):
    operator = calc.prompt_operator()
    if(operator == 0):
      break
    num1 = calc.prompt_number()
    num2 = calc.prompt_number()

    if(num1 == None or num2 == None):
      break
  
    result = calc.calculate_result(operator, num1, num2)

    if(result == None):
      break
    
    print("Result: " + str(result))




if __name__ == "__main__":
  main()
  print("Exiting")

