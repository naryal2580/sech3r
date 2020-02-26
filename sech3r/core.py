from re import compile as reCompile
from urllib.request import urlopen as request
from urllib.request import Request
from .style import *


def parseUrl(url):
    """Regex based URL parser"""
    pattern = (
               r'^'
               r'((?P<protocol>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = reCompile(pattern)
    matches = regex.match(url)
    matchesAsDict = matches.groupdict() if matches is not None else None
    return matchesAsDict


def validateUrl(url):
    """Validation if protocol is specified"""
    parsedUrl = parseUrl(url)
    if not parsedUrl['protocol']:
        url = 'http://' + url
    return url


def getHeaders(url):
    """Requests Headers of queried URL"""
    try:
        req = Request(
                        url,
                        data=None,
                        headers={'User-Agent': 'sech3r/4.2'}
                    )
        resp = request(req)
    except Exception as excptn:
        print(bad(str(excptn).replace(': ', ' -> ')))
        if 'HTTP Error' in str(excptn):
            resp = excptn
        else:
            return {}
    return dict(resp.headers)


def checkSecHeads(headers):
    """Checks if security headers present, or not"""
    headersPresent = {}
    headersNotPresent = []
    security_headers = [
                        'Referrer-Policy',
                        'X-XSS-Protection',
                        'Content-Security-Policy',
                        'X-Frame-Options',
                        'Strict-Transport-Security',
                        'X-Content-Type-Options',
                        'X-Permitted-Cross-Domain-Policies',
                        'Public-Key-Pins',
                        'Expect-CT',
                        'Feature-Policy',
                        'Report-To',
                        'NEL'
                       ]
    for security_header in security_headers:
        if security_header in headers:
            headersPresent[security_header] = headers[security_header]
        else:
            headersNotPresent.append(security_header)
    return headersPresent, headersNotPresent


def checkInfoHeads(headers, searchForVuln=False, color=True):
    """Checking for informative headers"""
    version_disclosure_headers = [
                                    'Server',
                                    'X-AspNet-Version',
                                    'X-Powered-By'
                                ]
    disclosedOnes = {}
    undisclosedOnes = {}
    for header in version_disclosure_headers:
        if header in headers.keys():
            if any(char.isdigit() for char in headers[header]):
                disclosedOnes[header] = headers[header]
            else:
                undisclosedOnes[header] = headers[header]
    return disclosedOnes, undisclosedOnes


