#Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#You need to write a function that checks whether if the number passed into it is a prime number or not.

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number == 1:
        print("It's not a prime number.")
        return;
    elif number <= 0:
        print("It's not a valid number.")
        return;
    else:
        divisible_by = 0;
        for x in range(2, number):
            if (number % x) == 0:
                is_prime = False
                divisible_by = x
                break;

        if is_prime:
            print("It's a prime number.")
        else:
            print(f"It's not a prime number. It is divisible by {divisible_by}.")
        


#Write your code above this line 👆    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)