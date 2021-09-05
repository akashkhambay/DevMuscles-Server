from django.http import Http404
from rest_framework.views import APIView
from .models import Workout
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import WorkoutSerializer
from rest_framework.decorators import api_view

# Create your views here.
class WorkoutList(APIView):    
    def get(self, request, format=None):
            workouts = Workout.objects.all()
            serializer = WorkoutSerializer(workouts, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    def get_object(self, workout_id):
        try:
            return Workout.objects.get(pk=workout_id)
        except Workout.DoesNotExist:
            raise Http404

    def get(self, request, workout_id, format=None):
        workout = self.get_object(workout_id)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    def put(self, request, workout_id, format=None):
        workout = self.get_object(workout_id)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, workout_id, format=None):
        workout = self.get_object(workout_id)
        workout.delete()
        return Response("Workout has successfully been deleted", status=status.HTTP_204_NO_CONTENT)

   
@api_view(['GET'])
def userWorkouts(self, user_id, format=None):
    workouts = Workout.objects.filter(user_id__pk = user_id)
    serializer = WorkoutSerializer(workouts, many=True)
    return Response(serializer.data)