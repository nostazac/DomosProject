def convert_to_octal(string):
  """Converts a string to octal."""
  octal_string = ""
  for char in string:
    octal_string += oct(ord(char))[2:]
  return octal_string

# Example usage:
string = input("Enter password:")
octal_string = convert_to_octal(string)
print(octal_string)
