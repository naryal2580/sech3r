#!/usr/bin/env python3

"""
`    /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--output <filename>]
    sech3r <urls>... [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--output <filename>]
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--input <filename>] [--output <filename>]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help               Display help, basically this screen.
    -V --version            Display version number.
    <urls>                  Optional URL(s) input from the Command-Line.
    -v --verbose            Show verbose output.
    -s --searchForVuln      Open Default WebBrowser, Googling for Vulnerabilities.
    -r --noRedirects        Do not follow HTTP-redirects.
    -k --insecure           Bypass TLS/SSL verification.
    -c --noColor            No Colours to be used for the Output.
    -q --quiet              Silent Mode, nothing else not even colors.
    -i --input <filename>   Take URLs from a file, Single URL per line
    -o --output <filename>  Save output to a file, a JSON output of headers

Examples:
    sech3r demo.testfire.net
    sech3r demo.testfire.net -i in.json
    sech3r demo.testfire.net -vs -o out.json
    sech3r demo.testfire.net -vr
    sech3r demo.testfire.net -c
    sech3r demo.testfire.net -q
    sech3r -vsirc
"""


__author__ = "naryal2580"
__version__ = "4.8"


from secher import *


def main(urls=[], verbose=False, search4cves=False, noRedirects=False, insecure=False, color=True, quiet=False):
    """
    `main` Function of sech3r.

        Parameters:
            urls (list): List of URL strings
            verbose (bool): Is verbosity necessary
            search4cves (bool): Shall tool search for CVEs from disclosed version
            noRedirects (bool): Shall redirections occur, while requesting for headers
            insecure (bool): Ignore TLS/SSL warnings
            color (bool): Shall color be printed while function is running

        Returns:
            output (dict): Output from the function in a dictionary
    """
    output = {}
    if not quiet:
        if urls:
            print(takenInput(f"URL(s) separated with double <space> -> {'  '.join(urls)}", color))
        else:
            urls = coolInput('URL(s) separated with double <space>', color).split('  ')
        print(info(f'Started [at] {fetchFormatedTime()}  -> Now, Requesting', color), end='\n\n')

    if quiet and not urls:
        if __name__ == '__main__':
            banner(__version__, color)
            print(bad('Duh! -> Give some urls from argument.'))
            coolExit(1, color)
        else:
            print('ERROR: You forgot to pass urls (list)')

    for url in urls:
        if quiet:
            print(f'URL: {url}')
        else:
            if len(urls) > 1:
                print(info(f'Requesting -> {url}', color))

        url = schemizeUrl(url, color, quiet)

        if not quiet:
            if url.startswith('http'+'://'):
                print(warn('Warning -> Crafting a non-TLS request', color))
            if insecure and url.startswith('https://'):
                print(warn('Warning -> Bypassing TLS verification'))

        headers = getHeaders(url, noRedirects, insecure, color, quiet)

        if headers:
            if verbose:
                print(info('Response Headers -> below:', color))
                for header in headers:
                    print(takenInput(f'{header}: {headers[header]}', color))

            securityHeaders = checkSecurityHeaders(headers)
            securityHeadersPresent, securityHeadersNotPresent = securityHeaders
            informativeHeaders = checkInformativeHeaders(headers)
            vulnerableHeaders, informativeHeaders = informativeHeaders

            if securityHeadersPresent:
                printHeaders(securityHeadersPresent, color, False, quiet)

            if securityHeadersNotPresent:
                printHeaders(securityHeadersNotPresent, color, True, quiet)

            if vulnerableHeaders:
                if search4cves:
                    for vulnerableHeader in vulnerableHeaders:
                        google(f'{vulnerableHeaders[vulnerableHeader]} CVE')
                printHeaders(vulnerableHeaders, color, True, quiet)

            if informativeHeaders:
                printHeaders(informativeHeaders, color, False, quiet)

            output[url] = {
                            'Security Headers Present': securityHeadersPresent,
                            'Security Headers Not Present': securityHeadersNotPresent,
                            'Vulnerable Headers': vulnerableHeaders,
                            'Informative Headers': informativeHeaders
                        }
        else:
            output[url] = {}

        if quiet:
            if urls[-1] == url or urls[-1] == url.split('://')[1]:
                return output
        print()

    return output


def run():
    """
    Function to be executed whenever sech3r is supposed to be executed.
    Does command-line argument parsing, etc..
    """
    from docopt import docopt
    args = docopt(__doc__, version='SéCh3r v{}'.format(__version__))
    color = True
    verbose = search4cves = noRedirects = insecure = quiet = output_filename = input_filename = False
    if args['--noColor']:
        color = False
    if args['--verbose']:
        verbose = True
    if args['--searchForVuln']:
        search4cves = True
    if args['--noRedirects']:
        noRedirects = True
    if args['--insecure']:
        insecure = True
    if args['--quiet']:
        quiet = True
    if args['--input']:
        input_filename = args['--input']
    if args['--output']:
        output_filename = args['--output']

    if not quiet:
        banner(__version__, color)

    if verbose:
        if not quiet:
            print(info('Verbosity -> Enabled', color))
            if color:
                print(info('Colorized Output -> Yeah'))
            else:
                print(info('Much fanciness -> Nope', False))
            if search4cves:
                print(info('Google for CVEs -> Yup!', color))
            else:
                print(info('Interested in CVEs -> Nah', color))
            if noRedirects:
                print(info('Follow Redirects -> No', color))
            else:
                print(info('Do Follow redirects -> Sure', color))
            if insecure:
                print(info('Bypass TLS/SSL verification -> Yea', color))
            else:
                print(info('Ignore TLS/SSL warnings -> Noo!', color))
        else:
            banner(__version__, color)
            print(bad('Wait a minute! -> How can I be both quiet, and verbose?', color))
            coolExit(1, color)

    if args['<urls>']:
        output = main(args['<urls>'], verbose, search4cves, noRedirects, insecure, color, quiet)
    elif input_filename:
        if not quiet:
            print(info(f'Input file -> {input_filename}'))
        urls = read_url_from_file(input_filename)
        if urls:
            output = main(urls, verbose, search4cves, noRedirects, insecure, color, quiet)
        else:
            print(bad(f'Wait! -> File not found or the file is empty'))
            coolExit(1, color)
    else:
        output = main([], verbose, search4cves, noRedirects, insecure, color, quiet)

    if output_filename:
        if not quiet:
            print(info(f'Output File -> {output_filename}'))
        with open(output_filename, 'w') as output_file:
            from json import dump as _dump
            _dump(
                    output,
                    output_file,
                    indent=2
                )

    if not quiet:
        coolExit(0, color)
    exit(0)


if __name__ == "__main__":
    run()