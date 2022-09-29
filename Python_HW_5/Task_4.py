# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

RLE_1_decod = open('RLE_1_decod.txt', 'w')
text = 'HHHHHHHhhhhhhhEEeeeEEEELLlllllllllooOOOOOooo!!!!!!!!'
RLE_1_decod.write(text)
RLE_1_decod.close()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

RLE_2_encod = open ('RLE_2_encod.txt', 'w') 
encode_rle(text)
RLE_2_encod.write(encode_rle(text))

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

print(encode_rle(text))
print(decoding_rle(encode_rle(text)))
RLE_2_encod.close()
