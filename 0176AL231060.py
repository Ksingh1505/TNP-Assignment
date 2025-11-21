#Name:Komal Singh
#Enrollment:0176AL231060
#Batch: Batch-5(MTF)
#Batch Time: 10:30 am

''' **************************** BASIC IF-ELSE Question*********************************** '''
#Write a program to check whether a number is positive, negative, or zero.

'''num=int(input("Enter a number: "))
if num>0:
    print("The number is Positive")
else:
    if num<0:
        print("The number is Negative")
    else:
        print("The number is zero")'''


#Write a program to check whether a number is even or odd.

'''num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even")

else:
    print("The number is odd")'''

#Write a program to check if a given year is a leap year or not.

'''year=int(input("Enter a year: "))
if year%400 == 0:
    print(year,"is a leap year")
else:
    if year%100 ==0:
        print(year,"is not a leap year")
    else:
        if year%4 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")'''

#Write a program to find the greatest of two numbers.

'''num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1 > num2:
    print(num1,"is greater")
else:
    print(num2,"is greater")'''

#Write a program to check whether a person is eligible to vote(age>=18)

'''age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")'''

#Write a program to check whether a given character is a vowel or consonant.

'''ch=input("Enter a character: ")
ch=ch.lower()
if ch in ('a','e','i','o','u'):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")'''

#Write a program to check if a number is divisible by 5.

'''num=int(input("Enter a number: "))
if num%5==0:
        print(num," is divisible by 5")
else:
    print(num," is not divisible by 5")'''

#Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.

'''num=int(input("Enter a number: "))
num = abs(num)
if num<10:
    print("It is a Single-digit number")
else:
    if num < 100:
        print("it is a two-digit number")
    else:
        print("it is more than two digit number")'''

#Write a program to check whether a student has passed or failed (passing marks = 40).

'''marks = int(input("Enter the marks: "))

if marks >= 40:
    print("Congratulations! You have Passed.")
else:
    print("Sorry! You have Failed.")'''


#Write a program to find whether the entered number is a multiple of both 3 and 7.
'''
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print(num, "is a multiple of both 3 and 7")
else:
    print(num, "is not a multiple of both 3 and 7")'''




''' **************************************** LADDER IF & NESTED IF ****************************'''

#1. Write a program to find the greatest among three numbers.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")'''
#2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).

'''age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child")
elif age >= 13 and age <= 19:
    print("You are a Teenager")
elif age >= 20 and age <= 59:
    print("You are an Adult")
else:
    print("You are a Senior")'''
#3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.

'''marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks <= 89:
    print("Grade: B")
elif marks >= 50 and marks <= 74:
    print("Grade: C")
elif marks >= 35 and marks <= 49:
    print("Grade: D")
else:
    print("Fail")'''

#4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.

'''a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("The triangle is Equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Scalene")
else:
    print("Not a valid triangle")'''

#5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.

'''ch = input("Enter a character: ")

if ch.isupper():
    print(ch, "is an Uppercase letter")
elif ch.islower():
    print(ch, "is a Lowercase letter")
elif ch.isdigit():
    print(ch, "is a Digit")
else:
    print(ch, "is a Special Symbol")'''

#6. Write a program to calculate electricity bill based on units: Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.
'''units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Your electricity bill is: ", bill)'''

#7. Write a program to determine the largest of four numbers using nested if.

'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    largest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    largest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    largest = num3
else:
    largest = num4

print("The largest number is:", largest)'''

#8. Write a program to check if a given year is a century year and also a leap year.

'''year = int(input("Enter a year: "))

if year % 100 == 0:
    print(year, "is a Century Year")
    if year % 400 == 0:
        print(year, "is also a Leap Year")
    else:
        print(year, "is not a Leap Year")
else:
    print(year, "is not a Century Year")
    if year % 4 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")'''
#9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).

'''weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")'''

#10. Write a program to display the smallest number among three using nested if.

'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

