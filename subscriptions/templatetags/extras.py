from django import template
import requests
import bs4
register = template.Library()

@register.filter
def custom(l):
    paragraphs = []
    r = requests.get(l)
    r.raise_for_status()
    b = bs4.BeautifulSoup(r.text, 'html')
    p = []
    paragraphs.append(b.find_all('p'))
    for i in paragraphs:
        temp_ti = []
        for j in i:
            temp_ti.append(j.text)
        p.append(temp_ti)
    return temp_ti
