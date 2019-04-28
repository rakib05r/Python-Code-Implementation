# Complexity O(log n)
# Enter the Array Elements:
# 5
# Enter  1  Index Value:
# 3
# Enter  2  Index Value:
# 1
# Enter  3  Index Value:
# 2
# Enter  4  Index Value:
# 5
# Enter  5  Index Value:
# 4
# After Sort The Array Elements:
# Index  1 : Value =  1
# Index  2 : Value =  2
# Index  3 : Value =  3
# Index  4 : Value =  4
# Index  5 : Value =  5
# Enter Your Search Value:3
# 3  Found At:  3
number_array = []
print('Enter the Array Elements: ')
element_number = int(input())
for i in range(element_number):
    print('Enter ', i+1, ' Index Value:')
    val = int(input())
    number_array.append(val)
number_array.sort()
print('After Sort The Array Elements:')
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
search_value = int(input('Enter Your Search Value:'))
first = 0
last = int(element_number-1)
middle = int((first+last)/2)
while first <= last:
    if number_array[middle]<search_value:
        first = int(middle+1)
    elif number_array[middle] == search_value:
        print(search_value, ' Found At: ', middle+1)
        break
    else:
        last = int(middle-1)
    middle = int((first+last)/2)
if first > last:
    print('Not Found')
input()
