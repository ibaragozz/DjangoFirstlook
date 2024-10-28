from django.shortcuts import render


def index(request):
    data = {
        'caption': 'DjangoTest'
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')


# def main_page(request):
#     return render(request, 'HW31/main_page.html')
#
# def first_breed(request):
#     return render(request, 'HW31/1st.html')
#
# def second_breed(request):
#     return render(request, 'HW31/2nd.html')
#
# def third_breed(request):
#     return render(request, 'HW31/3rd.html')
#
# def fourth_breed(request):
#     return render(request, 'HW31/4th.html')


