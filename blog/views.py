from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required



from .models import Post
from .forms import PostForm


@login_required
def home(request):
	post = Post.objects.all().order_by('-date')
	context={
		'datas':post
	}

	return render(request, 'blog/home.html',context)

# CREATING NEW BLOG POST

@login_required
def form_entry(request):
	# instance = Post(person=request.user.username)
	# form = PostForm(instance=instance)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			var = form.save(commit=False)
			var.person = request.user
			var.save()
<<<<<<< HEAD

=======
>>>>>>> 6c526d8f50087d6bc0a6ac1ea56d4da03fb3ca5f
			return redirect('home')


	else:
		form = PostForm()

	return render(request, 'blog/forms.html', {'form': form })

# FUNCTION TO SEND PROFILE DETAILS AND TOTAL NUMBER OF BLOGS BY THE USER

@login_required
def profile(request, person_id):
    detail = Post.objects.filter(person_id=person_id)
    count = detail.count()

    context={
        "datas": detail,
        "count":count
        
    }
    return render(request, 'blog/profile.html',context)


#FUNCTION FOR SEARCHING EXISTING USERS AND VIEW ONLY THEIR PUBLIC BLOGS

@login_required
def search(request):
	if request.method=='POST':
		srch = request.POST['srh']
		

		if srch:
			match = Post.objects.filter(Q(person__username__icontains=srch))
			if match:
				context={
					'datas':match,
					'name':srch
				}
				return render(request, 'blog/friend.html',context)
			else:
				messages.warning(request,'NO SUCH USER AVAILABLE')


	return render(request, 'blog/home.html')

# FUNCTION FOR SEARCHING ANY ARTICLE WITH A KEY_WORD

@login_required
def title_search(request):
	if request.method=='POST':
		srch = request.POST['srh']
		print(srch)

		if srch:
			match = Post.objects.filter(Q(title__icontains=srch) | Q(article__icontains=srch) )
			if match:
				context={
					'datas':match,
					'name':srch
				}
				return render(request, 'blog/friend.html',context)
			else:
				messages.warning(request,'NO SUCH BLOG AVAILABLE')


	return render(request, 'blog/home.html')

























