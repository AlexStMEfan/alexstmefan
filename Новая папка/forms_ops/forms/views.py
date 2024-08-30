from django.shortcuts import render
from .models import lessonmodel
# Create your views here.
def index(request):
    if request.method == 'POST':
        name_Lesson = request.POST['name_Lesson']
        date_lesson = request.POST['date_lesson']
        email_student = request.POST['email_student']
        fio_student = request.POST['fio_student']
        phone_teacher = request.POST['phone_teacher']
        number_classroom = request.POST['number_classroom']
        email_teach_teach_organization = request.POST['email_teach_teach_organization']
        FIO_director_organization = request.POST['FIO_director_organization']
        index_adress = request.POST['index_adress']
        rayon = request.POST['rayon']
        city = request.POST['city']
        street = request.POST['street']
        otzyv = request.POST['otzyv']

        new_lesson = lessonmodel(name_Lesson=name_Lesson, date_lesson=date_lesson, email_student=email_student, fio_student=fio_student, phone_teacher=phone_teacher, number_classroom=number_classroom, email_teach_teach_organization=email_teach_teach_organization, FIO_director_organization=FIO_director_organization, index_adress=index_adress, rayon=rayon, city=city, street=street, otzyv=otzyv)
        new_lesson.save()
    return render(request, 'index.html')