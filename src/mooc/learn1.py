#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python程序设计实验课1
# 猜数字游戏

import random

guesses_count = 0
name = input('Hello ! what is your name? \n')

number = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

while guesses_count <= 6:
    guess = int(input("Take a guess: "))
    guesses_count += 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('Good job, {0}, you guessed my number in {1} guesses!, the number is {2}'.format(name, guesses_count, number))
else:
    print('Nope, The number I was thinking of was {0}'.format(number))

