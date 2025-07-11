'''
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)


print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool


first_name='ganesh'
last_name='mhaske'
country = 'Finland'
city = 'Helsinki'
age=20
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info={
    'first_name':'name1',
    'last_name':'lastname1',
    'country':'india',
    'city':'pune'
}


print('first name:', first_name)
print('First name length: ',len(first_name))
print('last name: ', last_name)
print('Last name length: ', len(last_name))
print('Skills are: ', skills)
print('Person Information: ', person_info)



first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name=input('Enter your first name: ')
age=input('Enter your age: ')
print(first_name)
print(age)



num_int = 10
print(float(num_int))

gravity = 9.81
print(int(gravity))


print(str(num_int))
'''

first_name = 'Asabeneh'
list_firstname=list(first_name)
print(list_firstname)