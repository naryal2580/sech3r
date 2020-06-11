from stoyled import *

def banner(version, color=True):
    """
    Banner, just for fanciness
    
        Parameters:
            version (int): Version of SéCh3r
        
        Returns:
            None: Literally None object :p
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
    return None


def prnHeads(headers, color=True, isVuln=True):
    """
    Printing headers with fanciness
    
        Parameters:
            headers (dict/list): Headers based on condition
            color (bool): Shall color be printed while function is running
            isVuln (bool): Are passed headers vulnerability
        
        Returns:
            None: Literally None object :p
    """
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
    return None
