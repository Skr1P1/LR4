#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано предложение. Определить число букв о в нем.

if __name__ == '__main__':

    str = input('Введите предложение -->')

    liters = ['o', 'O', 'о', 'О']
    n = 0

    for i in str:
        if i in liters:
            n += 1

    print('Кол-во букв "о":', n)
