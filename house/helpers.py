from django.db.models import QuerySet

from house.models import House


def _filter_houses_by_form(form_data: dict, filtered_houses: QuerySet[House]) -> QuerySet[House]:
    for key, value in form_data.items():
        if value is not None and value != '':
            if key == 'country':
                filtered_houses = filtered_houses.filter(country=value)
            elif key == 'city':
                filtered_houses = filtered_houses.filter(city=value)
            elif key == 'parent_profession_1':
                filtered_houses = filtered_houses.filter(parent_profession_1=value)
            elif key == 'parent_profession_2':
                filtered_houses = filtered_houses.filter(parent_profession_2=value)
            elif key == 'highest_income':
                filtered_houses = filtered_houses.filter(income__lte=value)
            elif key == 'lowest_income':
                filtered_houses = filtered_houses.filter(income__gte=value)
            elif key == 'children':
                filtered_houses = filtered_houses.filter(children=value)

    return filtered_houses
