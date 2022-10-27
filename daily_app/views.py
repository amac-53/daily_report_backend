from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Daily
from .serializers import DailySerializer
from django.http import Http404


class DailyList(APIView):
    def get(self, request):
        reports = Daily.objects.filter(isOpen=True).values('id', 'date', 'evaluation').order_by('-date')
        serializer = DailySerializer(reports, many=True)
        return Response(serializer.data)
    

class DailyDetail(APIView):
    def get_object(self, pk):
        try:
            return Daily.objects.get(pk=pk)
        except Daily.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = DailySerializer(report)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request, cat):
        reports = Daily.objects.filter(isOpen=True).values('date', cat).order_by('-date')
        serializer = DailySerializer(reports, many=True)
        return Response(serializer.data)
