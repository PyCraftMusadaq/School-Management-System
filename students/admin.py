from django.contrib import admin
from .models import CandidateDetail,CandidateAddress,ParentsDetail,SiblingDetail,GuardianDetail,ReferenceDetail,StudentClass,Fee,FeeRecord,Teacher,StudentAttendence,Subjects,MarksRecord,ExpenseRecords,TeacherAttandance

# Register your models here.
@admin.register(CandidateDetail)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Last_Name','Date_of_Birth','Class','Gender','Place_of_Birth','Nationality','First_Langugae','Date_of_Admission','other_Languages_known')
@admin.register(CandidateAddress)
class StudentAddressAdmin(admin.ModelAdmin):
    list_display = ('id','Address','city','state','student')
@admin.register(ParentsDetail)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ('id','Father_Name','Father_Email','Father_Qualification','Father_Profession','Father_Designation','Father_Contact_No','Mother_Name','Mother_Email','Mother_Qualification','Mother_Profession','Mother_Designation','Mother_Contact_No','student')
@admin.register(GuardianDetail)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('id','Full_Name','Email_Address','Relation_with_student','phone_no','First_relation','Second_relation','Number_one','Number_two','student')
@admin.register(SiblingDetail)
class SiblingAdmin(admin.ModelAdmin):
    list_display = ('id','Full_Name','Date_of_Birth','Gender','Class','School','student')
@admin.register(ReferenceDetail)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id','Reference_Through','Address','Tell_No','student')

@admin.register(StudentClass)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','Roll_No','Full_Name','Father_Name','Gender','Class','student','session')
@admin.register(Fee)
class AdminFee(admin.ModelAdmin):
    list_display= ('id','Class','Amount')

@admin.register(FeeRecord)
class AdminFeeRecord(admin.ModelAdmin):
    list_display = ('id','Full_Name','Father_Name','Class','Roll_No','Month','Paid_Date','Paid_Amount','Dues','student')

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('Cnic','Full_Name','Father_Name','Education','Degree_Image','Profile_Image','contact','Address','Home_contact')
@admin.register(StudentAttendence)
class AdminAttendence(admin.ModelAdmin):
    list_display = ('id','Full_Name','Father_Name','Class','Roll_No','Date','status')

@admin.register(Subjects)
class AdminSubjects(admin.ModelAdmin):
    list_display = ('id','title','tutor','marks')


admin.site.register(MarksRecord)
#@admin.register(MarksRecord)
#class AdminMarksRecord(admin.ModelAdmin):
#    list_display = ('id','student','Class','rollno','session','English_Obj_marks','Math_Obj_marks','Bio_Obj_marks','Phy_Obj_marks','Chem_Obj_marks','Science_Obj_marks','Urdu_Obj_marks','Pak_Obj_marks','Isl_Obj_marks','Comp_marks')

@admin.register(ExpenseRecords)
class AdminExpenseRecords(admin.ModelAdmin):
    list_display = ('id','Name','Amount','comment','Date')

admin.site.register(TeacherAttandance)