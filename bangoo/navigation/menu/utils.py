from django.utils.text import slugify


def create_path(menu):
    roots = [u'/', menu.title]

    while True:
        menu = menu.parent
        if not menu:
            break

        roots.append(menu.title)
    roots.append(u'/')

    return u'/'.join(slugify(_) for _ in roots[::-1])