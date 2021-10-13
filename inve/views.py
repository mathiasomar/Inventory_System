from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from inve.models import Staff, Supplier, Product, Order, Delivery

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('/admin_home')
        else:
            messages.info(request, 'Invalid username/password')
            return redirect('/admin_login')
    else:
        return render(request, 'login.html')

def admin_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/admin_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/admin_register')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                messages.info(request, 'Account Successfully Registered')
                return redirect('/admin_register')
        else:
            messages.info(request, 'Password Do not Match')
            return redirect('/admin_register')
    else:
        return render(request, 'register.html')

def admin_logout(request):
    auth.logout(request)
    return redirect('/admin_login')

def admin_home(request):
    staff_number = Staff.objects.all().count()
    product_number = Product.objects.all().count()
    order_number = Order.objects.all().count()
    delivery_number = Delivery.objects.all().count()
    return render(request, 'index.html', {'staff_number':staff_number, 'product_number':product_number, 'order_number':order_number, 'delivery_number':delivery_number})

def add_staff(request):
    if request.method == 'POST':
        idno = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        dept = request.POST['dept']

        try:
            staff = Staff(id=idno, fname=fname, lname=lname, phone=phone, email=email, department=dept)
            staff.save()
            messages.info(request, 'Staff Added Successfully')
            return redirect('/add_staff')
        except:
            messages.info(request, 'Failed to Add Staff')
            return redirect('/add_staff')
    else:
        return render(request, 'add_staff.html')

def manage_staff(request):
    staffs = Staff.objects.all()
    return render(request, 'manage_staff.html', {'staffs':staffs})

def search_staff(request):
    if request.method == 'POST':
        search = request.POST['search']
        staffs = Staff.objects.filter(fname__contains=search)
        return render(request, 'manage_staff.html', {'search':search, 'staffs':staffs})
    else:
        return render(request, 'manage_staff.html')

def edit_staff(request, id):
    staff = Staff.objects.get(id=id)
    return render(request, 'edit_staff.html', {'staff':staff})

def edi_staff_save(request):
    if request.method == 'POST':
        idno = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        dept = request.POST['dept']

        try:
            staff = Staff.objects.get(id=idno)
            staff.id = idno
            staff.fname = fname
            staff.lname = lname
            staff.phone = phone
            staff.email = email
            staff.department = dept

            staff.save()
            messages.info(request, 'Update Successfully')
            return redirect('/edit_staff/'+idno)
        except:
            messages.info(request, 'Failed to Update')
            return redirect('/edit_staff/'+idno)
    else:
        return render(request, 'edit_staff.html')

def add_supplier(request):
    if request.method == 'POST':
        id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']

        try:
            supplier = Supplier(id=id, fname=fname, lname=lname, phone=phone, email=email, company=company)
            supplier.save()
            messages.info(request, 'Supplier Added Successfully')
            return redirect('/add_supplier')
        except:
            messages.info(request, 'Failed to add Supplier')
            return redirect('/add_supplier')
    else:
        return render(request, 'add_supplier.html')

def manage_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'manage_supplier.html', {'suppliers':suppliers,})

def search_supplier(request):
    if request.method == 'POST':
        search = request.POST['search']
        suppliers = Supplier.objects.filter(fname__contains=search)
        return render(request, 'manage_supplier.html', {'search':search, 'suppliers':suppliers})
    else:
        return render(request, 'manage_supplier.html')

def add_product(request):
    if request.method == 'POST':
        id = request.POST['id']
        pname = request.POST['pname']
        pcategory = request.POST['pcategory']
        pquantity = request.POST['pquantity']
        pprice = request.POST['pprice']
        sid = request.POST['supplier']

        supplier_obj = Supplier.objects.get(id=sid)

        try:
            product = Product(id=id, pname=pname, pcategory=pcategory, pquantity=pquantity, pprice=pprice, sid=supplier_obj)
            product.save()
            messages.info(request, 'Product Added Successfully')
            return redirect('/add_product')
        except:
            messages.info(request, 'Failed to Add Product')
            return redirect('/add_product')
    else:
        suppliers = Supplier.objects.all()
        return render(request, 'add_product.html', {'suppliers':suppliers})

def manage_product(request):
    products = Product.objects.all()
    return render(request, 'manage_product.html', {'products':products})

def search_product(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = Product.objects.filter(pname__contains=search)
        return render(request, 'manage_product.html',{'search':search, 'products':products})
    else:
        return render(request, 'manage_product.html')

def order(request):
    return render(request, 'order.html')

def delivery(request):
    return render(request, 'delivery.html')