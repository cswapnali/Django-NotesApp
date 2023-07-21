from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib import messages
from .models import Note
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@csrf_protect
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            messages.error(request, "Passwords don't match!")
            return redirect('signup')  
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            user = authenticate(request, username=uname, password=pass1)
            if user is not None:
                login(request, user)
                messages.success(request, 'Signup successful!')  
                return redirect('notes')  
            else:
                messages.error(request, 'Failed to authenticate user')
                return redirect('signup')  
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')  
            return redirect('notes')  
        else:
            messages.error(request, 'Username and Password are incorrect!')
            return redirect('login')  
    return render(request, 'login.html')

@login_required
def note_details(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    shared_username = None
    if note.shared:
        shared_username = note.shared_with.username
    return render(request, 'notes.html', {'note': note, 'shared_username': shared_username})

@login_required
def notes(request):
    user = request.user
    user_notes = Note.objects.filter(user=user)
    shared_notes = Note.objects.filter(shared_with=user)
    notes = user_notes | shared_notes
    return render(request, 'notes.html', {'notes': notes, 'user': user})

@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        content = request.FILES['content']
        if Note.objects.filter(user=request.user, title=title).exists():
            messages.error(request, 'A note with the same title already exists.')
            return redirect('add_note')
        allowed_file_types = {
            'text': ['txt', 'pdf', '.docx'],
            'audio': ['mp3', 'wav'],
            'video': ['mp4', 'mov']
        }
        file_extension = content.name.split('.')[-1].lower()
        if file_extension in allowed_file_types[category]:
            note = Note(title=title, category=category, content=content, user=request.user)
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('notes')
        else:
            messages.error(request, 'Invalid file type. Please upload a valid file.')
            return redirect('add_note')
    return render(request, 'add_note.html')

@login_required
def share_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            note.shared_with.add(user)
            messages.success(request, f'Note shared with {username} successfully!')
            return redirect('notes')
        except User.DoesNotExist:
            messages.error(request, f'User {username} does not exist.')
            return redirect('share_note', note_id=note_id)
    return render(request, 'share_note.html', {'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    
    if note.user != request.user and not note.shared_with.filter(id=request.user.id).exists():
        messages.error(request, 'You do not have permission to delete this note.')
        return redirect('notes')
    
    if note.user == request.user:
        note.delete()
        messages.success(request, 'Note deleted successfully!')
    else:
        note.shared_with.remove(request.user)
        messages.success(request, 'Note unshared successfully!')
    
    return redirect('notes')

def LogOutPage(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')  
    return redirect('login')  
