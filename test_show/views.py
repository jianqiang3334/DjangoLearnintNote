from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello word")

import  datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"  % now
    return HttpResponse(html)
def hours_ahead(request, offset):
    # try:
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

from django.template import Template, Context
def modul_1(requst):
    raw_template = """<p>Dear {{ person_name }},</p>
    <p>Thanks for placing an order from {{ company }}. It's scheduled to
... ship on {{ ship_date|date:"F j, Y" }}.</p>
...
... {% if ordered_warranty %}
... <p>Your warranty information will be included in the packaging.</p>
... {% else %}
... <p>You didn't order a warranty, so you're on your own when
... the products inevitably stop working.</p>
... {% endif %}
...
... <p>Sincerely,<br />{{ company }}</p>"""
    t = Template(raw_template)
    c = Context({'person_name': 'John Smith','company': 'Outdoor Equipment','ship_date': datetime.date(2009, 4, 2),'ordered_warranty': False})
    tex=t.render(c)
    return HttpResponse(tex)


