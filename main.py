import requests


def main():
    locations = ('london', 'svo', 'Череповец')
    display_params = {
        'm': '',
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }

    url_template = 'https://wttr.in/{}'
    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=display_params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
