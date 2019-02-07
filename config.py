import os

class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_BASE_API_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey=89d86575840d4357be582bd2faf0f4ae'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=89d86575840d4357be582bd2faf0f4ae'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('HOMES')



class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
