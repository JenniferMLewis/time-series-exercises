import pandas as pd
import requests


def get_api(url):
    '''
    Takes a URL to pull,
    returns the response from the JSON API.
    '''
    response = requests.get(url)
    return(response.json())

def get_payload(url, payload, db_name):
    data = get_api(url)
    pages = data[payload]['max_page']
    page_url = url + '?page='
    sales = []
    for page in range(1,pages):
        endpoint = str(page)
        response = requests.get(
            page_url+endpoint).json()[payload][db_name]
        print(f'''Getting page {endpoint} of 183. 
        ''', end='')
        sales.extend(response)
        sales.to_csv(db_name + '.csv')
    return sales

def page(data, dict_key):
    '''
    Takes in response data variable and dictionary key for the data you want,
    Returns current page, max pages, and next page.
    '''
    current_page = data[dict_key]['page']
    max_page = data[dict_key]['max_page']
    next_page = data[dict_key]['next_page']
    print(f'Current Page: {current_page}')
    print(f'Max Pages: {max_page}')
    print(f'Next Page : {next_page}')