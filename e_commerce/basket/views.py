from django.shortcuts import render


def basket_summary(request):
    return render(request, "stores/basket/summary.html")
