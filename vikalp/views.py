from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from .models import Branch, Company, Message
from .forms import RegistrationForm, CompanyForm


# Create your views here.
def index(request):
    branch = Branch.objects.all()
    return render(request, 'vikalp/index.html', {'branches':branch})


def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('vikalp:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            error_message = "Invalid Login Details Supplied"
            print "Invalid login details:{0}, {1}".format(username, password)
            return render(request, 'vikalp/sign.html', {'branches':Branch.objects.all(), 'error_message':error_message})
    else:
        return render(request, 'vikalp/sign.html', {'branches':Branch.objects.all()})


class RegistrationView(FormView):
    template_name = 'vikalp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('vikalp:index')
    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['branches'] = Branch.objects.all()
        return context

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('vikalp:index'))


def add_company(request):
    if request.method == 'POST':
        a = Company(user=request.user)
        form = CompanyForm(request.POST, instance=a)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CompanyForm()
    return render(request, 'vikalp/add_company.html', {'form': form, 'branches':Branch.objects.all()})

@login_required
def list(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method == 'POST':
        c = request.POST.get('ctc')
        ls = request.POST.getlist('location')
        e = request.POST.get('experience')
        if ls:
            companies = branch.company_set.filter(ctc__gte=c).filter(experience__gte=e).filter(location__in=ls)
        else:
            companies = branch.company_set.filter(ctc__gte=c).filter(experience__gte=e)
    else:
        companies = branch.company_set.all
    return render(request, 'vikalp/listOfCompany.html', {'branch':branch, 'companies':companies, 'branches':Branch.objects.all()})

@login_required
def detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'vikalp/individualcomp.html', {'company':company, 'branches':Branch.objects.all()})

def contact(request):
    if request.method == 'POST':
        m = Message(name=request.POST['name'], email=request.POST['email'], contact=request.POST['contact'], message=request.POST['message'])
        m.save()
        return HttpResponseRedirect(reverse('vikalp:index'))
    else:
        return render(request, 'vikalp/contact.html', {'branches':Branch.objects.all()})