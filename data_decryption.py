import base64

# Read the encrypted data from the file
with open("encrypted.txt", "r") as f:
  encrypted_data = f.read()

# Decrypt the data using base64 decoding
decrypted_data = base64.b64decode(encrypted_data).decode()

# Print the decrypted data to the console
print(decrypted_data)
