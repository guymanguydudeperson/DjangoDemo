from django.shortcuts import render, redirect
from .firebase import database_ref


# Function to add user to Firebase Realtime Database
def add_user_to_firebase(name, email):
    user_ref = database_ref.child('users').push({
        'name': name,
        'email': email
    })
    return user_ref


# Function to retrieve users from Firebase Realtime Database
def get_users_from_firebase():
    users_ref = database_ref.child('users')
    users = users_ref.get()
    return users


# View to handle adding a user
def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        add_user_to_firebase(name, email)
        return redirect('list_users')  # Redirect to the list_users view
    return render(request, 'add_user.html')


# View to handle listing users
def list_users(request):
    users = get_users_from_firebase()
    return render(request, 'list_users.html', {'users': users})


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

def print_w2(request):
    if request.method == 'POST':
        name = request.user.get_full_name()
        email = request.user.email
        subject = f"EdTech Request Submitted:"
        message = (
            f"Hello {name},\n\n"
            f"Your message for has been successfully submitted. \n\n"
            f"Summary: \n"
            f"Thank you, \n"
            f"EdTech @ ISM"
        )
        send_mail(subject, message, None, [email], fail_silently=False)
        return redirect('thank_you')  # Or wherever you want to redirect
    return render(request, 'contact_us.html')
