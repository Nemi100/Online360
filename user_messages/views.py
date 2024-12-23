from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_inbox')
    else:
        form = MessageForm()
    return render(request, 'user_messages/message_form.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'user_messages/inbox.html', {'messages': messages})
