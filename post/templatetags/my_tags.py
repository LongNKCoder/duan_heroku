# <app>/templatetags/my_tags.py
from django import template
from django.utils import timezone
import math
register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()

@register.simple_tag
def chuyen_ngay(date):
    now = timezone.now()
    diff= now - date
    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        seconds= diff.seconds
        if seconds == 1:
            return str(seconds) +  " giây trước"
        else:
            return str(seconds) + " giây trước"

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        minutes= math.floor(diff.seconds/60)
        if minutes == 1:
            return str(minutes) + " phút trước"
        else:
            return str(minutes) + " phút trước"

    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        hours= math.floor(diff.seconds/3600)
        if hours == 1:
            return str(hours) + " giờ trước"
        else:
            return str(hours) + " giờ trước"

    # 1 day to 30 days
    if diff.days >= 1 and diff.days < 30:
        days= diff.days
        if days == 1:
            return str(days) + " ngày trước"
        else:
            return str(days) + " ngày trước"

    if diff.days >= 30 and diff.days < 365:
        months= math.floor(diff.days/30)
        if months == 1:
            return str(months) + " tháng trước"
        else:
            return str(months) + " tháng trước"

    if diff.days >= 365:
        years= math.floor(diff.days/365)
        if years == 1:
            return str(years) + " năm trước"
        else:
            return str(years) + " năm trước"