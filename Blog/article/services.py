from django.core import exceptions
from user.models import CustomUser
from category.models import Category
from django.core.exceptions import ObjectDoesNotExist

def get_author(author_id, field_name='author'):
    try:
        author = CustomUser.objects.get(pk=author_id)
        return author
    except ObjectDoesNotExist:
        pass

def get_category(category_id, field_name="category"):
    try:
        category = Category.objects.get(pk=category_id)
        return category
    except ObjectDoesNotExist:
        pass