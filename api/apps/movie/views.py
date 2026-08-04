from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


# Create your views here.


class GetMoviesView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                movie = Movie.objects.get(id=pk)
            except Movie.DoesNotExist:
                return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)

        all_movies = Movie.objects.all()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        
        
        



