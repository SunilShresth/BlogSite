from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User


def index(request):
    """
    view function for home page of site
    """
    return render(request, 'index.html',)


class BlogListView(generic.ListView):


class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog


class BloggerListView(generic.ListView):


class BlogsByAuthorListView(generic.ListView):
    """
    View for a list of blogs posted by a particular blogger
    """
    model = Blog
    paginate_by = 5
    template_name = 

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor
        """
        id = self.kwargs['pk']
        by_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=by_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        context = super(BlogsByAuthorListView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context