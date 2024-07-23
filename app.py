import os
import subprocess
from cryptography.fernet import Fernet

# Fetch environment variables
variable_value = os.getenv('TEST1')
print(f'The value of TEST1 is {variable_value}')

if os.getenv('TEST1')=="dhanshree":
    testval=os.getenv('TEST1')
    print("Val is correct")
    print(f'testval is {testval}')
else:
    print("Val is not correct")    

variable_value1 = os.getenv('USER')
print(f'The value of USER is {variable_value1}')

variable_value = os.getenv('TEST2')
print(f'The value of TEST2 is {variable_value}')


# Encryption key (generate and store securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Access the secret value
my_secret = os.getenv('TEST1')

# Encrypt the secret value
encrypted_secret = cipher_suite.encrypt(my_secret.encode())

# Print the encrypted secret value
print(f"Encrypted secret value: {encrypted_secret}")

# Decrypt the secret value
decrypted_secret = cipher_suite.decrypt(encrypted_secret).decode()

print(f"Decrypted secret value: {decrypted_secret}")


# # Run the printenv command
# result = subprocess.run(['printenv'], capture_output=True, text=True)
 
# # Print the output
# print(result.stdout)