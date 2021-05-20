s = input('Введите предложение -->')

word = s.split(' ')
liters = ['или']
out_lst = []

for i in word:
    if i in liters:
        out_lst.append(i)

    print(i)
print('Кол-во слов "или":', len(out_lst))
