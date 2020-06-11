from webbrowser import open_new_tab as webrowser_openNewTab

def google(query):
    """
    Google for a query in a default web browser.
    
        Parameters:
            query (str): Query to be googled
        
        Returns:
            None: Literally None object :p
    """
    url = f'https://google.com#q={query}'
    webrowser_openNewTab(url)
    return None
