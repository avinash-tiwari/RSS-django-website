import bs4,requests
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from .models import Websites,Feedback,SaveArticles,ReadArticles
from .forms import SubForm,FeedbackForm
# Create your views here.

def HomePageView(request):
    if request.user.username=="tiwari":
        f=Feedback.objects.filter(to_user='tiwari')
        return render(request,'home.html',{'msg':f})
    else:
        subs = Websites.objects.filter(app_user=str(request.user.username))
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
        # Getting the name of the subscription
        name=[]
        for i in range(len(title)):
            name.append(title[i].pop(0))
        # ------------------------------------
        # Creating the final Dictionary of the Subs Name and their content
        a={}
        for i in range(len(title)):
            de={}
            for j in range(len(title[i])):
                de[title[i][j]]=link[i][j+2]
            a[name[i]]=de
        # -----------------------------------------------------------------

        # Fixing the links with no rss links        
        for i,j in a.items():
            for t,l in j.items():
                if len(l)<3:
                    j[t]='no link'
        # -----------------------------------
    return render(request,'home.html',{'dict':a,'subs':subs})


class AboutPageView(TemplateView):
    template_name='about.html'

class FeedbackPageView(TemplateView):
    template_name='feedback.html'

def FeedbackPageView(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = request.POST['message']

            newObj = Feedback.objects.create(to_user="tiwari",from_user=str(
                request.user.username), message=message)
        return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

class SignUp(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')    
    template_name='signup.html'

def addSubs(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            web_name = request.POST['web_name']
            web_url = request.POST['web_url']

            newObj = Websites.objects.create(app_user=str(
                request.user.username), web_name=web_name, web_url=web_url)
        return redirect('home')
    else:
        form = SubForm()
    return render(request, 'add.html', {'form': form})


class SubsListView(ListView):
    context_object_name = 'SubList'
    model = Websites
    template_name = 'list.html'


class SubsDeleteView(DeleteView):
    model = Websites
    success_url = reverse_lazy('list')
    template_name = 'delete.html'

def ReaderModeView(request,l):
    if l=='no link':
        isRss=False
        temp_ti=[]
    else:
        isRss=True
        paragraphs=[]
        r = requests.get(l)
        r.raise_for_status()
        b = bs4.BeautifulSoup(r.text, 'html')
        p=[]
        paragraphs.append(b.find_all('p'))
        for i in paragraphs:
            temp_ti = []
            for j in i:
                temp_ti.append(j.text)
            p.append(temp_ti)
    return render(request,'reader.html',{'paras':temp_ti,'real':l,'isRss':isRss})
def SaveArticleView(request,l,n):
    b=SaveArticles.objects.create(app_user=str(request.user.username),article_link=l,article_title=n)
    return render(request,'saveconfirm.html')

def MarkAsReadView(request, l, n):
    b=ReadArticles.objects.create(app_user=str(request.user.username),article_link=l,article_title=n)
    data={'status':'success'}
    print('saved successfully')
    return JsonResponse(data)

def ReadPageView(request):
    b=ReadArticles.objects.filter(app_user=str(request.user.username))
    return render(request,'read.html',{'read':b})    

def SavePageView(request):
    b=SaveArticles.objects.filter(app_user=str(request.user.username))
    return render(request,'save.html',{'saved':b})    

def SaveRemove(request,l):
    b=SaveArticles.objects.filter(article_link=l).delete()
    return render(request,'removeConfirm.html')

def SaveRemove(request,l):
    b=ReadArticles.objects.filter(article_link=l).delete()
    return render(request,'remove_read.html')
