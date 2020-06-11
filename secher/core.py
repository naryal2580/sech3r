from re import compile as reCompile
from urllib import request
from urllib.parse import urlparse
from .style import *


class NoRedirects(request.HTTPRedirectHandler):
    """Class to handle HTTP Rediect"""
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None



def validateUrl(url, color=True):
    """Validation if protocol is specified, prepend if not"""
    parsedUrl = urlparse(url)
    if not parsedUrl.scheme:
        url = 'http://' + url
    elif parsedUrl.scheme not in ('http', 'https'):
        print(bad(f'Scheme `{parsedUrl.scheme}` does not looks like of `http`', color))
        print(info('Scheme modified to `http`', color))
        url = url.split('://')
        url[0] = 'http'
        url = '://'.join(url)
    return url


def getHeaders(url, noRedirects=False, color=True):
    """Requests Headers of queried URL"""
    try:
        if noRedirects:
            opener = request.build_opener(NoRedirects)
            request.install_opener(opener)
        req = request.Request(
                                url,
                                data=None,
                                headers={'User-Agent': 'sech3r/4.2'}
                            )
        resp = request.urlopen(req)
        if resp.url != url:
            if resp.url.startswith('https://'):
                print(good(f'Redirected to -> {resp.url}', color))
            else:
                print(info(f'Redirected to -> {resp.url}', color))
    except Exception as excptn:
        print(bad(str(excptn).replace(': ', ' -> '), color))
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
    """Checks for informative headers"""
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