print("The smallest number is:", smallest)'''


'''********************************************FOR-LOOP QUESTION *************************************'''
#1. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).
'''for num in range(100, 1000):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == num:
        print(num)'''

#2. Write a program to generate and display the first n prime numbers using a for loop.
'''n = int(input("Enter how many prime numbers to generate: "))
count = 0
num = 2

while count < n:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1'''

#3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
'''for num in range(1, 501):
    if num % 3 == 0:
        sum_digits = sum(int(d) for d in str(num))
        if sum_digits <= 10:
            print(num, end=" ") '''

#4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:
'''n = int(input("Enter the height of the pyramid: "))

for i in range(1, n + 1):
    stars = 2 * i - 1
    print("*" * stars) '''

#5. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.

''' unable to solve this question '''

#7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
'''num = int(input("Enter a number: "))
sum_digits = sum(int(d) for d in str(num))

if num % sum_digits == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")'''
#8. Write a program to generate Pascal’s Triangle up to n rows using a for loop.
''' n = int(input("Enter number of rows: "))

for i in range(n):
    num = 1
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j) // (j+1)
    print()'''
#9. Write a program using a for loop to display the sum of the series: 12 + 22 + 32 + ... + n2
'''n = int(input("Enter n: "))
total = 0

for i in range(1, n+1):
    total += i**2

print("Sum of series:", total) '''
#10. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
''' unable to solve this question'''


'''************************************************************ WHILE LOOP ******************************************************************* '''
#While Loop Problems:
#11. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.
'''num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number is:", reverse)
is_prime = True
if reverse < 2:
    is_prime = False
else:
    i = 2
    while i <= reverse // 2:
        if reverse % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(reverse, "is a prime number")
else:
    print(reverse, "is not a prime number") '''
#12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
''' total_sum = 0

while total_sum <= 100:
    num = int(input("Enter a number: "))
    temp = num
    while temp > 0:
        total_sum += temp % 10
        temp //= 10

print("Sum of digits exceeded 100. Total sum:", total_sum)'''
#13. Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
'''num = input("Enter a number: ")

if num[0] == '0':
    print("Not a Duck number")
else:
    if '0' in num:
        print("It is a Duck number")
    else:
        print("Not a Duck number") '''
#14. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a
#happy number.
'''num = int(input("Enter a number: "))
seen = []

while num != 1 and num not in seen:
    seen.append(num)
    sum_sq = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_sq += digit ** 2
        temp //= 10
    num = sum_sq

if num == 1:
    print("It is a Happy number")
else:
    print("It is not a Happy number") '''
#15. Write a program using a while loop to find the largest prime factor of a given number.
''' num = int(input("Enter a number: "))
i = 2
largest = 0
temp = num

while temp > 1:
    if temp % i == 0:
        largest = i
        temp //= i
    else:
        i += 1

print("Largest prime factor of", num, "is", largest)'''
#16. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
''' while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome entered:", s)
        break
    else:
        print("Not a palindrome. Try again.")''' 
#17. Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
'''num = int(input("Enter a number: "))

while num > 9:
    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    num = sum_digits

print("Digital root is:", num) '''

#18. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).
'''num = int(input("Enter a number: "))

while num != 1:
    print(num, end=" -> ")
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
print("1") '''
#19. Write a program using a while loop to accept a number and check whether it is a Kaprekar number.(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.
#Example: 452=2025 => 20+25=45).
''' unable to solve this question '''


'''20. Write a program to simulate an ATM machine using a while loop where a user can:
• Check balance
• Deposit money
• Withdraw money (only if balance is sufficient)
• Exit
Continue until the user chooses to exit.'''



balance =20000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("Current balance: Rs", balance)
    elif choice == '2':
        amount = int(input("Enter amount to deposit: Rs"))
        balance += amount
        print("Amount deposited. New balance: Rs", balance)
    elif choice == '3':
        amount = int(input("Enter amount to withdraw: Rs"))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Amount withdrawn. New balance: Rs", balance)
    elif choice == '4':
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Try again.")


