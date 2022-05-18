from django.db.models import QuerySet, Q

from house.models import House


def _filter_houses_by_form(form_data: dict, filtered_houses: QuerySet[House]) -> QuerySet[House]:
    filtered_houses = filtered_houses.filter(public=True)
    for key, value in form_data.items():
        if value is not None and value != '':
            if 'profession' in key and form_data['parent_profession_1'] != form_data['parent_profession_2']:
                filtered_houses = filtered_houses.filter(Q(parent_profession_1=value) | Q(parent_profession_2=value))
            elif key == 'highest_income':
                filtered_houses = filtered_houses.filter(income__lte=value)
            elif key == 'lowest_income':
                filtered_houses = filtered_houses.filter(income__gte=value)
            else:
                filtered_houses = filtered_houses.filter(**{key: value})
    return filtered_houses
