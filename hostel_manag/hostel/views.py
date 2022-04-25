from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from hostel.models import contactUs,VisitorDetails,studentDetails
from django.contrib.auth import authenticate,login
from django.contrib import messages

def saveContactDetails(request):
    if request.method=='POST':
      name=  request.POST.get('name')
      email=  request.POST.get('email')
      message=  request.POST.get('message')
      contact=contactUs(name=name,email_id=email,message=message)
      contact.save()
    return render(request,'hostel/homepage.html')

def saveVisitorDetails(request):
    if request.method=='POST':
      fname=  request.POST.get('fname')
      lname=  request.POST.get('lname')
      email=  request.POST.get('email')
      room=  request.POST.get('room')
      phone=  request.POST.get('phone')
      intime=  request.POST.get('intime')
      outtime=  request.POST.get('outtime')
      relation=  request.POST.get('relation')
      visitor=VisitorDetails(fname=fname,email=email,lname=lname,room=room,phone=phone,intime=intime,outtime=outtime,relation=relation)
      visitor.save()
    return render(request,'hostel/visitor.html')

def login_user(request):
    if request.method=='POST':
        username=  request.POST.get('username')
        password=  request.POST.get('password')
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            # if user.is_active:
            return redirect('home-page')
        else:
            messages.error(request, f'Invalid Login Credentials')
            return redirect('login-page')

    return render(request,'hostel/login.html')




def home(request):
    return render(request,'hostel/homepage.html')
def aboutUs(request):
    return render(request,'hostel/about_us.html')

# def createUser(request):
#     if request.method == 'POST':
#             username = request.POST('uname')
#             password=request.POST('password')
#             p = User(uname=username,password=password)
#             p.save()

#     return render(request,'hostel/login.html')
    
def saveStudentDetails(request):
    if request.method =='POST':
        sname=request.POST.get('fname')
        pname=request.POST.get('lname')
        dob=request.POST.get('dob')
        address=request.POST.get('mob')
        snumber=request.POST.get('mob1')
        pnumber=request.POST.get('mob2')
        semail=request.POST.get('email1')
        pemail=request.POST.get('email2')
        hcity=request.POST.get('hometown')
        state=request.POST.get('state')
        caste=request.POST.get('caste')
        nation=request.POST.get('nation')
        aadhar=request.POST.get('aadhar')
        pan=request.POST.get('pan')
        blood=request.POST.get('blood')
        allergy=request.POST.get('allergy')
        guard=request.POST.get('guard')
        gaddress=request.POST.get('gaddress')
        gnumber=request.POST.get('gnumber')
        sphoto=request.POST.get('sphoto')
        aphoto=request.POST.get('aphoto')
        svaccine=request.POST.get('svaccine')
        certi=request.POST.get('certi')
        student=studentDetails(fname=sname,lname=pname,dob=dob,mob=address,mob1=snumber,mob2=pnumber,email1=semail,email2=pemail,hometown=hcity,state=state,caste=caste,nation=nation,aadhar=aadhar,pan=pan,blood=blood,allergy=allergy,guard=guard,gaddress=gaddress,gnumber=gnumber,sphoto=sphoto,aphoto=aphoto,svaccine=svaccine,certi=certi)
        student.save()
    return render(request,'hostel/student_registration.html')

def visitor_registration(request):
    return render(request,'hostel/visitor.html')

def facilities(request):
    return render(request,'hostel/facilities.html')

def student_registration(request):
    return render(request,'hostel/student_registration.html')
