import os
import subprocess

# Fetch environment variables
variable_value = os.getenv('TEST1')
print(f'The value of TEST1 is {variable_value}')

variable_value1 = os.getenv('USER')
print(f'The value of USER is {variable_value1}')

variable_value = os.getenv('TEST2')
print(f'The value of TEST2 is {variable_value}')

# Run the printenv command
result = subprocess.run(['printenv'], capture_output=True, text=True)
 
# Print the output
print(result.stdout)