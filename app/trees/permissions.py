from accounts.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib import messages


class PermissionsGeralMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(PermissionsGeralMixin, cls).as_view())

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(PermissionsGeralMixin, self).dispatch(request, *args, **kwargs)


class PermissionsTreeCreateMixin(PermissionsGeralMixin):

    def form_valid(self, form):
        messages.success(self.request, self.message_success)
        return super(PermissionsTreeCreateMixin, self).form_valid(form)