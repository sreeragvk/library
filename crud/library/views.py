from django.shortcuts import render
from library.models import Book
from library.forms import Bookform

def home(request):
    books_created=Book.objects.all()
    return render(request,'home.html',{'b':books_created})
def create(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        d=request.POST['d']
        p=request.POST['p']
        book_create=Book.objects.create(Title=t,Author=a,Date_published=d,price=p)
        book_create.save()
        return home(request)
    return render(request,'create.html')

def view(request,v):
    book_view=Book.objects.get(id=v)
    return render(request,'view.html',{'w':book_view})
def delete(request,d):
    book_delete=Book.objects.get(id=d)
    book_delete.delete()
    return home(request)
def edit(request,e):
    book_edit=Book.objects.get(id=e)
    if(request.method=="POST"):
        form=Bookform(request.POST,instance=book_edit)
        if form.is_valid():
            form.save()
            return home(request)
    form=Bookform(instance=book_edit)
    return render(request,'edit.html',{'r':form})





