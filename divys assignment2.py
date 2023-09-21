SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
number = 1
while number < len(SYMBOLS):
    mystr = ""
    for letter in message:
        index = SYMBOLS.index(letter)
        if index+number>65:
            remainder = index+number-66
            if remainder==0:
                mystr+=SYMBOLS[0]
            else:      
                mystr+=SYMBOLS[remainder]
        else:
            index+=number
            mystr+=(SYMBOLS[index])
    print(mystr)
    number+=1