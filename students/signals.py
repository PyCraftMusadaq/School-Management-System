from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime 
year = datetime.date.today().year
from .models import CandidateDetail,StudentClass,ParentsDetail
@receiver(post_save,sender=ParentsDetail)
def create_student_class(sender,instance,created,**kwargs):
    if created:
        FName = instance.student.First_Name + " "+ instance.student.Last_Name

        StudentClass.objects.create(
            student=instance.student,
            Full_Name=FName,
            Father_Name=instance.Father_Name,
            Gender=instance.student.Gender,
            Class=instance.student.Class,
            session=year
            )

