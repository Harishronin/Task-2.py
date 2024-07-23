
"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 1 : write a program to take even and odd numbers in the given list [10,501,22,37,100,999,87,351]
 """

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

evens = []
odds = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print("Even numbers :", evens)
print("Odd numbers :", odds)


"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 2 : write a program to count prime numbers in the given list [10,501,22,37,100,999,87,351] and create a new prime list
 """

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = []

for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

print(f"Count of prime numbers: {len(prime_numbers)}")
print(f"Prime numbers: {prime_numbers}")




"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 3 : write a program to find sum of first and last digit of an integer
 """

def sum_first_last_digits(number):
    num_str = str(number)  
    first_digit = int(num_str[0])  
    last_digit = int(num_str[-1])  
    return first_digit + last_digit

number = 12345
result = sum_first_last_digits(number)
print(f"The sum of the first and last digits of {number} is {result}")




"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 4 : write a program to find sum of first and last digit of an integer
 """

def find_duplicates(data_list):
    return list({item for item in data_list if data_list.count(item) > 1})

data_list_1 = [1, 2, 3, 7, 2, 1, 5, 6, 4, 8, 5]
data_list_2 = [1, 5, 5, 6, 7]
data_list_3 = [8, 8, 9, 9, 0, 1, 2, 3, 4]

duplicates_1 = find_duplicates(data_list_1)
duplicates_2 = find_duplicates(data_list_2)
duplicates_3 = find_duplicates(data_list_3)

print(f"Duplicates in data_list_1: {duplicates_1}")
print(f"Duplicates in data_list_2: {duplicates_2}")
print(f"Duplicates in data_list_3: {duplicates_3}")


"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 5 : write a program to find non repeating integers in the list
"""

data_list = [1, 2, 3, 1, 5, 6, 7, 8, 7]

counts = {item: data_list.count(item) for item in data_list}

non_repeating = [item for item, count in counts.items() if count == 1]

print(f"Non-repeating integers: {non_repeating}")



"""
 Name : Harish kumar
 Date : 21-july-2024
 Program 6 : write a program to find minimal element in a rated and sorted list 
"""
myNumList = [108, 65, 50, 82, 23]
myNumList.sort()
print(myNumList)

myList = [108, 65, 50, 82, 23]


# sorting in reverse
myList.sort(reverse=True)
print(myList)

