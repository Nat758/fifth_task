# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# file5 = open('file5.txt', 'w')
# ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
# file5.write(ex5)
# file5.close()


# def coding(txt):
#   count = 1
# res = ''
# for i in range(len(txt)-1):
#    if txt[i] == txt[i+1]:
#         count += 1
# else:
#    res = res + str(count) + txt[i]
#    count = 1
# if count > 1 or (txt[len(txt)-2] != txt[-1]):
#    res = res + str(count) + txt[-1]
# return res

# def decoding(txt):
#   num = ''
#   res = ''
# for i in range(len(txt)):
#  if not txt[i].isalpha():
#    num += txt[i]
# else:
#    res = res + txt[i] * int(num)
#    num = ''
# return res

# pol6 = open('file6.txt', 'w')
# coding (ex5)
# pol6.write(coding(ex5))

# print(coding(ex5))
# print(decoding(coding(ex5)))
# pol6.close()


def read_file(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readline()
    lines = [line.rstrip('\n') for line in lines]
    file.close()
    return lines
lines = read_file('encoded_text.txt')
print(lines)


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

encoded_val = rle_encode(lines)
print(encoded_val)

with open('encoded1_text.txt', 'w') as modified: modified.write(f"{encoded_val}\n")


lines = read_file('encoded1_text.txt')
print(lines)


def rle_decode(data1):
    decode = ''
    count = ''
    for char in data1:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoded_val = rle_decode(lines)
print(decoded_val)

with open('decoded_text.txt', 'w') as modified: modified.write(f"{decoded_val}\n")