import socket
import string
import random

def spiralencry(encry0):
    c="XdX"
    encry0 = encry0.replace(' ',c )
    encry = ""
    for character in encry0:
        encry = encry + str(ord(character)) + random.choice(string.ascii_letters)
    leng= len(encry)
    list0 = []
    encode = ""
    for i in range(1, leng + 1):
        if leng % i == 0:
            list0.append(i)
    
    row = random.choice(list0)
    while( row == 0 or row == 1 or row == leng):
        row = random.choice(list0)
    coloum = int(leng/row)
    
    mat= [[0 for i in range(coloum)] for j in range(row)]
    top = 0
    bottom = row - 1
    left = 0
    right = coloum - 1
    index = 0
    
    while (True):
        
        if (top > bottom):
            break
        
        # prright column
        for i in range(top, bottom+1):
            mat[i][left] = int(ord(encry[index]) + i + left)
            index += 1
        left += 1
        
        if (left > right):
            break
        
        # prbottom row
        for i in range(left, right+1):
            mat[bottom][i] = int(ord(encry[index]) + bottom + i)
            index += 1
        bottom -= 1
        
        if (top > bottom):
            break
 
        # prleft column
        for i in range(bottom, top-1, -1):
            mat[i][right] = int(ord(encry[index]) + i + right)
            index += 1
        right -= 1
        
        if(left > right):
            break
        
        # prtop row
        for i in range(right, left-1 ,-1):
            mat[top][i] = int(ord(encry[index]) + top + i)
            index += 1
        top += 1
    for i in range(row):
        for j in range(coloum):
            encode = encode + str(mat[i][j]) + random.choice(string.ascii_letters)
    return(encode+" "+str(row)+ str(''.join(random.choices(string.ascii_uppercase, k=3))) +str(coloum))
    
def spiraldecry(decry):
    nkey = input("key ->")
    key = ""
    key0 = ""
    dig = ""
    dig0 = ""
    msg = decry.split(" ")
    decry = msg[0]
    okey = msg[1]
    
    if(okey == nkey):
        for i in nkey:
            if i.isdigit() == False:
                key = key + " "
            else:
                key = key + i
                
        k=key.split("  ")
        
        row = int(k[0])
        coloum = int(k[1])
        char = 0
        mat= [[0 for i in range(coloum)] for j in range(row)]
        for i in decry:
            if i.isdigit() == False:
                key0 = key0 + " "
            else:
                key0 = key0 + i
                
        la=key0.split(" ")
        for i in range(row):
            for j in range(coloum):
                mat[i][j]= la[char]
                char+=1
                
        top = 0
        bottom = row - 1
        left = 0
        right = coloum - 1
        index = 0
        decode = ""
        
        while (True):
            if (top > bottom):
                break

            # prright column
            for i in range(top, bottom+1):
                decode = decode + str(int(mat[i][left]) - i - left ) + random.choice(string.ascii_letters)
                index += 1
            left += 1
            
            if (left > right):
                break
            
            # prbottom row
            for i in range(left, right+1):
                decode = decode + str(int(mat[bottom][i])- bottom - i) + random.choice(string.ascii_letters)
                index += 1
            bottom -= 1
            
            if (top > bottom):
                break
            
            # prleft column
            for i in range(bottom, top-1, -1):
                decode = decode + str(int(mat[i][right]) - i - right) + random.choice(string.ascii_letters)
                index += 1
            right -= 1
            
            if(left > right):
                break
            # prtop row

            for i in range(right, left-1 ,-1):
                decode = decode + str(int(mat[top][i]) - top - i) + random.choice(string.ascii_letters)
                index += 1
            top += 1
        
        for i in decode:
            if i.isdigit() == False:
                dig = dig + " "
            else:
                dig = dig + i
        final = dig.split(" ")
        digit = ""

        for i in range(len(final)-1):
            digit = digit + chr(int(final[i]))
            
        for i in digit:
            if i.isdigit() == False:
                dig0 = dig0 + " "
            else:
                dig0 = dig0 + i
        
        final = dig0.split(" ")
        digit0 = ""
        for i in range(len(final)-1):
            digit0 = digit0 + chr(int(final[i]))
            
        decode = digit0.replace('XdX',' ')
        return decode
    else:
        return "worng key"


HOST = '127.0.0.1'
PORT = 3306
print("sender is ready to tranfer") 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        pWord = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))
        print("password is : " + pWord)
        data = conn.recv(1024).decode("utf-16")
        print('\nConnected successfully')
        message = input("\n -> ")
        if(message == "send"):
            #str0 = "I am trying to introduce new encryption algorithm98. In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string."
            str0 = input("->> ")
            if(data == pWord):
                print("\n"+data)
                print('\nConnected by', addr)
                print("\n"+str0)
                data = spiralencry(str0)
                msg = data.split(" ")
                password = msg[1]
                print("\n" + msg[0] + "\n" )
                print(password)
                conn.sendall(data.encode("utf-16"))
            else:
                data = "wrong"
                conn.sendall(data.encode("utf-16"))
