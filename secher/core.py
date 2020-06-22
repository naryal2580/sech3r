__version__ = "4.7"

from urllib import request as _request
from urllib.parse import urlparse as _urlparse
from ssl import _create_unverified_context
from .style import *


class _NoRedirects(_request.HTTPRedirectHandler):
    """
    Sub-class to handle HTTP Rediect, to be installed via opener on request object.
    """
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        pass



def schemizeUrl(url, color=True, quiet=False):
    """
    Returns url string after adding scheme if not present, and modofying scheme if not http.

        Parameters:
            url (str): URL string
            color (bool): Shall color be printed while function is running

        Returns:
            url (str): URL string after prepending or modifying scheme to http
    """
    parsedUrl = _urlparse(url)
    if not parsedUrl.scheme:
        url = 'http'+'://' + url
    elif parsedUrl.scheme not in ('http', 'https'):
        if not quiet:
            print(bad(f'Scheme `{parsedUrl.scheme}` does not looks like of `http`', color))
            print(info('Scheme modified to `http`', color))
        url = url.split('://')
        url[0] = 'http'
        url = '://'.join(url)
    return url


def getHeaders(url, noRedirects=False, insecure=False, color=True, quiet=False):
    """
    Returns HTTP Headers of a queried URL with a GET HTTP request.

        Parameters:
            url (str): URL string
            noRedirects (bool): Shall redirection be followed
            insecure (bool): Ignore TLS/SSL warnings
            color (bool): Shall color be printed while function is running

        Returns:
            headers (dict): HTTP Headers of a queried URL
    """
    try:
        if noRedirects:
            opener = _request.build_opener(_NoRedirects)
            _request.install_opener(opener)
        req = _request.Request(
                                url,
                                data=None,
                                headers={'User-Agent': f'sech3r/{__version__}'}
                            )
        if not insecure or url.startswith('http'+'://'):
            resp = _request.urlopen(req)
        else:
            resp = _request.urlopen(req, context=_create_unverified_context())
        if resp.url != url:
            if not quiet:
                if resp.url.startswith('https://'):
                    print(good(f'Redirected to -> {resp.url}', color))
                else:
                    print(info(f'Redirected to -> {resp.url}', color))
    except Exception as excptn:
        if not quiet:
            print(bad(str(excptn).replace(': ', ' -> '), color))
        else:
            print(f'ERROR: {excptn}')
        if 'HTTP Error' in str(excptn):
            resp = excptn
        else:
            return {}
    return dict(resp.headers)


def checkSecurityHeaders(headers):
    """
    Check for Security Headers.

        Parameters:
            headers (dict): HTTP Headers

        Returns:
            headersPresent (dict): HTTP security headers present with it's values
            headersNotPresent (list): HTTP security headers not present
    """
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


def checkInformativeHeaders(headers):
    """
    Check for Informative Headers, like version disclosure.

        Parameters:
            headers (dict): HTTP Headers

        Returns:
            disclosedOnes (dict): Informative HTTP headers with disclosed version
            undisclosedOnes (dict): Informative HTTP headers with version not disclosed
    """
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
