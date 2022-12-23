from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import  ngo_profile, posts
from myapp.models import  vsession,profile

# Create your views here.
def profilepage(request):
            return redirect('/ngo')
def ngo_index(request):
    if (not (request.user.username)):
            return render(request, 'ngo_pages/ngo_register.html')
    if (request.user.username):
            profiles = ngo_profile.objects.get(Email=request.user.username)
            areas = list(profiles.areas)
            context = {'profile': profiles,
                       'area':areas
                       }
            
            return render(request, 'ngo_pages/ngo_profile.html',context)
    else:
            return render(request, 'ngo_pages/ngo_profile.html')

def vneeded(request):
    return render(request, 'ngo_pages/vol_need.html')

def vparticipated(request):
    profiles = ngo_profile.objects.get(Email=request.user.username)
    post_name = posts.objects.filter(name = profiles.ngo_name)
    context = {'post':post_name}
    
    # if request.method == 'POST':

    #     selection = request.POST['eventselect']
    #     vsess = vsession.objects.filter(vevent = selection)
    #     profiles = profile.objects.all()
    #     # n_name = ngo_profile.objects.
    #     # ngo_profiles = ngo_profile.objects.get(Email=request.user.username)
    #     #post_name = posts.objects.filter(name = ngo_profiles.ngo_name)
    #     context1 = {'sess':vsess,'profile':profiles,'post':post_name}
    #     return redirect('/ngo/participated_volunteers',context1)
    return render(request, 'ngo_pages/vol_part.html',context)

def ngo_session(request):
    if request.method == 'POST':

        selection = request.POST['eventselect']
        vsess = vsession.objects.filter(vevent = selection)
        vprofiles = profile.objects.all()
        profiles = ngo_profile.objects.get(Email=request.user.username)
        post_name = posts.objects.filter(name = profiles.ngo_name)
        # n_name = ngo_profile.objects.
        # ngo_profiles = ngo_profile.objects.get(Email=request.user.username)
        #post_name = posts.objects.filter(name = ngo_profiles.ngo_name)
        context1 = {'sess':vsess,'profile':vprofiles,'post':post_name}
        return render(request, 'ngo_pages/vol_part.html',context1)
        # return redirect('/ngo/participated_volunteers',context1)
    
    # return redirect('/ngo/participated_volunteers')
    return render(request, 'ngo_pages/vol_part.html')


    
def ngo_register(request):
    return render(request, 'ngo_pages/ngo_register.html')

def ngo_login(request):
    return render(request, 'ngo_pages/ngo_login.html')

def ngo_register_check(request):

    if request.method == 'POST':

        ngo_name = request.POST['ngo_name']
        o_name = request.POST['o_name']
        pnumber = request.POST['cno']
        a_head = request.POST['h_area']
        areas = request.POST.getlist('checks[]')
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        print("before")
        user = User.objects.create_user(username = email, password = password2, email = email)
        user.save()
        print("after")
        user_model = ngo_profile(ngo_name=ngo_name, owner_name=o_name,Contact_no=pnumber,area_head=a_head,areas=areas, Email= email ,Password=password2).save()
        print("Before User Created")

        print("User Created")
        return redirect('/ngo/login')

    else:
        return redirect('/ngo/register')

def ngo_login_check(request):
    if request.method == 'POST':
        username = request.POST['email']
        # email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            a = ngo_profile.objects.get(Email=username)
            au = a.authorized
            #context = {'ngo_profile': a}
            print(au)
            auth.login(request, user)
            if au == True:
                print("1")
                return redirect('/ngo')
            else:
                messages.info(request, 'NGO is not authorized yet')
                print("2")
                return redirect('/ngo/login')
                # return redirect(login)
        else:
            messages.info(request, 'Credentials Invalid')
            print("3")
            return redirect('/ngo/login')
    else:
        return render(request, 'ngo_pages/ngo_login.html')

def nvsession(request):
    if request.method == 'POST':

        event_name = request.POST['event_name']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        area = request.POST['area']
        slot = request.POST['slot']
        n_vol = request.POST['n_vol']
        info = request.POST['specifications']
        
        if (request.user.username):
            profiles = ngo_profile.objects.get(Email=request.user.username)
            name = profiles.ngo_name
            #context = {'profile': profiles}
        
        vol = posts(event_name=event_name, sdate=sdate, edate = edate, narea = area, nslot = slot, vneeded = n_vol, info = info, name = name).save()
        print("Post saved")

        
        return redirect('/ngo/vneeded')

    else:
        return redirect('/ngo/vneeded')