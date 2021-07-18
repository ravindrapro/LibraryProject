from django.shortcuts import render,redirect
from Book.models import Book
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    all_books = Book.active_objects.all()
    return render(request,template_name='home.html',context={"books": all_books})

def save_book(request):
    # print("In save Book")
    # print(request.POST)
    if request.POST.get("id"):

        book_obj = Book.objects.get(id=request.POST.get("id"))
        b_name = request.POST.get("name")
        b_author = request.POST.get("auth")
        b_price = request.POST.get("price")
        b_qty = request.POST.get("qty")
        b_pub = request.POST.get("pub")
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.price = b_price  
        book_obj.qty = b_qty
        if b_pub == "on":
            flag = True
        else:
            flag = False
        book_obj.is_published = flag
        book_obj.save()
        return redirect('welcome')


    # print(b_name,b_author,b_price,b_qty,b_pub)
    else:
        b_name = request.POST.get("name")
        b_author = request.POST.get("auth")
        b_price = request.POST.get("price")
        b_qty = request.POST.get("qty")
        b_pub = request.POST.get("pub")
        if b_pub == "on":
            flag = True
        else:
            flag = False
        b = Book(name=b_name,author=b_author,price=b_price,qty=b_qty,is_published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request,id):
    try:
        print("AA")
        book_obj = Book.objects.get(id=id)
    except Exception:
        msg = f"No book found for id:{id}"
        return HttpResponse(msg)

    # book_obj=Book.objects.get(id=id)
    # all_books=Book.objects.all().filter(is_deleted='N')
    all_books = Book.inactive_objects.all()

    return render(request, template_name='home.html',context={"book": book_obj,"books": all_books})

def delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_deleted = 'Y'
    # book_obj.delete()
    book_obj.save()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request, template_name='home.html',context={"books": all_deleted_books})

def hard_delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    # book_obj.is_deleted = 'Y'
    # book_obj.delete()
    book_obj.delete()
    return redirect('welcome')

def restore_book(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 'N'
    # book_obj.delete()
    book_obj.save()
    return redirect('welcome')