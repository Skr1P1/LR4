#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Даны три слова. Напечатать неповторяющиеся в них буквы.

if __name__ == '__main__':
    s = input('Введите три слова -->')
    out_list = []

    for i in s:
        if i in out_list:
            out_list.remove(i)
        else:
            out_list.append(i)

    print(out_list)
