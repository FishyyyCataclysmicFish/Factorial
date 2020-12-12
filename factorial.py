while True:  ##infinite loop
    num = int(input("Enter a number greater than or equal to zero:"))  ##user enter number
    if num >= 0:  ##returns factorial of number
        counter = 1
        f = 1
        while  counter <= num:
            f = f * counter
            counter += 1
        print("The factorial of {} is {}".format(num, f))
    if num < 0:  ##if user enters a negative number, there is no factorial
        print("That's not a number greater than or equal to zero...")
        print("NO FACTORIAL FOR {}".format(num))
