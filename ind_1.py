#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано предложение. Определить число букв о в нем.

if __name__ == '__main__':

    str = input('Введите предложение -->')

    liters = ['o', 'O', 'о', 'О']
    out_lst = []

    for i in str:
        if i in liters:
            out_lst.append(i)

    print('Кол-во букв "о":', len(out_lst))
