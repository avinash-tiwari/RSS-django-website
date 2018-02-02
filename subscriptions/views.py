import bs4,requests
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from .models import Websites
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

    # -------------core functionality-----------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

# ---------------------main logic-----------------------------------------------------
        subs = Websites.objects.order_by('web_name')
        title = []
        ti = []
        link = []
        li = []
        # getting the xml file------------------
        for i in subs:
            r = requests.get(i.web_url)
            r.raise_for_status()
            b = bs4.BeautifulSoup(r.text, 'xml')
            ti.append(b.find_all('title'))
            li.append(b.find_all('link'))
        # ----------------------------------------
        # getting the title values----------------
        for i in ti:
            temp_ti = []
            for j in i:
                temp_ti.append(j.text)
            title.append(temp_ti)
        # -----------------------------------------
        # getting the link values----------------
        for i in li:
            temp_li = []
            for j in i:
                temp_li.append(j.text)
            link.append(temp_li)
        # -----------------------------------------
        d = {}
        for k in range(len(title)):
            i = 0
            while(i < len(title[k])):
                d[title[k][i]] = link[k][i + 1]
                i += 1
        s1 = list(map(len, title))
        s2 = list(map(len, link))
        context['dict'] = d
        context['subs'] = subs
        return context

class AboutPageView(TemplateView):
    template_name='about.html'

class FeedbackPageView(TemplateView):
    template_name='feedback.html'

class SignUp(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')    
    template_name='signup.html'


class AddCreateView(CreateView):
    fields = '__all__'
    model = Websites
    template_name = 'add.html'


class SubsListView(ListView):
    context_object_name = 'SubList'
    model = Websites
    template_name = 'list.html'


class SubsDeleteView(DeleteView):
    model = Websites
    success_url = reverse_lazy('app1:list')
    template_name = 'delete.html'
