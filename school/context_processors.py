from . import models

def principal(request):
    return {"principal": models.PrincipalImage.objects.last()}