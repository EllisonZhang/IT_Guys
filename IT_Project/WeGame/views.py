from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Game, Review
from django.urls import reverse_lazy

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['review_list'] = Review.objects.all()
        return context
    

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ['game_reviewed', 'comment_text']
    success_url = reverse_lazy('index')
    def get(self, *args, **kwargs):
        pk1 = kwargs.get('pk1', None)
        pk2 = kwargs.get('pk2', None)
        print(pk1)
        print(pk2)
        return super(ReviewCreateView, self).get(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreateView, self).form_valid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review_edit.html'
    fields = ['game_reviewed', 'comment_text']
    success_url = reverse_lazy('index')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('index')


# Create your views here.
def index(request):
    response = render(request, 'wegame/home.html')
    return response

def about(request):
    response = render(request, 'wegame/about.html')
    return response


