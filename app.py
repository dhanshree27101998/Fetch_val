import os
# import subprocess
# from cryptography.fernet import Fernet
import requests

# Fetch environment variables
variable_value = os.getenv('TEST1')
# variable_value="Dhanshree"
print(f'The value of TEST1 is {variable_value}')

def get_request(url, headers=None, params=None):
    print("inside")
    """
    Sends a GET request to the specified URL with optional headers and parameters.

    :param url: The URL to send the GET request to.
    :param headers: A dictionary of headers to include in the request.
    :param params: A dictionary of query parameters to include in the request.
    :return: The response from the GET request.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        print(response)
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the response JSON if possible, else the text content
        try:
            return response.json()
        except ValueError:
            return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# Example usage
url = 'http://127.0.0.1:5000/api/data'
headers = {
    'Content-Type': 'application/json',
    'apiKey': variable_value
}
params = {
    'param1': 'value1',
    'param2': 'value2'
}

print("calling request")
response = get_request(url, headers=headers, params=params)
print(response)

# if os.getenv('TEST1')=="dhanshree":
#     testval=os.getenv('TEST1')
#     print("Val is correct")
#     print(f'testval is {testval}')
# else:
#     print("Val is not correct")    

# variable_value1 = os.getenv('USER')
# print(f'The value of USER is {variable_value1}')

# variable_value = os.getenv('TEST2')
# print(f'The value of TEST2 is {variable_value}')


# # Encryption key (generate and store securely)
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

# # Access the secret value
# my_secret = os.getenv('TEST1')

# # Encrypt the secret value
# encrypted_secret = cipher_suite.encrypt(my_secret.encode())

# # Print the encrypted secret value
# print(f"Encrypted secret value: {encrypted_secret}")

# # Decrypt the secret value
# decrypted_secret = cipher_suite.decrypt(encrypted_secret).decode()

# print(f"Decrypted secret value: {decrypted_secret}")


# # Run the printenv command
# result = subprocess.run(['printenv'], capture_output=True, text=True)
 
# # Print the output
# print(result.stdout)