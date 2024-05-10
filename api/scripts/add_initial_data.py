from products.models import *
from main.models import *


def run():
    Container.objects.get_or_create(name="szklanka", capacity=250)

    Setting.objects.get_or_create(
        name="dark_mode", value=False, category="general")
    Setting.objects.get_or_create(
        name="sort_by", value="id", category="browser")
    Setting.objects.get_or_create(
        name="sort_direction", value="asc", category="browser")
    Setting.objects.get_or_create(
        name="hide_columns", value=[], category="browser")
    Setting.objects.get_or_create(
        name="hide_status", value=[], category="browser")
