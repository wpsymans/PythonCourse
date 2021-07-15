def fizz_buzz(guess: int = 1):
    """
    Text here
    """
    
    div_by_five = int(guess) % 5 == 0
    div_by_three = int(guess) % 3 == 0
    
    if div_by_five == True and div_by_three == True:
        return "fizz buzz"
    elif div_by_five == True:
        return "buzz"
    elif div_by_three == True:
        return "fizz"
    else:
        return guess
        
for guess in range(1,100):
    result = fizz_buzz(guess)
    
            