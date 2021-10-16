
import string 

def Encrypt(string_text, int_key): 
  b = ""
  for value in range(len(string_text)):
        c = string_text[value] 
        if (c.isupper()): 
            b += chr((ord(c) + int_key-65) % 26 + 65) 
        if(c.islower()): 
            b += chr((ord(c) + int_key-97) % 26 + 97) 
        else:
            b += c
  return b

def Decrypt(string_text, int_key): 
  b = ""
  for value in range(len(string_text)):
        c = string_text[value] 
        if (c.isupper()): 
            b += chr((ord(c) - int_key-65) % 26 + 65) 
        if(c.islower()): 
            b += chr((ord(c) - int_key-97) % 26 + 97) 
        else:
            b += c
  return b


def Get_input():
  b = Print_menu()
  return b



def Print_menu():
  print("Main Menu")
  print("1) Encode a String")
  print("2) Decode a String")
  print("Q) Quit")
  a = input(print("Enter your selection ==>"))
  return a


  
def main(): 
  Again = True 
  while Again: 
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program: 
main() 
