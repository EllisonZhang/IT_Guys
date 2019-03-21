from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Review, Picture, Video
from django.urls import reverse_lazy
from newsapi import NewsApiClient

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['review_list'] = Review.objects.all()
        context['picture_list'] = Picture.objects.all()
        context['video_list'] = Video.objects.all()
        return context
    

class ReviewCreateView(LoginRequiredMixin, CreateView):
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
    newsapi = NewsApiClient(api_key='7184697691164311aaca455ed36c0b68')
    top_headlines = newsapi.get_top_headlines(sources='ign')
    games = Game.objects.all()
    return render(request, 'wegame/home.html', {
        'articles':top_headlines['articles'], 
        'games': games
    })

def about(request):
    response = render(request, 'wegame/about.html')
    return response

def news(request):
    newsapi = NewsApiClient(api_key='7184697691164311aaca455ed36c0b68')
    top_headlines = newsapi.get_top_headlines(sources='ign')
    return render(request, 'wegame/news.html', {
        'articles':top_headlines['articles']
    })

