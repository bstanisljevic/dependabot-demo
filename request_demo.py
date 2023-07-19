import requests

def get_url(url):
    response = requests.get(url)
    return response.content

def main():
    url = 'https://www.google.com'
    content = get_url(url)
    print(content)

if __name__ == '__main__':
    main()

