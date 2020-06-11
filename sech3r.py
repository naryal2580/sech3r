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
__version__ = "4.5"


from secher import *


def main(urls=[], verbose=False, search4cves=False, noRedirects=False, color=True):
    """
    `main` Function of sech3r.

        Parameters:
            urls (list): List of URL strings
            verbose (bool): Is verbosity necessary
            search4cves (bool): Shall tool search for CVEs from disclosed version
            noRedirects (bool): Shall redirections occur, while requesting for headers
            color (bool): Shall color be printed while function is running
        
        Returns:
            url (str): URL string after prepending or modifying scheme to http
    """
    if urls:
        print(takenInput(f"URL(s) separated with double <space> -> {'  '.join(urls)}", color))

    else:
        urls = coolInput('URL(s) separated with double <space>', color).split(' ')
    print(info(f'Started [at] {fetchFormatedTime()}  -> Now, Requesting', color), end='\n\n')

    for url in urls:
        if len(urls) > 1:
            print(info(f'Requesting -> {url}', color))
        url = validateUrl(url, color)
        if url.startswith('http://'):
            print(warn('Warning -> Crafting a non TLS request', color))
        heads = getHeaders(url, noRedirects, color)
        if heads:
            if verbose:
                print(info('Response Headers -> below:', color))
                for head in heads:
                    print(takenInput(f'{head}: {heads[head]}', color))
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
                if search4cves:
                    for vulnHead in vulnHeads:
                        google(f'{vulnHeads[vulnHead]} CVE')
                prnHeads(vulnHeads, color)
            if infoHeads:
                prnHeads(infoHeads, color, False)
            print()


def run():
    """
    `run` function of sech3r, function to be executed whenever sech3r is supposed to be executed. Does argument parsing, and controls exits too.
        
        Parameters:
            Nothing

        Returns:
            Nothing
    """
    from docopt import docopt
    args = docopt(__doc__, version='SéCh3r v{}'.format(__version__))
    color = True
    verbose = search4cves = noRedirects = False
    if args['--noColor']:
        color = False
    if args['--verbose']:
        verbose = True
    if args['--searchForVuln']:
        search4cves = True
    if args['--noRedirects']:
        noRedirects = True
    banner(__version__, color)
    if verbose:
        print(info('Verbosity -> Enabled', color))
        if color:
            print(info('Colorized Output -> Yeah'))
        else:
            print(info('Much fanciness -> Nope', False))
        if search4cves:
            print(info('Google for CVEs -> Yup!'))
        else:
            print(info('Interested in CVEs -> Nah'))
        if noRedirects:
            print(info('Follow Redirects -> No'))
        else:
            print(info('Do Follow redirects -> Sure'))

    if args['<urls>']:
        main(args['<urls>'], verbose, search4cves, noRedirects, color)
    else:
        main([], verbose, search4cves, noRedirects, color)

    coolExit(0, color)


if __name__ == "__main__":
    run()