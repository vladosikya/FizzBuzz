FizzBuzz = True

while FizzBuzz:
    while True:
        try:
            stop = input("Specify on what number to stop the game? ")
            stop = int(stop)
            break
        except:
            print("Need number.")

    for numb in range(1, stop+1):
        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz")
        elif numb % 3 == 0:
            print("Fizz")
        elif numb % 5 == 0:
            print("Buzz")
        else:
            print(numb)
    while True:
        choose = input("Run again? 'y' or 'n' ").lower()
        if choose == 'y':
            break
        elif choose == 'n':
            FizzBuzz = False
            break
        else:
            print("Unknown command.")
