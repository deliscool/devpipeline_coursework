
def dec_to_hex ():
    hexa_table = ['0','1', '2','3','4','5','6','7','8','9','10','a','b','c','d','e']
    dec = int(input("Enter a number: "))
    hex_dec = ''

    while (dec>0):
        dec = dec // 16
        r = dec % 16
        [r]+ hex_dec
        hex_dec = hexa_table
    print ('Hexadecimal value: ', hex_dec)
        