import json


def run():
    file_path = input('Write the countries cities data json file path from root repo: ')
    file_path = './scripts/countries_cities_data.json' if file_path == '' else file_path

    with open(file_path, 'r') as json_file:
        data = json_file.read()
        pk_country = 0
        pk_city = 0
        data = json.loads(data)
        fixture = []
        for country in data:
            pk_country += 1

            fixture.append(
                {'fields': {'name': country['name']}, 'model': 'house.Country', 'pk': pk_country},
            )
            for city in country['cities']:
                pk_city += 1
                fixture.append(
                    {'fields': {'country': pk_country, 'name': city}, 'model': 'house.city', 'pk': pk_city},
                )

        with open('./house/fixtures/countries_cities.json', 'w') as json_file:
            json_file.write(json.dumps(fixture))
