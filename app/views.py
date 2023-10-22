from django.http import HttpResponse
from django.shortcuts import redirect
from .models import UrlRedirect


def welcome(request):
    return HttpResponse('Welcome')


def redirect_to_url(request, job_id):
    try:
        # Get the UrlRedirect instance based on the provided job_id
        url_redirect = UrlRedirect.objects.get(job_id=job_id)

        # Increment the 'clicks' counter
        url_redirect.clicks += 1
        url_redirect.save()

        # Redirect to the URL associated with the job_id
        return redirect(url_redirect.url)
    except UrlRedirect.DoesNotExist:
        return redirect('welcome')
