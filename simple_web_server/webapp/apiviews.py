from rest_framework.decorators import api_view
from rest_framework.response import Response

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from .models import Teacher, Subject, Clas, Learningactivity
from .serializers import ClasSerializer, TeacherSerializer, LearningActivitiesSerializer

engine = create_engine(
    "postgresql://admin:prosto100@localhost/Test_web_server1", echo=True)

session = scoped_session(
    sessionmaker(bind=engine)
)

@api_view(['GET'])
def classes_view(request):
        classes = session.query(Clas).all()
        serializer = ClasSerializer(classes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def teachers_view(request):
        teachers = session.query(Teacher).all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def teacher_detail_view(request, teacher_id):
    print("teacherid:" + str(teacher_id))
    learningactivities = session.query(Learningactivity).filter(Learningactivity.idteacher == teacher_id).all()
    print(len(learningactivities))
    for la in learningactivities:
        print("learningactivities:", la)
        #Learningactivity.objects.filter(idteacher=teacher_id)
    #classes = []
    #subjects = []
    #for la in learningactivities:
    #    clas = session.query(Clas).filter(Clas.id == la.idclass)
    #    subject = session.query(Subject).filter(Subject.id == la.idsubject)
    #    classes.append(clas)
    #    subjects.append(subject)
    #teacher = session.query(Teacher).filter(Teacher.id == teacher_id)
    serializer = LearningActivitiesSerializer(learningactivities, many=True)
    return Response(serializer.data)