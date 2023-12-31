from genres.models import Genre
from authors.models import Author


def authors(request):
    return {'authors': Author.objects.all()}


def genres(request):
    return {'genres': Genre.objects.all()}
