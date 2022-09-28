
from Products.models import Category

def header(request):
        cat=[]
        sub_cat=Category.objects.filter(category_p=None).order_by('title')
        for elm in sub_cat:
            cat.append(elm.catproductmodel.all())

        ctx = { 
        'sub_cats':sub_cat, 
        'cats':cat,  
        }
        return ctx


