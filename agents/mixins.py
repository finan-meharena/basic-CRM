from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganizerAndLoginRequiredMixing(AccessMixin):
        """Verify that the current user is authenticated and is an organizer."""
def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated or not request.user.is_organizer:
        return redirect("login")
    return super().dispatch(request, *args, **kwargs)
    