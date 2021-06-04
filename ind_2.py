#!/usr/bin/env python3
# -*- coding: utf-8 -*-from datetime import date
# Вывести количество слов или

if __name__ == '__main__':
    s = input('Введите предложение -->')

    word = s.split(' ')
    liters = ['или']
    n = 0

    for i in word:
        if i in liters:
            n += 1

    print('Кол-во слов "или":', n)
