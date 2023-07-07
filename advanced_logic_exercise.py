# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

int_list = []
for num in numbers:
    if (num % 2) == 0:
        int_list.append(num)
print(int_list)

# 2. Print the difference between the largest and smallest value:

mini = min(numbers)
maxi = max(numbers)
print(maxi-mini)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

def neighbour(numbers):
    length_check = len(numbers)
    for number in numbers:
        if number < length_check:
            if number == numbers[number+1] and number == 2:
                return True
    return False

print(neighbour(numbers))

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

def exclusive_sum(numbers):
    running_total = []
    counting_bool = True
    for number in numbers:
        if number == 6:
            counting_bool = False
        if counting_bool == True:
            running_total.append(number)
        if number == 7:
            counting_bool = True
    final_total = sum(running_total)
    return final_total


print(exclusive_sum(numbers))
# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

def unlucky_sum(numbers):
    unlucky = numbers.index(13)
    running_total = 0
    for number in numbers:
        if number != numbers[unlucky] and number != numbers[unlucky+1]:
            running_total += number
    return running_total


print(unlucky_sum(numbers))





