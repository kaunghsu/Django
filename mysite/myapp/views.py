from django.shortcuts import render
from.models import Post ,Myfriend

# Create your views here.
def postdata(request):
    post_data = Post.objects.all()
    context = {'post_data':post_data}
    return render(request,'post.html',context)

def myfriends(request):
    friends = Myfriend.objects.all()
    context = {'friends': friends}
    return render(request,'myfriend.html',context)