# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы и заранее известно какой алфавит надо использовать.

s = input('Введите слово: ').upper()

dict = {'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3, 'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' : 10}
dict1 = {'АВЕИНОРСТ' : 1, 'ДКЛМПУ' : 2, 'БГЁЬЯ' : 3, 'ЙЫ' : 4, 'ЖЗХЦЧ' : 5, 'ШЭЮ' : 8, 'ФЩь' : 10}
summ = 0
for i in s:
    for key, val in dict.items():
            if i in key:
                summ += val

for i in s:
    for key, val in dict1.items():
            if i in key:
                summ += val
print(summ)

