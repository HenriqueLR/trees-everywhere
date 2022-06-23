from django.http import HttpResponseRedirect


def login_required(function):
    def wraper(request, *args, **kwargs):
        if not (request.user.is_authenticated and \
                request.user.account.filter(status_account=True).exists()):
            return HttpResponseRedirect('/accounts/sign_out/')
        return function(request, *args, **kwargs)

    wraper.__doc__=function.__doc__
    wraper.__name__=function.__name__
    return wraper
