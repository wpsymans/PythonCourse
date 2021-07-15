def factorial(guess: int = 1):
    """
    this calculates a factorial
    """
    iter = 1

    if guess == 0:
        print(1)
    else:
        for item in range(1,guess):
            iter = item*iter
        
        print(iter)

for num in range(0,36):
    factorial(num)