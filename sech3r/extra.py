from webbrowser import open_new_tab as webrowser_openNewTab

def google(query):
    url = f'https://google.com#q={query}'
    webrowser_openNewTab(url)
