from django.shortcuts import render
from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['title'] = 'Index'
        return context


def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'chat/chatroom.html', context)
