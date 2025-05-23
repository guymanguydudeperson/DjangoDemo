from django.shortcuts import render, redirect
from .firebase import database_ref
from django.shortcuts import render, redirect
from .forms import EmployerInfoForm
from .models import EmployerInfo


# Function to add user to Firebase Realtime Database



# Function to retrieve users from Firebase Realtime Database
def get_users_from_firebase():
    users_ref = database_ref.child('users')
    employee_info_ref = database_ref.child('employeeinformation')
    users = users_ref.get()
    employeeinformation = employee_info_ref.get()
    return employeeinformation
def get_users_from_firebase2():
    users_ref = database_ref.child('users')
    info_ref = database_ref.child('info')
    users = users_ref.get()
    info = info_ref
    info = info.get()
    return info
def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        add_user_to_firebase(name, email)
        return redirect('list_users' ) # Redirect to the list_users view
    return render(request, 'add_user.html' )

# View to handle adding a user


# View to handle listing users
def list_users(request):
    users = get_users_from_firebase()
    employee = get_users_from_firebase()
    info = get_users_from_firebase2()
    return render(request, 'list_users.html', {'employeeinformation': employee, 'info': info})


def edit_user(request, user_id):
    user_ref = database_ref.child('users').child(user_id)
    user = user_ref.get()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_ref.update({
            'name': name,
            'email': email,
        })
        return redirect('list_users')
    return render(request, 'edit_user.html', {'user': user, 'user_id': user_id})


def delete_user(request, user_id):
    user_ref = database_ref.child('users').child(user_id)
    user_ref.delete()
    return redirect('list_users')


def home(request):
    return render(request, 'home.html')

def employee(request):
    return render(request, 'employee.html')

def contact_us(request):
    return render(request, 'employee.html')

def info(request):
    return render(request, 'info.html')

def FAQs(request):
    return render(request, 'FAQs.html')

def home(request):
    return render(request, 'home.html')

def UnderstandingTax(request):
    return render(request, 'UnderstandingTax.html')

def UnderstandingW2(request):
    return render(request, 'UnderstandingW2.html')

def collect_info(request):
    if request.method == 'POST':
        form = EmployerInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_info')
    else:
        form = EmployerInfoForm()
    return render(request, 'collect_info.html', {'form': form})

def display_info(request):
    employers = EmployerInfo.objects.all()
    return render(request, 'display_info.html', {'employers': employers})

def add_user_to_firebase(EM_Zipcode,EM_Fedtax,EM_SSTAX,EM_SNN,EM_NAME,EM_Income,EM_NUM,EM_Address,EM_SSincome,Med_TAX
                             ,AL_TIPS,SS_TIPS,dependents,e457_plan,otherplan,employee_type):
    employeeinformation_ref = database_ref.child('employeeinformation').push({
        'EM_Zipcode': EM_Zipcode,
        'EM_Fedtax': EM_Fedtax,
        'EM_SSTAX': EM_SSTAX,
        'EM_SNN': EM_SNN,
        'EM_NAME': EM_NAME,
        'EM_Income': EM_Income,
        'EM_NUM': EM_NUM,
        'EM_Address': EM_Address,
        'EM_SSincome': EM_SSincome,
        'Med_TAX': Med_TAX,
        'AL_TIPS': AL_TIPS,
        'SS_TIPS': SS_TIPS,
        'dependents': dependents,
        'e457_plan': e457_plan,
        'otherplan': otherplan,
        'employee_type': employee_type,
    })
    return employeeinformation_ref

def submit_form(request):
    if request.method == 'POST':
        EM_NAME = request.POST.get('EM_NAME')
        EM_NUM = request.POST.get('EM_NUM')
        EM_Address = request.POST.get('EM_Address')
        EM_Zipcode = request.POST.get('EM_Zipcode')
        EM_SNN = request.POST.get('EM_SNN')
        EM_Income = request.POST.get('EM_Income')
        EM_Fedtax = request.POST.get('EM_Fedtax')
        EM_SSincome = request.POST.get('EM_SSincome')
        EM_SSTAX = request.POST.get('EM_SSTAX')
        Med_TAX = request.POST.get('Med_TAX')
        SS_TIPS = request.POST.get('SS_TIPS')
        AL_TIPS = request.POST.get('AL_TIPS')
        dependents = request.POST.get('dependents')
        e457_plan = request.POST.get('457_plan')
        otherplan = request.POST.get('other')
        employee_type = request.POST.get('employee_type')
        print(EM_NUM)
        print(EM_NAME)
        add_user_to_firebase(EM_Zipcode,EM_Fedtax,EM_SSTAX,EM_SNN,EM_NAME,EM_Income,EM_NUM,EM_Address,EM_SSincome,Med_TAX
                             ,AL_TIPS,SS_TIPS,dependents,e457_plan,otherplan,employee_type)
        return redirect('list_users')  # Redirect to the list_users view
    return render(request, 'list_users.html')

def add_user_to_firebase2(NAME, EIN, STATE, Locality, Address, Zipcode, SSN ):
    info_ref = database_ref.child('info').push({
        'NAME': NAME,
        'EIN': EIN,
        'STATE': STATE,
        'Locality': Locality,
        'Address': Address,
        'Zipcode': Zipcode,
        'SSN': SSN,
    })
    return info_ref

def save_info(request):
    if request.method == 'POST':
        NAME = request.POST.get('NAME')
        EIN = request.POST.get('EIN')
        STATE = request.POST.get('STATE')
        Locality = request.POST.get('Local')
        Address = request.POST.get('Address')
        Zipcode = request.POST.get('Zipcode')
        SSN = request.POST.get('SSN')
        add_user_to_firebase2(NAME, EIN, STATE, Locality, Address, Zipcode, SSN)
        return redirect('employee')  # Redirect to the list_users view
    return render(request, 'employee.html')