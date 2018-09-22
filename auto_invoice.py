import math

# print the name of the auto shop
print('Davy\'s auto shop services')

# make and print a list of automotive services
auto_services = {
        'Oil change': 35,
        'Tire rotation': 19,
        'Car wash': 7,
        'Car wax': 12,
}
print(f"Oil change -- ${auto_services['Oil change']}")
print(f"Tire rotation -- ${auto_services['Tire rotation']}")
print(f"Car wash -- ${auto_services['Car wash']}")
print(f"Car wax -- ${auto_services['Car wax']}")

# print a newline to satisfy whitespace requirements in zybooks
print()

# get the name of two auto service from the user and read it into a variable (entering a - should make the program not use that variable)
service_one = input('Select first service:\n')
service_two = input('Select second service:\n')

# print a newline to satisfy whitespace requrements in zybooks
print()

# calculate the total price for the invoice
if service_one in auto_services:
    price_one = f'${auto_services[service_one]}'
else:
    price_one = 'No service'
if service_two in auto_services:
    price_two = f'${auto_services[service_two]}'
else:
    price_two = 'No service'

if (price_one == 'no service') and (price_two == 'no service'):
    price_total = 0
elif price_one == 'No service':
    price_total = auto_services[service_two]
elif price_two == 'No service':
    price_total = auto_services[service_one]
else:
    price_total = auto_services[service_one] + auto_services[service_two]

# do some more calculating to make output cleaner
if price_one == 'No service':
    service_price_one = price_one
else:
    service_price_one = f"{service_one}, {price_one}"
if price_two == 'No service':
    service_price_two = price_two
else:
    service_price_two = f"{service_two}, {price_two}"

# print the invoice
print('Davy\'s auto shop invoice')
# print a newline for zybooks output detecting
print()
print(f"Service 1: {service_price_one}")
print(f"Service 2: {service_price_two}")
# print another newline for zybooks output detecting
print()
print(f"Total: ${price_total}")
