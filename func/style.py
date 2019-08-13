# -*- coding: utf-8 -*-

from sys import exit
from datetime import datetime


def fetchTime():
    now = datetime.now()
    dd = str(now.day)
    mm = str(now.month)
    yyyy = str(now.year)
    HH = str(now.hour)
    MM = str(now.minute)
    SS = str(now.second)
    return dd, mm, yyyy, HH, MM, SS


def fetchFormattedTime():
    now = fetchTime()
    now = now[0]+'.'+now[1]+'.'+now[2]+'│'+now[3]+':'+now[4]+':'+now[5]
    return now


def info(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '[\033[1m\033[36m*\033[0m] \033[94m'+str(text)+'\033[0m'
        else:
            text = text.split(' -> ')
            return '[\033[1m\033[36m*\033[0m] \033[94m' +\
                str(text[0])+': '+'\033[0m\033[36m\033[3m'+str(text[1]) +\
                '\033[0m'
    else:
        if len(text.split(' -> ')) != 2:
            return '[*] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[*] {}: {}'.format(text[0], text[1])


def warn(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return'[\033[1m\033[93m!\033[0m] \033[33m'+str(text)+'\033[0m'
        else:
            text = text.split(' -> ')
            return '[\033[1m\033[93m!\033[0m] \033[33m' +\
                str(text[0])+': '+'\033[0m\033[93m\033[3m'+str(text[1]) +\
                '\033[0m'
    else:
        if len(text.split(' -> ')) != 2:
            return '[!] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[!] {}: {}'.format(text[0], text[1])


def good(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '[\033[1m\033[92m+\033[0m] \033[32m'+str(text)+'\033[0m'
        else:
            text = text.split(' -> ')
            return '[\033[1m\033[92m+\033[0m] \033[32m' +\
                str(text[0])+': '+'\033[0m\033[92m\033[3m'+str(text[1]) +\
                '\033[0m'
    else:
        if len(text.split(' -> ')) != 2:
            return '[+] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[+] {}: {}'.format(text[0], text[1])


def bad(text, color=True):
    if color:
        if len(text.split(' -> ')) != 2:
            return '[\033[1m\033[91m-\033[0m] \033[31m'+str(text)+'\033[0m'
        else:
            text = text.split(' -> ')
            return '[\033[1m\033[91m-\033[0m] \033[31m' +\
                str(text[0])+': '+'\033[0m\033[91m\033[3m'+str(text[1]) +\
                '\033[0m'
    else:
        if len(text.split(' -> ')) != 2:
            return '[-] {}'.format(text)
        else:
            text = text.split(' -> ')
            return '[-] {}: {}'.format(text[0], text[1])


def cls():
    print('\033[H\033[J', end='')


def banner(version, author='naryal2580', color=True):
    print('\33]0;SéCh3r_{} by {}\a'.format(version, author), end='')
    if color:
        logo = '''
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/ {} {}  by --{}'''.format('\033[0m',
                                                    version,
                                                    '{}{}{}'.format('\033[1m',
                                                                    author,
                                                                    '\033[0m'))
        print('\033[1m'+logo[1:])
    else:
        logo = '''
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/  {}  by --{}'''.format(version, author)
        print(logo[1:])


def printTakenInput(value, prompt='Prompt', color=True):
    if color:
        x = '[\033[1m\033[95m<\033[0m] \033[95m{}:\033[0m\033[3m {}\033[0m'.\
          format(prompt, value)
    else:
        x = '[<] {}: {}'.format(prompt, value)
    print(x)


def coolInput(prompt='Prompt', color=True):
    try:
        if color:
            prompt = '[\033[1m\033[35m<\033[0m] \033[35m{}:\033[0m \033[3m'.\
                       format(prompt)
        else:
            prompt = '[<] {}: '.format(prompt)
        _input = input(prompt)
        if color:
            print('\033[0m', end='')
        return _input
    except KeyboardInterrupt:
        print('\b\bNull\033[0m')
        print(bad('Exitting, because recived an Interruption from Keyboard.'))
        coolExit(0)
    except EOFError:
        print('Null\033[0m')
        print(bad('Terminating via EOF, actually EOL.'))
        coolExit(0)


def coolExit(exitCode=0, color=True):
    now = fetchFormattedTime()
    print(info('Halted [at] {}'.format(now), color))
    exit(exitCode)
