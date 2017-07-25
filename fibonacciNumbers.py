
userInput = int(raw_input("How many fibonacci numbers would you like to see? "))
def fibonacciNumbers(n):
    fibonacci = [1, 1]
    nPLace = [1,2]
    for i in range (1, n-1):
        twoBackNumber = fibonacci[i-1]
        oneBackNumber = fibonacci[i]
        newNumber = twoBackNumber + oneBackNumber
        fibonacci.append(newNumber)
        nPLace.append(i+3)
        i += 1
    return fibonacci

print fibonacciNumbers(userInput);
