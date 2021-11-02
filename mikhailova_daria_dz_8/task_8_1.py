import re

RE_SOUP = re.compile(r'([A-Za-z0-9_-]+\.)*[A-Za-z0-9_-]+@[A-za-z0-9_-]+(\.[A-za-z0-9_-]+)*\.[A-za-z]{2,6}')


def email_parse(arg) -> dict:
    if RE_SOUP.match(arg):
        soup_list = arg.split('@')
        name = ['username', 'domain']
        return dict(zip(name, soup_list))
    else:
        raise ValueError(f' wrong email: {arg}')
