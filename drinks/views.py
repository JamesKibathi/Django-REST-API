from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers

def drink_list(request):
    # get all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializers(drinks,many=True)
    # return json
    return JsonResponse({"Drinks":serializer.data},safe=False)