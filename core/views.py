from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactsView(TemplateView):
    template_name = 'core/contacts.html'