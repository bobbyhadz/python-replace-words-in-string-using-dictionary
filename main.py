# Replace words in a String using a Dictionary in Python

my_str = 'site | name'

my_dict = {
    'site': 'bobbyhadz.com',
    'name': 'borislav'
}


for key, value in my_dict.items():
    my_str = my_str.replace(key, value)

# 👇️ bobbyhadz.com | borislav
print(my_str)