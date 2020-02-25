#!/usr/bin/env python3

"""
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r <urls>... [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help           Display help, basically this screen.
    -V --version        Display version number.
    <urls>               Optional URL(s) input from the Command-Line.
    -v --verbose        Show verbose output.
    -s --searchForVuln  Open Default WebBrowser, Googling for Vulnerabilities.
    -r --noRedirects    Do not follow HTTP-redirects.
    -c --noColor        No Colours to be used for the Output.

Examples:
    sech3r demo.testfire.net
    sech3r demo.testfire.net -vs
    sech3r demo.testfire.net -vr
    sech3r demo.testfire.net -c
    sech3r -vsrc
"""

__author__ = "naryal2580"
__version__ = "4.0"

from secher import *
from docopt import docopt

def main(urls=[], verbose=False, color=True):
    if urls:
        print(takenInput(f"URL(s) separated with double <space> -> {'  '.join(urls)}", color))

    else:
        urls = coolInput('URL(s) separated with double <space>', color).split(' ')
    print(info(f'Started [at] {fetchFormatedTime()}  -> Now, Requesting', color), end='\n\n')

    for url in urls:
        if len(urls) > 1:
            print(info(f'Requesting -> {url}', color))
        url = validateUrl(url)
        if url.startswith('http://'):
            print(warn('Warning -> Crafting a non TLS request', color))
        heads = getHeaders(url)
        if heads:
            if verbose:
                print(info('Response Headers -> ', color))
                for head in heads:
                    print(f'{head}: {heads[head]}')
            secHeads = checkSecHeads(heads)
            secHeadsPresent = secHeads[0]
            secHeadsNotPresent = secHeads[1]
            infoHeads = checkInfoHeads(heads)
            vulnHeads = infoHeads[0]
            infoHeads = infoHeads[1]
            if secHeadsPresent:
                prnHeads(secHeadsPresent, color, False)
            if secHeadsNotPresent:
                prnHeads(secHeadsNotPresent, color)
            if vulnHeads:
                prnHeads(vulnHeads, color)
            if infoHeads:
                prnHeads(infoHeads, color, False)
            print()


if __name__ == "__main__":
    args = docopt(__doc__, version=__version__)
    color = True
    verbose = False
    if args['--noColor']:
        color = False
    if args['--verbose']:
        verbose = True
    if args['--searchForVuln']:
        print('works.')
    banner(__version__, color)
    if verbose:
        print(info('Verbosity -> Enabled', color))
        if color:
            print(info('Colorized Output -> Yeah'))
        else:
            print(info('Much fanciness -> Nope', False))
    if args['<urls>']:
        main(args['<urls>'], verbose, color)
    else:
        main([], verbose, color)

    coolExit(0, color)
