from naryal2580.style import rst, bold, purple_l, italic


def banner(version, author='naryal2580', color=True):
    print('\33]0;SéCh3r_{} by {}\a'.format(version, author), end='')
    if color:
        logo = '''
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/ {} {}  by --{}'''.format(rst,
                                                    version,
                                                    '{}{}{}'.format(bold,
                                                                    author,
                                                                    rst))
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
        x = '['+bold+purple_l+'<'+rst+']'+rst+' '+purple_l+prompt+':'+rst +\
              italic+' '+value+rst.format(prompt, value)
    else:
        x = '[<] {}: {}'.format(prompt, value)
    print(x)
