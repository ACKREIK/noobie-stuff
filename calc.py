

ready = False
answer = None
choice = None



if not ready:
    print("Prep...")


    while True:
   
        choice = input("Enter your operation or put quit, */x, -, +, /: ")

  
        if choice in ('x', '*', '/', '+', '-'):
            num1 = float(input(""))
            num2 = float(input(""))
        if not choice in ('x', '*', '/', '+', '-') and choice != "quit":
            print("False Input")
        if choice == 'quit':
            quit()
        if choice == '+':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '-':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '*':
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == 'x':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '/':
            print(num1, "/", num2, "=", num1 / num2)
        
        
        next_calculation = input("More? (n/no to quit, anything else to continue) ")
        if next_calculation == "no":
          quit()
        