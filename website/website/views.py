from django.views import generic
from django.shortcuts import render


class HomePageView(generic.ListView):
    template_name = 'home_page/index.html'
    context_object_name = 'none'

    def get_queryset(self):
        """get home page"""

        return


def home_page(request):
    current_path = request.get_raw_uri()
    print(current_path)
    admin_path = current_path + 'admin'
    finance_path = current_path + 'finance'
    data = {
        'admin_path': admin_path,
        'finance_path': finance_path,
    }
    return render(request, 'home_page/index.html', data)
