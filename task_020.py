# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

name_fail = 'nam_1.txt'
name_fail_2 = 'nam_2.txt'
string_input = 'До чегоабв дошел прогресс абв. Было времени в обрезабв '

function.write_file(string_input, name_fail)
string_output = function.read_file(name_fail)
string_output = list(filter(lambda x: not 'абв' in x, string_output.split()))
string_output = ' '.join(string_output)
function.write_file(string_output, name_fail_2)