logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
should_continue=True
while should_continue==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceasar(start_text,shift_amount,cipher_direction):
        end_text=""
        if cipher_direction== "decode":
                shift_amount *= -1
        for char in start_text:
         if char in alphabet:
            position=alphabet.index(char)
            new_position=position + shift_amount
            end_text += alphabet[new_position]
         else:
            end_text+=char
        print(f"The ceasar text is {end_text}")
    ceasar(start_text=text,shift_amount=shift,cipher_direction=direction)

    result=input("should continue or not?")
    if result=="no":
        should_continue=False
        print("Goodbye")
  


  #below is only for encryption
'''def  encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
       position =alphabet.index(letter)
       new_position=position+shift_amount
       new_letter=alphabet[new_position]
       cipher_text += new_letter
    print(f"The encrypted text is {cipher_text}")
encrypt(plain_text=text, shift_amount=shift)'''

#below is only for decryption
'''def  decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
       position =alphabet.index(letter)
       new_position=position-shift_amount
       new_letter=alphabet[new_position]
       plain_text += new_letter
    print(f"The decrypted text is {plain_text}")
decrypt(cipher_text=text, shift_amount=shift)'''