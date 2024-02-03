from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import UserForm, MessageForm
from .models import MessageModel


class MessageView(View):
    def get(self, request):
        messages = MessageModel.objects.filter(to_user=request.user.id)
        return render(request, "message_to.html", {"messages": messages})
    
    def post(self, request):
        form = MessageForm(request.POST,  files=request.FILES)
        messages = MessageModel.objects.filter(to_user=request.user.id)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = request.user
            message.save()
        
        return render(request, 'message_to.html', {"form": form, "messages": messages})




class RegisterView(View):
    def get(self, request):
        create_form = UserForm()
        context = {
            'form': create_form
        }
        return render(request, "register.html", context)
        
    def post(self, request):
        create_form = UserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            user = create_form.save()
            return redirect('login')
        else: 
            context = {
                "form": create_form
            }
            return render(request, 'register.html', context)

