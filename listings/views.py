from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(request.GET.get('page'))

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
        'photo_urls': _create_photo_url_list(listing)
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')


def _create_photo_url_list(listing):
    result = []
    for i in range(1, 8):
        photo_prop_name = f"photo_{i}"
        existing = getattr(listing, photo_prop_name, None)
        if not existing:
            return result
        result.append(existing.url)
