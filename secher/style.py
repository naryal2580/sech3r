from stoyled import *

def banner(version, color=True):
    """Banner, just fanciness"""
    _banner = """
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/ """[1:]
    if color:
        print(f"{rst}{bold}{_banner}{rst}  v{version} by --{bold}naryal2580{rst}")
    else:
        print(f"{_banner}  v{version} by --naryal2580")


def prnHeads(headers, color=True, isVuln=True):
    """Printing Headers, with colors"""
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
