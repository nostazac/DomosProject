import binascii

def hex_string(string):
  """Converts a string to a hexadecimal string."""
  return binascii.hexlify(string.encode('utf-8')).decode('utf-8')

string = input("Enter your phrase: ")
hex_string = hex_string(string)

print(hex_string)
