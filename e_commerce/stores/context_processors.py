from e_commerce.stores.models import Category


def categories(request):
    return {"categories": Category.objects.all()}
