
bin_str = str(input('Enter a binary: '))

def bin_inverse(bin_str):
    inverse_value = ''
    for num in bin_str:
        if num == '0':
            inverse_value += '1'
        else:
            inverse_value += '0'
          
    print(f'You binary inverse value is: {inverse_value}')

bin_inverse(bin_str)