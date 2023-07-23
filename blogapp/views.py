from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
# Create your views here.
from .models import Post, Category
from .forms import PostForm, NewUserForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def home(request):
    # load all the post from db(10)
    # load all the post from db(10)
    posts = Post.objects.all().order_by('-created_at')[:11]
    # print(post)
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


@login_required(login_url="/login")
def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


@login_required(login_url="/login")
def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


# for testing only
# def create_testform(request):
#     form = PostForm()
#     context = {'form': form}
#     return render(request, 'test.html', context)


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # replace 'home' with the name of your home page URL pattern
    else:
        form = PostForm()
    return render(request, 'test.html', {'form': form})


@login_required(login_url="/login")
def update_post(request, id):
    # check if the form has been submitted
    post = get_object_or_404(Post, post_id=id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # save the updated post object
            yourmodel = form.save(commit=False)
            yourmodel.author = request.user
            yourmodel.save()
            form.save()
            # return redirect('post_detail', post_id=id)
            return redirect('home')
    else:
        # create a form instance and populate it with data from the post object
        form = PostForm(instance=post)

    return render(request, 'test.html', {'form': form})


@login_required(login_url="/login")
def delete_post(request, id):
    # get the post object with the given id
    post = get_object_or_404(Post, post_id=id)

    # delete the post object
    post.delete()

    return redirect('home')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            print("Success")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Enter Information according to the given constraints.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"form": form})


def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Show an error message
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


@login_required(login_url="/login")
def logout_request(request):
    logout(request)
    return redirect('register')


@login_required
def get_my_articles(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'author_post.html', context)
