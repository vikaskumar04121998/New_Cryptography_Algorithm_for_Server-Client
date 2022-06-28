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


def client_program():
    host = '127.0.0.1'
    port = 3306
    print("receiver is ready to tranfer") 
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    message = input(" -> ")
    print("\nConnection successfully")
    client_socket.send(message.encode("utf-16"))
    massege = ""
    while True:    
        data = client_socket.recv(51200000)
        data = data.decode("utf-16")
        massege = massege + data
        if not data:
                break
    
    if(massege == "wrong"):
        print(massege)
    else:
        print(massege)
        decode = spiraldecry(massege)
        print('\nReceived from server: \n' + decode )
    client_socket.close()


if __name__ == '__main__':
    client_program()
