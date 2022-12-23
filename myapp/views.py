
import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import profile, vsession
from ngo.models import posts
from django.db.models import Count
# from .models import vsession
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.
flag = 0
def index(request):
    # print("you are entered into INDEX")
    # print("flag is: ",flag)
    # print("Value of username is: ",request.User.username)
    
    if (not (request.user.username)):
        # print("NO bro")
        return redirect('register')

    # if (request.user.username is not None):
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        context = {'profile': profiles}
        # print("YES bro")
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')
    # # return render(request, 'index.html')

def feed(request):
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        post = posts.objects.filter(edate__gt=today) 
        context = {'profile': profiles,
                   'posts': post,
                   }
        # print("YES bro")
        return render(request, 'pages/feed.html',context)
    else:
        return render(request, 'pages/feed.html')
    # return render(request, 'pages/feed.html')

def leaderboard(request):
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        context = {'profile': profiles}
        # print("YES bro")
        return render(request, 'pages/leaderboard.html',context)
    else:
        return render(request, 'pages/leaderboard.html')
    # return render(request,'pages/leaderboard.html')


today = datetime.date.today()


def profilepage(request):
        if (not (request.user.username)):
            return render(request, 'pages/profile.html')
        if (request.user.username):
            profiles = profile.objects.get(Email=request.user.username)
            co_vol = vsession.objects.filter(Email=profiles.Email).count()
            latest = list( vsession.objects.filter(Email=profiles.Email).order_by('vdate'))
            l1 = 0
            l2 = 0
            if latest:
                l1 = latest[-1].vdate
                l2 = latest[-1].vevent
            a = list( vsession.objects.filter(Email=profiles.Email,vdate__year=today.year,vdate__month=today.month))
            l_cnt = len(list( vsession.objects.filter(Email=profiles.Email,vdate__year=today.year,vdate__month=today.month,vslot='Lunch')))
            d_cnt = len(list( vsession.objects.filter(Email=profiles.Email,vdate__year=today.year,vdate__month=today.month,vslot='Dinner')))
            this_mon = len(a)
            result = (vsession.objects.filter(Email=profiles.Email,vdate__year=today.year,vdate__month=today.month).values('vevent').annotate(c=Count('vevent')).order_by())
            
            context = {'profile': profiles,
                       'num_vol':co_vol,
                       'l_date':l1,
                       'l_place':l2,
                       'curr_mon':this_mon,
                       'lun_n': l_cnt,
                       'din_n': d_cnt,
                       'area_n': result,
                    }
            
            return render(request, 'pages/profile.html',context)
        else:
            return render(request, 'pages/profile.html')

    


def loginpage(request):
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'signuppage.html')


def register(request):

    if request.method == 'POST':

        name1 = request.POST['name1']
        name2 = request.POST['name2']
        age = request.POST['age']
        pnumber = request.POST['pnumber']
        address = request.POST['address']
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User.objects.create_user(username = email, password = password2, email = email)
        user.save()
        user_model = profile(First_name=name1, Last_name=name2,Address=address, Age=age , Email= email ,Contact_no=pnumber, Password=password2).save()
        print("Before User Created")

        print("User Created")
        return redirect('login')

    else:
        return render(request, 'signuppage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            flag = 1
            # print("flag at login is: ",flag)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'loginpage.html')

def logout(request):
    auth.logout(request)
    flag = 0
    request.user.username = None
    print("username is: ",request.user.username)
    print("flag is: ",flag)
    return redirect('/')
    # return render(request, 'index.html')


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})


def session(request):
    if request.method == 'POST':

        date = request.POST['date']
        print("date is: ",date)
        area = request.POST['area']
        print("area is: ",area)
        slot = posts.objects.get(event_name = area)
        slot = slot.nslot
        print("slot is: ",slot)

    # d = datetime.date(1997, 10, 19)
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        context = {'profile': profiles}
    print("before time date saved")
    print("email is: ", profiles.Email)
    dateandtime = vsession(vdate=date,vslot=slot,vevent=area,Email=profiles.Email)
    dateandtime.save()
    print("after time date saved")
    return redirect('feed')


def pp_img(request):
    print("Before all")
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        context = {'profile': profiles}
    
    # print("img is: ",request.POST['imgfile'])
    # print("img is: ",request.FILES['imgfile'])

    # if request.POST['imgfile'] == "imgfile":
    #     print("BC")
    #     return redirect('profile')

    if request.method == 'POST':

        # if not request.FILES['imgfile']:
        #     print("hehe")
        #     return redirect('profile')

        # name1 = request.POST['name1']
        # name2 = request.POST['name2']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        pnumber = request.POST['pnumber']

        # pnumber = request.POST['pnumber']
        # address = request.POST['address']
        # email = request.POST['email']
        # username = request.POST['username']
        # password = request.POST['password']
        # password2 = request.POST['password2']

        profiles.Age=age
        profiles.Address=address
        profiles.Email=email
        profiles.Contact_no=pnumber
        profiles.save()
        # print("Before User Created")

    if request.method == 'POST' and request.FILES['imgfile']:
        myfile = request.FILES['imgfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        url = fs.url(filename)
        print("type of img: ",type(url))

        print("name is: ",profiles.First_name)
        print("img is: ",profiles.pp_img)
        profiles.pp_img=url
        profiles.save()


    print("After all")
    return redirect('profile')
