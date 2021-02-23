from rest_framework import serializers

from .models import Clas, Subject, Teacher, Learningactivity


class ClasSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Clas.objects.create(**validated_data)


class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(max_length=20)
    qualification = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


class LearningActivitiesSerializer(serializers.Serializer):
    idclass = serializers.IntegerField(read_only=True)
    idteacher = serializers.IntegerField(read_only=True)
    idsubject = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Learningactivity.objects.create(**validated_data)