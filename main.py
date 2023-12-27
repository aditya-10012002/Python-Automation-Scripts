import webbrowser
import sys

# Add the search query in the command line to the url

include_search_results_from_sites = [
    'medium.com',
    'stackoverflow.com',
    'reddit.com',
    'geekforgeeks.org',
    'stackexchange.com'
]

# print('Arguments ',str(sys.argv))
def get_query():
    query = ''
    for i in range(1, len(sys.argv)):
        query += sys.argv[i] + '+'
    query = query[:-1] if query != '' else query
    return query

# https://www.google.com/search?q=how+to+code+%28site%3Amedium.com+OR+site%3Astackoverflow.com%29
# Format:
# ( - %28
# ) - %29
# : - %3A

def get_url():
    query = get_query()
    if query == '':
        print('Enter a valid search query bro!')
    else:
        url = 'https://www.google.com/search?q=' + query + '+%28'
        for site in include_search_results_from_sites:
            url += 'site%3A' + site + '+OR+'
        url = url[:-4] + '%29'
        webbrowser.open(url)
        
get_url()