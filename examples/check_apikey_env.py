import os


def check_apikey():
    api_key = os.getenv('ZAI_API_KEY')
    if api_key and api_key.strip():
        print('ZAI_API_KEY is set.')
        print(api_key)
    else:
        print('ZAI_API_KEY is NOT set. Please set the ZAI_API_KEY environment variable or configure it in the .env file.')


if __name__ == '__main__':
    check_apikey() 