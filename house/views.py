from django.http import HttpResponse


def home_page(request):
    return HttpResponse("home page")


def global_page(request):
    filter_filled_1 = request.GET.get('filter_filled_1', '')
    filter_filled_2 = request.GET.get('filter_filled_2', '')
    return HttpResponse(
        f'this is the dashboard,' f' filter_filled_1={filter_filled_1},' f' filter_filled_2={filter_filled_2}'
    )


def house_login(request):
    return HttpResponse('house login')


def house_view(request, house_id):
    return HttpResponse(f'this is the house view for house {house_id}')


def add_house(request):
    post = request.POST["id"]
    return HttpResponse(f"try to update data for house POST PARAMETERS {'None' if post is None else post}")
