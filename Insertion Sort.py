number_array = []
print('Enter the Array Elements: ')
element_number = int(input())
for i in range(element_number):
    print('Enter ', i+1, ' Index Value:')
    val = int(input())
    number_array.append(val)
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
for i in range(element_number):
    temp_number = number_array[i]
    j = i-1
    while temp_number < number_array[j] and j >= 0:
        number_array[j+1] = number_array[j]
        j = j-1
    number_array[j+1] = temp_number
print('After Insertion Sort:')
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
