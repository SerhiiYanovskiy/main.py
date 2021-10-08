from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
import math

import this
from random import choice

# URL
# https://docs.python.org # /3/library/index.html path

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='asdf'
)

text = [x for x in dir(math) if not x.startswith('_')]
TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <div>
     {content}
    </div>
  </body>
</html>  
    """


def mod_handler(request, ):
    links = ['<a href ="{}">{}</a><br>'.format(name,name) for name in text]
    return HttpResponse(TEMPLATE.format(content=''.join(links)))

def obj_handler(request, mod_name, obj_name ):
    pass

urlpatterns = [
    path('', mod_handler ),
    path('<mod_name>/<obj_name>', obj_handler)
]


if __name__ == '__main__':
    execute_from_command_line()