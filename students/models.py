from django.db import models

# Create your models here.
# Registration related models...

class CandidateDetail(models.Model):
    First_Name = models.CharField(max_length=255,blank=True,null=True)
    Last_Name = models.CharField(max_length=255,blank=True,null=True)
    Date_of_Birth = models.DateField(blank=True,null=True)
    Class = models.CharField(max_length=100,blank=True,null=True)
    Gender = models.CharField(max_length=100,blank=True,null=True)
    Place_of_Birth= models.CharField(max_length=255,blank=True,null=True)
    Nationality = models.CharField(max_length=100,blank=True,null=True)
    First_Langugae = models.CharField(max_length=100,blank=True,null=True)
    Date_of_Admission = models.DateField(auto_now_add=True,blank=True,null=True)
    other_Languages_known = models.CharField(max_length=255,blank=True,null=True)
    Student_Image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return str(self.id)
    
    def delete(self):
        self.Student_Image.delete()
        super().delete()

class CandidateAddress(models.Model):
    Address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    student = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)

class ParentsDetail(models.Model):
    student = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    Father_Name = models.CharField(max_length=255,blank=True,null=True)
    Father_Email =models.EmailField(max_length=100,blank=True,null=True)
    Father_Qualification=models.CharField(max_length=100,blank=True,null=True)
    Father_Profession = models.CharField(max_length=100,blank=True,null=True)
    Father_Designation = models.CharField(max_length=100,blank=True,null=True)
    Father_Contact_No = models.CharField(max_length=100,blank=True,null=True)
    Mother_Name = models.CharField(max_length=255,blank=True,null=True)
    Mother_Email =models.EmailField(max_length=100,blank=True,null=True)
    Mother_Qualification=models.CharField(max_length=100,blank=True,null=True)
    Mother_Profession = models.CharField(max_length=100,blank=True,null=True)
    Mother_Designation = models.CharField(max_length=100,blank=True,null=True)
    Mother_Contact_No = models.CharField(max_length=100,blank=True,null=True)


class GuardianDetail(models.Model):
    student = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=255,blank=True,null=True)
    Email_Address = models.EmailField(max_length=100,blank=True,null=True)
    Relation_with_student = models.CharField(max_length=100,blank=True,null=True)
    phone_no = models.CharField(max_length=100,blank=True,null=True)
    First_relation = models.CharField(max_length=100,blank=True,null=True)
    Second_relation = models.CharField(max_length=100,blank=True,null=True)
    Number_one = models.CharField(max_length=100,blank=True,null=True)
    Number_two = models.CharField(max_length=100,blank=True,null=True)

class SiblingDetail(models.Model):
    student = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=255,blank=True,null=True)
    Date_of_Birth = models.DateField(blank=True,null=True)
    Gender = models.CharField(max_length=10,blank=True,null=True)
    Class = models.CharField(max_length=100,blank=True,null=True)
    School = models.CharField(max_length=150,blank=True,null=True)


class ReferenceDetail(models.Model):
    student = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    Reference_Through = models.TextField(blank=True,null=True)
    Address = models.TextField(blank=True,null=True)
    Tell_No = models.CharField(max_length=100,blank=True,null=True)




class StudentClass(models.Model):
    student = models.ForeignKey(CandidateDetail,on_delete=models.SET_NULL,null=True)
    Roll_No = models.IntegerField(blank=True,null=True)
    Full_Name = models.CharField(max_length=100,blank=True,null=True)
    Father_Name = models.CharField(max_length=100,blank=True,null=True)
    Gender= models.CharField(max_length=10,blank=True,null=True)
    Class = models.CharField(max_length=20,blank=True,null=True)
    session = models.CharField(max_length=10)

    class Meta:
        ordering = ['-id']
    
    
    def __str__(self):
        return self.Full_Name



class Fee(models.Model):
    Class = models.CharField(max_length=50,unique=True)
    Amount = models.IntegerField()



# Add Fee Table 
class FeeRecord(models.Model):
    MONTH_NAMES = (
        ('January','January'),
        ('Feburary','Feburary'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )
    CLASSES = (
        ('Playgroup','Playgroup'),
        ('Nursery','Nursery'),
        ('Prep','Prep'),
        ('One','One'),
        ('Two','Two'),
        ('Three','Three'),
        ('Four','Four'),
        ('Five','Five'),
        ('Six','Six'),
        ('Seven','Seven'),
        ('Eight','Eight'),
        ('9th','9th'),
        ('10th','10th'),
        ('1stYear','1stYear'),
        ('2ndYear','2ndYear'),
    )
    Full_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Class = models.CharField(max_length=100,choices=CLASSES)
    session = models.CharField(max_length=10)
    Roll_No = models.IntegerField(null=True,blank=True)
    Month = models.CharField(max_length=100,choices=MONTH_NAMES)
    Paid_Date = models.DateField()
    Paid_Amount = models.IntegerField(null=True,blank=True)
    Dues = models.IntegerField(null=True,blank=True)
    student = models.ForeignKey(CandidateDetail,on_delete=models.SET_NULL,null=True)



# Teachers Tables
class Teacher(models.Model):
    Cnic = models.CharField(max_length=20,primary_key=True)
    Full_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
    Degree_Image = models.ImageField(upload_to='Techer_Degree_images/')
    Profile_Image = models.ImageField(upload_to='Teacher_Profile_images/')
    contact = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    Home_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.Full_Name


# Attendence Model of students 
class StudentAttendence(models.Model):
    CHOICES = (
        ('P','P'),
        ('L','L'),
        ('A','A'),
    )
    Full_Name = models.CharField(max_length=100)
    Father_Name =models.CharField(max_length=100)
    Class = models.CharField(max_length=50)
    Roll_No = models.IntegerField()
    Date = models.DateField()
    status = models.CharField(max_length=30,choices=CHOICES)


class Subjects(models.Model):
    title = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    tutor = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    marks = models.IntegerField()


    def __str__(self):
        return self.title



class MarksRecord(models.Model):
    student = models.ForeignKey(StudentClass,on_delete=models.SET_NULL,null=True,related_name='studentname')
    Class = models.CharField(max_length=50)
    rollno = models.IntegerField()
    session = models.IntegerField()
    English_Obj_marks = models.IntegerField(null=True,blank=True)
    Math_Obj_marks = models.IntegerField(null=True,blank=True)
    Bio_Obj_marks = models.IntegerField(null=True,blank=True)
    Phy_Obj_marks = models.IntegerField(null=True,blank=True)
    Chem_Obj_marks = models.IntegerField(null=True,blank=True)
    Science_Obj_marks = models.IntegerField(null=True,blank=True)
    Urdu_Obj_marks = models.IntegerField(null=True,blank=True)
    Pak_Obj_marks = models.IntegerField(null=True,blank=True)
    Isl_Obj_marks = models.IntegerField(null=True,blank=True)
    Comp_marks = models.IntegerField(null=True,blank=True) 

    def __str__(self):
        return self.student.Full_Name
    


class ExpenseRecords(models.Model):
    Name = models.CharField(max_length=200)
    Amount = models.IntegerField()
    comment = models.TextField()
    Date = models.DateField() 

class TeacherAttandance(models.Model):
    CHOICES = (
        ('P','P'),
        ('L','L'),
        ('A','A'),
    )
    Full_Name = models.CharField(max_length=100)
    Father_Name =models.CharField(max_length=100)
    Cnic = models.CharField(max_length=100)
    Date = models.DateField()
    status = models.CharField(max_length=30,choices=CHOICES)
