from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm, CompleteProfileForm
from rango.bing_search import run_query


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': page_list}
    
    # site visits

    # visits = int(request.COOKIES.get('visits', 1))
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
    
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    
    context_dict['visits'] = visits

    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "I am me."}
    visits = request.session.get('visits')
    if visits:
        count = visits
    else:
        count = 1
    context_dict['visits'] = count
    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        category.views = category.views + 1
        category.save()
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = category

        # search
        result_list = []
        if request.method == 'POST':
            query = request.POST['query'].strip()
            if query:
                result_list = run_query(query)
        context_dict['result_list'] = result_list

    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors

    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.first_visit = datetime.now() 
                page.last_visit = datetime.now()
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()
    context_dict = {'form': form, 'category': cat}
    return render(request, 'rango/add_page.html', context_dict)


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})


def track_url(request):
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.last_visit = datetime.now()
                page.save()
            except:
                return redirect('index')
        else:
            return redirect('index')
    return redirect(page.url)


@login_required
def register_profile(request):
    context_dict = {}
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        registered = True
    except:
        registered = False

    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
    else:
        form = UserProfileForm()
    
    context_dict['form'] = form
    context_dict['registered'] = registered
    return render(request, 'registration/profile_registration.html', context_dict)


@login_required
def profile(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        try:
            user_profile = UserProfile.objects.get(user=user)
        except:
            user_profile = None
    except:
        return index(request)
    context_dict['profile'] = user_profile
    context_dict['person'] = user
    return render(request, 'registration/profile.html', context_dict)


def users(request):
    context_dict = {}
    users = User.objects.filter(is_active=True)
    context_dict['users'] = users
    return render(request, 'rango/users.html', context_dict)


@login_required
def update_profile(request, user_id):
    context_dict = {}
    
    try:
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
    except:
        print "Can't get user object."
        return index(request)

    if request.method == 'POST':
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            
            user_profile.website = form.cleaned_data['website']
            if 'picture-clear' in request.POST:
                if request.POST['picture-clear']:
                    user_profile.picture = None
            if 'picture' in request.FILES:
                user_profile.picture = request.FILES['picture']
            user_profile.save()
            
            return profile(request, user.username)
    else:
        form = CompleteProfileForm(initial={'username': user.username,
                                            'email': user.email,
                                            'website': user_profile.website,
                                            'picture': user_profile.picture})

    context_dict['form'] = form
    context_dict['person'] = user
    context_dict['profile'] = user_profile
    return render(request, 'registration/profile_form.html', context_dict)


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__startswith=starts_with)[:max_results]
    else:
        cat_list = Category.objects.all()
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list


def suggest_category(request):
    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    cat_list = get_category_list(8, starts_with)
    return render(request, 'rango/cats.html', {'cats': cat_list})


@login_required
def auto_add_page(request):
    cat_id = None
    url = None
    title = None
    context_dict = {}
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        url = request.GET['url']
        title = request.GET['title']
        if cat_id:
            category = Category.objects.get(id=int(cat_id))
            p = Page.objects.get_or_create(category=category, url=url, title=title)[0]
            p.first_visit = datetime.now()
            p.last_visit = datetime.now()
            p.save()
            pages = Page.objects.filter(category=category).order_by('-views')
            context_dict['pages'] = pages
    return render(request, 'rango/pages.html', context_dict)