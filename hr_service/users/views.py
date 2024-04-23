from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import User

class UserListView(ListView):

    model = User
    template_name = "user_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"