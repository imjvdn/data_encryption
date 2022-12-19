import base64

# Get user input
user_input = input("Enter the information you want to encrypt: ")

# Encrypt the input using base64 encoding
encrypted_input = base64.b64encode(user_input.encode())

# Store the encrypted input in a text file
with open("encrypted.txt", "w") as f:
  f.write(encrypted_input.decode())

print("Encrypted information saved to encrypted.txt")
