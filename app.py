import os

# Fetch environment variables
variable_value = os.getenv('TEST1')
print(f'The value of TEST1 is {variable_value}')

variable_value1 = os.getenv('USER')
print(f'The value of USER is {variable_value1}')
