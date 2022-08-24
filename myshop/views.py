import imp
from math import ceil
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import prdlist, contact, Order, orderstatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.

@login_required(login_url='login')
def index(request):
    datalst = []
    specificdata = prdlist.objects.values('prd_cat','id')
    cats = {x['prd_cat'] for x in specificdata}
    for i in cats:
        products = prdlist.objects.filter(prd_cat=i)
        p = len(products)
        nslide = p//4 + ceil((p/4)-(p//4))
        datalst.append([products,range(1,nslide),nslide])
    data = {'lst':datalst,'uname':request.session['username']}
    return render(request,'shop/index.html',data)

def search_result(stxt, prd):
    txt = stxt.lower() 
    print(prd.prd_name.lower())
    if (txt in prd.prd_name.lower() or txt in prd.prd_cat.lower() or txt in prd.prd_subcat.lower() or txt in prd.prd_des.lower()):
        return True
    else:
        return False

@login_required(login_url='login')
def search(request):
    searchtxt = request.GET.get('srch')
    datalst = []
    specificdata = prdlist.objects.values('prd_cat','id')
    cats = {x['prd_cat'] for x in specificdata}
    for i in cats:
        products = prdlist.objects.filter(prd_cat=i)
        search_prd = [prd for prd in products if search_result(searchtxt,prd)]
        p = len(search_prd)
        nslide = p//4 + ceil((p/4)-(p//4))
        if p>0:
            datalst.append([search_prd,range(1,nslide),nslide])
    if (len(datalst)==0):
        msg = True
    else:
        msg = False
    data = {'lst':datalst,'msg':msg,'uname':request.session['username']}
    return render(request,'shop/search.html',data)

@login_required(login_url='login')
def product(request, id):
    recent = []
    prd = prdlist.objects.get(id=id)
    if 'recent_prd' in request.session:
        if id in request.session['recent_prd']:
            request.session['recent_prd'].remove(id)
        recent = prdlist.objects.filter(pk__in=request.session['recent_prd'])
        request.session['recent_prd'].insert(0,id)
    else:
        request.session['recent_prd'] = [id]
    request.session.modified = True
    return render(request,'shop/productview.html',{'prd':prd,'uname':request.session['username'],'recent':recent})

@login_required(login_url='login')
def about(request):
    return render(request,'shop/about.html',{'uname':request.session['username']})

@login_required(login_url='login')
def Contact(request):
    addmsg = contact()
    if request.method == 'POST':
        addmsg.name = request.POST.get('name','')
        addmsg.mail = request.POST.get('mail','')
        addmsg.phone = request.POST.get('phone','')
        addmsg.message = request.POST.get('msg','')
        addmsg.save()
        msg = True
        return render(request,'shop/contact.html',{'msg':msg})
    return render(request,'shop/contact.html',{'uname':request.session['username']})

@login_required(login_url='login')
def checkout(request):
    addorder = Order()
    if request.method == 'POST':
        addorder.items = request.POST.get('items','')
        addorder.amount = request.POST.get('amount','')
        addorder.name = request.POST.get('name','')
        addorder.phone = request.POST.get('phone','')
        addorder.email = request.POST.get('email','')
        addorder.address1 = request.POST.get('address1','')
        addorder.address2 = request.POST.get('address2','')
        addorder.country = request.POST.get('country','')
        addorder.state = request.POST.get('state','')
        addorder.pin = request.POST.get('pin','')
        addorder.save()
        msg = True
        oid = addorder.order_id
        status = orderstatus(order_id=oid,status="Your order has been placed!")
        status.save()
        return render(request,'shop/checkout.html',{'msg':msg,'id':oid,'uname':request.session['username']})
    return render(request,'shop/checkout.html',{'uname':request.session['username']})

@login_required(login_url='login')
def tracker(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        orderid = request.POST.get('orderid')
        show = Order.objects.filter(order_id=orderid,email=email)
        if len(show) > 0:
            status = orderstatus.objects.filter(order_id=orderid)
            prd = Order.objects.get(order_id=orderid)
            showstatus = []
            for i in status:
                showstatus.append({'status':i.status,'time':i.timestamp})
            return render(request,'shop/tracker.html',{'status':showstatus,'prd':prd,'uname':request.session['username']})
        else:
            msg = 'No order with such Order Id or Email'
            return render(request,'shop/tracker.html',{'msg':msg,'uname':request.session['username']})
    return render(request,'shop/tracker.html',{'uname':request.session['username']})

@login_required(login_url='login')
def cart(request):
    products = prdlist.objects.all()
    return render(request,'shop/cart.html',{'products':products,'uname':request.session['username']})

def lgnpage(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        upwd = request.POST.get('user_pwd')
        validation = authenticate(request,username=uname,password=upwd)
        if validation is not None:
            login(request,validation)
            request.session['username'] = uname
            return redirect('/shop')
        else:
            msg = True
            return render(request,'shop/login.html',{'msg':msg,'uname':request.session['username']})
    return render(request,'shop/login.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('login')
    return render(request,'shop/register.html',{'form':form})

def lgoutpage(request):
    logout(request)
    return redirect('login')