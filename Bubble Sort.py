# Worst-case performance	O( n^2 )
# Best-case performance	    O( n )
# Example
# Enter the Array Elements:
# 3
# Enter  1  Index Value:
# 2
# Enter  2  Index Value:
# 1
# Enter  3  Index Value:
# 3
# Index  1 : Value =  2
# Index  2 : Value =  1
# Index  3 : Value =  3
# After Ascending Order Bubble Sort:
# Index  1 : Value =  1
# Index  2 : Value =  2
# Index  3 : Value =  3
# After Descending order Bubble Sort:
# Index  1 : Value =  3
# Index  2 : Value =  2
# Index  3 : Value =  1


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
    for j in range(element_number-i-1):
        if number_array[j] > number_array[j+1]:
            temp = number_array[j]
            temp = int(temp)
            number_array[j] = number_array[j+1]
            number_array[j+1] = temp
print('After Ascending Order Bubble Sort:')
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
for i in range(element_number-1):
    for j in range(element_number-i-1):
        if number_array[j] < number_array[j+1]:
            temp = number_array[j]
            temp = int(temp)
            number_array[j] = number_array[j+1]
            number_array[j+1] = temp
print('After Descending order Bubble Sort:')
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
