from webbrowser import open_new_tab as _open_new_tab

def google(query):
    """
    Google for a query in a default web browser.

        Parameters:
            query (str): Query to be googled
    """
    url = f'https://google.com#q={query}'
    _open_new_tab(url)
