from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    contacts=Contact.objects.all()
    context={
    "contacts":contacts
    }
    return render(request,"contactlist/index.html",context)

def addcontact(request):
    
    if request.method=="POST":
        contact_name=request.POST.get("fname")
        email=request.POST.get("inmail")
        phone=request.POST.get("phnumber")
        #print("hi")
        #contact=Contact.objects.create(contact_name=fname,email=inmail,phone=phnumber)
        contact=Contact.objects.create(contact_name=contact_name,email=email,phone=phone)
        contact.save()
        return redirect("contactlist:index")
    return render(request,"contactlist/addcontact.html")   

def editcontact(request,contact_id):
    connect = get_object_or_404(Contact, pk=contact_id)
    if request.method=="POST":
        contact_name=request.POST.get("fname")
        email=request.POST.get("inmail")
        phone=request.POST.get("phnumber")
        connect.contact_name=contact_name
        connect.email=email
        connect.phone=phone
        connect.save()
        return redirect("contactlist:index")
    #contact=get_object_or_404(Contact,pk=contact_id)
    return render(request,"contactlist/editcontact.html",{"connect":connect})
def deleteconfirmation(request,contact_id):
    dele=get_object_or_404(Contact,pk=contact_id)
    if request.method=="POST":
        dele.delete()
        return redirect("contactlist:index")
    return render(request,"contactlist/deleteconfirmation.html",{"dele":dele})






