from re import compile as reCompile
from socket import socket
import ssl
from http_parser.http import HttpStream as httpStream
from http_parser.reader import SocketReader as socketReader
from string import digits
from .style import info, warn, good, bad
from webbrowser import open_new_tab as openNewTab_ofWebBrowser


def parseUrl(url):
    pattern = (r'^'
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


def preRequest(url, color=True):
    parsedURL = parseUrl(url)
    protocol = parsedURL['protocol']
    if not protocol:
        protocol = 'http'
    if parsedURL['user'] or parsedURL['password']:
        print(warn('No creds. support, yet.', color))
    host = parsedURL['host']
    port = parsedURL['port']
    if not port:
        if protocol == 'https':
            port = '443'
        else:
            port = '80'
    path = parsedURL['path']
    if not path:
        path = '/'
    query = ''
    if parsedURL['query']:
        query += parsedURL['query']
    return protocol, host, port, path, query


def getHTTPheaders(url, color=True, verbose=False, redirect=True):
    protocol, host, port, path, query = preRequest(url, color)
    if int(port) in (80, 443):
        print(info('Requesting to -> {}://{}{}'.format(protocol,
                                                       host,
                                                       path+query), color))
    else:
        print(info('Requesting to -> {}://{}:{}'.format(protocol,
                                                        host,
                                                        port+path+query),
                   color))
    sock = socket()
    sock.connect((host, int(port)))
    request = 'GET {}{} HTTP/1.1\r\n'.format(path, query)
    if int(port) in (80, 443):
        request += 'Host: {}'.format(host)
    else:
        request += 'Host: {}:{}'.format(host, port)
    request += "\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67."
    request += "0)' Gecko/20100101 Firefox/67.0"
    request += '''\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
Pragma: no-cache\r
Cache-Control: no-cache\r\n\r\n'''
    if verbose:
        print(info('Requesting Headers -> \n{}\n'.format(request.strip()),
                   color))
    request = request.encode()
    if protocol == 'https':
        sock = ssl.wrap_socket(
                               sock,
                               keyfile=None,
                               certfile=None,
                               server_side=False,
                               cert_reqs=ssl.CERT_NONE,
                               ssl_version=ssl.PROTOCOL_TLSv1_2
                               )
    else:
        print(warn('Non-HTTPS request -> Someone else can interact.', color))
    sock.send(request)
    response = socketReader(sock)
    parsedResponse = httpStream(response)
    headers = parsedResponse.headers()
    if verbose:
        recvdHdrs = 'Recieved Headers -> \n'
        for header in headers:
            recvdHdrs += '{}: {}\n'.format(header, headers[header])
        print(info(recvdHdrs, color))
    if redirect:
        if 'location' in headers:
            if verbose:
                print(info('Redirecting to -> {}'.format(headers['location']),
                           color))
            rprotocol, rhost, rport, rpath, rquery = preRequest(
                                                          headers['location'],
                                                          color
                                                          )
            if rhost:
                if int(rport) in (80, 443):
                    rurl = '{}://{}{}'.format(rprotocol,
                                              rhost,
                                              rpath+rquery)
                else:
                    rurl = '{}://{}:{}'.format(rprotocol,
                                               rhost,
                                               rport+rpath+rquery)
            else:
                if rport:
                    if int(rport) in (80, 443):
                        rurl = '{}://{}{}'.format(rprotocol,
                                                  host,
                                                  rpath+rquery)
                    else:
                        rurl = '{}://{}:{}'.format(rprotocol,
                                                   host,
                                                   rport+rpath+rquery)
                else:
                    if int(port) in (80, 443):
                        rurl = '{}://{}{}'.format(rprotocol,
                                                  host,
                                                  rpath+rquery)
                    else:
                        rurl = '{}://{}:{}'.format(rprotocol,
                                                   host,
                                                   port+rpath+rquery)
            headers = getHTTPheaders(rurl, color, verbose)
    return headers


def checkSecurityHeaders(headers, color=True):
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
            print(good('{} -> {}'.format(security_header,
                                         headers[security_header]), color))
        else:
            print(bad('{} -> Not Present!'.format(security_header), color))


def checkVersionDisclosure(headers, searchForVuln=False,
                           verbose=False, color=True):
    version_disclosure_headers = ['Server', 'X-AspNet-Version']
    for header in version_disclosure_headers:
        header = header
        if header in headers:
            for digit in digits:
                if digit in headers[header]:
                    print(bad('Version Disclosure Present -> {}'.format(
                                                            headers[header]
                                                                    ), color))
                    if searchForVuln:
                        if verbose:
                            print(info('Googling -> Yeah!', color))
                        url = 'http://google.com/#q=' + headers[header] +\
                            ' site:cvedetails.com'
                        openNewTab_ofWebBrowser(url)
                    break
                else:
                    continue
    if 'X-Powered-By' in headers:
        print(bad('Version Disclosure Present -> {}'.format(
                                                     headers['X-Powered-By']
                                                            ), color))
