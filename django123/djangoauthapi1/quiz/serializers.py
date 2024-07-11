from .models import QuizforMatric,QuizforInter
from rest_framework import serializers

class QuizforMatricSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizforMatric
        fields = ['id','percentage','question1']
        
class QuizforInterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizforInter
        fields = ['id','percentage','question1','question2']