enc_pass = [0x52, 0x48, 0x4E, 0x56, 0x7, 55, 0x55, 0x10, 0x1A, 0x1A, 0x68, 0x55, 0x40, 0x50, 0x10, 0x1, 0x4F, 0x55, 0x14, 0x5A, 0x1A, 0x57, 0x46, 0x43, 0x45, 0x56, 0x1A, 0x48, 0x5F, 0x0F]
xor_key1 = "This is not the real password?"
xor_key2 = 0x55

decrypted_pass = ""
current_decrypted = 0
for i in range(len(enc_pass)):
    current_decrypted = (enc_pass[i] ^ ord(xor_key1[i])) ^ xor_key2
    decrypted_pass += chr(current_decrypted)

print(decrypted_pass)