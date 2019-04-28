# Complexity O(n)
# Example:
# Enter the Array Elements:
# 5
# 45
# 55
# 23
# 34
# 21
# Index  1 : Value =  45
# Index  2 : Value =  55
# Index  3 : Value =  23
# Index  4 : Value =  34
# Index  5 : Value =  21
# Enter Your Search Value:23
# 23  Found At Position: 3

flag = 0
number_array = []
print('Enter the Array Elements: ')
element_number = int(input())
for i in range(element_number):
    print('Enter ', i+1, ' Index Value:')
    val = int(input())
    number_array.append(val)
for i in range(element_number):
    print('Index ', i+1, ': Value = ', (number_array[i]))
search_value = int(input('Enter Your Search Value:'))
for i in range(element_number):
    if search_value == number_array[i]:
        flag = 1
        position = i
        break
if flag == 1:
    print(search_value, ' Found At Position:', position+1)
else:
    print(search_value, 'Not Found')
input()
