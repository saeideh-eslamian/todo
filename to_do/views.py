from django.shortcuts import render
from django.views.generic import ListView, DetailView,DeleteView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import ToDo
from .forms import ToDOForm
from django.db.models import Q

class ToDoListView(ListView):
    template_name ='to_do/to-do-list.html'
    model = ToDo
    context_object_name = 'to_do_list'

    def get_queryset(self): 
        search = self.request.GET.get('search','')
        result_search =ToDo.objects.filter(Q(title__icontains=search)
                         | Q(description__icontains=search)).order_by('complete','expiry_date')
        return result_search
    
class DeleteToDoView(DeleteView):
    model = ToDo
    success_url ='/'
    context_object_name = "delete_do"

class DoRegisterView(View):  
    def get(self,request):
        return render(request,'to_do/do-register.html',{
            'to_do_form':ToDOForm()
        })

    def post(self,request):
        # to_do = ToDo.objects.get(pk=id).by_order('-expiry_date')
        to_do_form = ToDOForm(request.POST)
        if to_do_form.is_valid():
            to_do_form.save()
            return HttpResponseRedirect(reverse('to-do'))
        return render(request,'to-do/do-register.html',{
            'to_do_form': to_do_form
        })


class DetailDoView(DetailView):
    template_name = 'to_do/detail-do.html'
    model = ToDo
    context_object_name = 'detail_do'     

class UpdateToDoView(UpdateView):
   model = ToDo
   fields = '__all__'
   success_url ='/'   
    
      

   



    

    
