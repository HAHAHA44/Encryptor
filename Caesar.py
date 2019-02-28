def doCaesar(plaintext):
    cipher = ''
    for i in plaintext:
        asc = ord(i)
        asc = asc + 3
        if asc >= ord('0') + 3 and asc <= ord('9') + 3:
            m = asc % ord('9')
            if m <= 3 and m != 0:
                asc = ord('0') + m-1
            cipher = cipher + chr(asc)
        elif asc >= ord('A') + 3 and asc <= ord('Z') + 3:
            m = asc % ord('Z')
            if m <= 3 and m != 0:
                asc = ord('A') + m-1
            cipher = cipher + chr(asc)            
        elif asc >= ord('a') + 3 and asc <= ord('z') + 3:
            m = asc % ord('z')
            if m <= 3 and m != 0:
                asc = ord('a') + m-1
            cipher = cipher + chr(asc)
        else:
            cipher = cipher + i
    return cipher