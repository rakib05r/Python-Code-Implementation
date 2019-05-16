# Complexity n^2
# Author Md.Rokibul Islam
# Intern Engineer
# W3 Engineers Ltd.
number_array = []
print('Enter the Array Elements: ')
element_number = int(input())
for i in range(element_number):
    print('Enter ', i+1, ' Index Value:')
    val = int(input())
    number_array.append(val)
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
for i in range(element_number-1):
    min_number = number_array[i]
    location = i
    for j in range(i+1, element_number):
        if min_number > number_array[j]:
            min_number = number_array[j]
            location = j
    temp = number_array[i]
    number_array[i] = number_array[location]
    number_array[location] = temp
print('After Selection Sort:')
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
