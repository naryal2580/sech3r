from webbrowser import open_new_tab as webrowser_openNewTab

def google(query):
    """Google a query, to default web browser"""
    url = f'https://google.com#q={query}'
    webrowser_openNewTab(url)
