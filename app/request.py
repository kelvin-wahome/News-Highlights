from app import app
import urllib.request,json
from .models import Source
from .models import Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        source_results = None

            #urllib opens and reads URLs
        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)
    return source_results

def process_sources(source_list):
    """
    Function that processes new list dictionary and turns them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news sources_list
    Returns:
        news_results: A list of news objects
    """
    news_results = []
    for source in source_list:
        id = source.get('id')
        print(id)
        name = source.get('name')
        print(name)
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            source_object = Source(id,
                                    name,
                                    description,
                                    url,
                                    category,
                                    country)
            news_results.append(source_object)
    return news_results
