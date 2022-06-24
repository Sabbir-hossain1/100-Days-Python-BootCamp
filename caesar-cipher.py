end_of_program = False
encodedtext = ""
decoded_text = ""

while not end_of_program:
    encodingType = input("Type 'encode' to encript, type 'decode' to decrypt:  ").lower()           
    if encodingType == 'encode':
        message = input("Enter your message: ")
        shift_amount = int(input("type shift amount: "))
        for index in range(0,len(message)):
            encodedtext += chr(ord(message[index])+shift_amount)
    elif encodingType == 'decode':
        for index in range(0,len(message)):
            decoded_text += chr(ord(message[index])-shift_amount)
    print(message)
    print(encodedtext)
    print(decoded_text)
    
        
    if input("Type 'yes' to go again. Otherwise type 'no' ") == "yes":
        end_of_program = False
    else:
        end_of_program = True
    
