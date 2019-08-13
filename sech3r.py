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

__author__ = 'naryal2580'
__version__ = 'v3.0'

from func import banner, fetchFormattedTime, info, printTakenInput, coolInput,\
  getHTTPheaders, checkVersionDisclosure, checkSecurityHeaders, coolExit, bad
from docopt import docopt


def main(urls=[], verbose=False, searchForVuln=False,
         followRedirects=True, color=True):
    try:
        if urls:
            printTakenInput('  '.join(urls), 'URL', color)
        else:
            urls = coolInput('URL(s) separated with double <space>', color)
        for url in urls:
            headers = getHTTPheaders(url, color, verbose, followRedirects)
            checkVersionDisclosure(headers, searchForVuln, verbose, color)
            checkSecurityHeaders(headers, color)
    except KeyboardInterrupt:
        print('\b\b'+bad('Recieved SIGINT, terminating.', color))
        coolExit(0, color)
    except Exception as excptn:
        print(bad('Woops! Error -> {}'.format(excptn), color))
        coolExit(1, color)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='SéCh3r_{} by {}'.format(
                                                                  __version__,
                                                                  __author__
                                                                ))
    color = followRedirects = True
    verbose = searchForVuln = False
    if arguments['--verbose']:
        verbose = True
    if arguments['--noColor']:
        color = False
    if not arguments['--help']:
        banner(__version__, __author__, color)
        now = fetchFormattedTime()
        print(info('Started [at] {}'.format(now), color))
        if verbose:
            print(info('VerboseOutput -> True', color))
            if color:
                print(info('Color -> Enabled', color))
            else:
                print(info('Color -> Disabled', color))
    if arguments['--searchForVuln']:
        if verbose:
            print(info('Search For Known Vulnerability -> Yes', color))
            searchForVuln = True
    if arguments['--noRedirects']:
        if verbose:
            print(info('Redirects -> Do not follow', color))
        followRedirects = False

    if arguments['<urls>']:
        urls = arguments['<urls>']
        main(urls, verbose, searchForVuln,
             followRedirects, color)
    else:
        main([], verbose, searchForVuln, followRedirects, color)
    coolExit(0, color)
