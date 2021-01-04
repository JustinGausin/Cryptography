import simpleaes

if __name__ == "__main__":
    #the key should be hexadecimal but here i just did ascii -> hexadecimal format. 
    key1 = "1a2b3c4d5e6f7g8h" #in hexadecimal 0x6162636465666768696a6b6c6d6f70710
    plaintext = "abcdefghijklmopq"  

    cipher = simpleaes.AES()
    encrypted_text = cipher.encrypt(key1, plaintext)
    print("Encrypting now..........Done\n")
    print("encrypted text is: ", simpleaes.list_to_hex(encrypted_text) )

    print('\ndecrpypting AES now.....')
    decrypted= simpleaes.AES()
    decry_text = decrypted.decrypt(key1, encrypted_text)
    print("decrypted text is: ", simpleaes.list_to_hex(decry_text))
    print("Does decrypted hex match plaintext in hex form?\n")
  