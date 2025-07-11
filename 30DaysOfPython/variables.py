#Day 2: 30 Days of python programming
first_name = 'ganu'
last_name = 'mhaske'
full_name = 'ganesh mhaske'
country = 'India'
city = 'Pune'
age = 32
year, is_married, is_true, is_light_on = 2025, True, True, False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married), type(is_light_on), type(is_light_on))

print(len(first_name))
print(len(last_name))

print(bool(len(first_name) >= len(last_name)))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one*num_two
print(product)
division = num_one/num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

import math
radius = 30
area_of_circle = math.pi * (radius ** 2)
print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

radius = input('Enter radius of circle: ')
area_of_circle = math.pi * (int(radius) ** 2)
print(area_of_circle)

