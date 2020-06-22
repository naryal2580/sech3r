from stoyled import *

def banner(version, color=True):
    """
    Banner, just for fanciness
    
        Parameters:
            version (int): Version of SéCh3r
    """
    _banner = """
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/ """[1:]
    if color:
        print(f"{rst}{bold}{_banner}{rst}  v{version} by --{bold}naryal2580{rst}")
    else:
        print(f"{_banner}  v{version} by --naryal2580")


def printHeaders(headers, color=True, isVuln=True, quiet=False):
    """
    Printing headers with fanciness
    
        Parameters:
            headers (dict/list): Headers based on condition
            color (bool): Shall color be printed while function is running
            isVuln (bool): Are passed headers vulnerability
    """
    if not quiet:
        if isVuln:
            if type(headers) != list:
                for header in headers:
                    print(bad(f'{header} -> {headers[header]}', color))
            else:
                for header in headers:
                    print(bad(f'{header} -> Not Present', color))
        else:
            for header in headers:
                print(info(f'{header} -> {headers[header]}', color))
    else:
        if type(headers) != list:
            for header in headers:
                print(f'{header}: {headers[header]}')


del blink, blue, blue_l, cyan, cyan_l, dim, green, green_l, hidden, invert, italic, normal, purple, purple_l, red, red_l, strike, uline, white, white_l, yellow, yellow_l