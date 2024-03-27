
from django.template import loader
from django.http import HttpResponse
from .models import Member
from django.shortcuts import render, redirect


"""def hhh(request):
   template= loader.get_template('mywife.html')
    return HttpResponse(template.render())"""

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'greetng':2,
  }
  return HttpResponse(template.render(context, request))

def test(request):
  mydata = Member.objects.all()
  template = loader.get_template('fetch.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
def userprofile(request):
    if request.method == 'POST':
        form = Member(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = Member()
    return render(request, 'user_profile.html', {'form': form})