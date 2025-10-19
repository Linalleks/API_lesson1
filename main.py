import requests


def main():
    locations_params = (
        (
            'san francisco',
            'San francisco (Сан Франциско)',
            {
                'u': '',
                'M': '',
                'n': '',
                'q': '',
                'T': '',
                'lang': 'en'
            }
        ),
        (
            'london',
            'London (Лондон)',
            {
                'm': '',
                'M': '',
                'n': '',
                'q': '',
                'T': '',
                'lang': 'en'
            },
        ),
        (
            'svo',
            'Аэропорт Шереметьево (Sheremetyevo Airport, код ICAO: SVO)',
            {
                'm': '',
                'M': '',
                'n': '',
                'q': '',
                'T': '',
                'lang': 'ru'
            },
        ),
        (
            'Череповец',
            'Череповец (Cherepovets)',
            {
                'm': '',
                'M': '',
                'n': '',
                'q': '',
                'T': '',
                'lang': 'ru'
            },
        )
    )

    print('Номер : Локация офиса')

    for location in locations_params:
        print(f'    {locations_params.index(location)} : {location[1]}')

    id_location = int(input('\nУкажите номер локации вашего офиса: '))
    url_template = 'https://wttr.in/{}'
    url = url_template.format(locations_params[id_location][0])
    response = requests.get(url, params=locations_params[id_location][2])
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
