def encrypt(password):
    encPassword = ""
    for i in range(len(password)):
        num = str((ord(password[i])*5) % 17 + 65 + i*2) + "#"
        encPassword += num
    if(len(encPassword) >= 16):
        encPassword = encPassword[0:15]
    return(encPassword[:-1])
