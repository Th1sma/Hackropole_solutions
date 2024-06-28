def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - ord('A')
            if char.islower():
                plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            key_index = (key_index + 1) % key_length
        else:
            plaintext += char
    return plaintext

ciphertext = "Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."
key = "FCSC"

decrypted_message = vigenere_decrypt(ciphertext, key)
print(decrypted_message)

#    Le code est adaptable pour tout les textes chiffrés avec la méthode vigenere
Test 