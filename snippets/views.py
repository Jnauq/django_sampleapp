from django.shortcuts import render, get_object_or_404
from snippets.models import Snippet
from django.views.generic import ListView, DetailView


def snippet_list(request):
    snippets_list = Snippet.objects.all()
    return render(request, 'snippets/snippet-list.html', {'snippet_list': snippets_list, 'title': 'MY TITLE'})


def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request, 'snippets/snippet-details.html', {'snippet_detail': snippet})


# class SnippetListView(ListView):
#     model = Snippet
#     template_name = 'snippets/snippet-list.html'
#     context_object_name = 'snippet_list'
#
#
# class SnippetDetailView(DetailView):
#     model = Snippet
#     template_name = 'snippets/snippet-details.html'
#     context_object_name = 'snippet_detail'
