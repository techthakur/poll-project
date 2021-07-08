from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout


from .forms import CreatePollForm
from .models import Poll

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1


        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/result.html', context)




















def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']




        # check user name
        if len(username)<1:
            messages.success(request,    ' Please fill the form ! Try Again ')
            return redirect('home')


        if len(username)>15:
            messages.success(request,    'Take Username is under 15 characters! Please Try Again ')
            return redirect('home')

        if len(username)<4:
            messages.success(request,    ' Your Username is to Smaller! Please Try Again ')
            return redirect('home')
            
        if not username.isalnum():
            messages.success(request,    ' Take Username Only letter or number ! Please Try Again ')
            return redirect('home')



        # check first name 
        if len(fname)>15:
            messages.success(request,    ' Your First name is to Long ! Please Try Again ')
            return redirect('home')
        

        if len(fname)<2:
            messages.success(request,    ' Your First name is to Smaller ! Please Try Again ')
            return redirect('home')
        

        


        # check Last Name
        if len(lname)>15:
            messages.success(request,    ' Your Last Name is to Long ! Please Try Again ')
            return redirect('home')
        

        if len(lname)<2:
            messages.success(request,    ' Your Last name is to Smaller ! Please Try Again ')
            return redirect('home')

        
        # check password
        if len(pass1)<4:
            messages.success(request,    ' Your Password is to week  ! Please Try Again ')
            return redirect('home')





        if pass1 != pass2:
            messages.success(request,    ' Your Password is does not  match ! Please Try Again ')
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, ' Your Account has been created successfully !')
        return redirect('home')

    
    else:

        return HttpResponse("  error  404 ")


    












def handlelogin(request):
    if request.method == "POST":
        loginuser = request.POST['loginuser']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginuser , password = loginpass)

        if len(loginuser)<1:
            messages.success(request, ' Please fill the form ! try again ')
            return redirect('home')


        if user is not None:
            login(request,user)
            messages.success(request, 'you are successfully logged in ')
            return redirect('home')

        else:
            messages.success(request, 'invalid username or password ! Please Try Again ')
            return redirect('home')

    return HttpResponse(" error  404 ")










def handlelogout(request):
    logout(request)
    messages.success(request, ' you are successfully logged out ')
    return redirect('home')

#return HttpResponse(" logout")                 # any body come direct logout page. not any problem. 
                                                # beacuse this logout page. so here will not used HttpResponse


  







