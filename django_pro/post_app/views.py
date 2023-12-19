from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostAPI(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()