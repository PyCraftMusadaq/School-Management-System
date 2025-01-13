from django import forms 
from .models import CandidateAddress,CandidateDetail,ParentsDetail,ReferenceDetail,GuardianDetail,SiblingDetail,StudentClass,FeeRecord,Teacher,StudentAttendence,Subjects,MarksRecord,Fee,ExpenseRecords


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateDetail
        fields = '__all__'


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = '__all__'
        labels = {'Full_Name':"Name"}
        widgets = {'student':forms.TextInput(attrs={'class':"inputfield"}),'Roll_No':forms.TextInput(attrs={'class':"inputfield"}),'Full_Name':forms.TextInput(attrs={'class':"inputfield"}),'Gender':forms.TextInput(attrs={'class':"inputfield"}),'Class':forms.TextInput(attrs={'class':"inputfield"}),'session':forms.NumberInput(attrs={'class':'inputfield'})}
        


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = '__all__'
        exclude = ['student']
        widgets = {
            'Full_Name': forms.TextInput(attrs={'class': 'inputfield'}),
            'Father_Name': forms.TextInput(attrs={'class': 'inputfield'}),
            'Class': forms.Select(attrs={'class': 'inputfield'}),
            'session': forms.TextInput(attrs={'class': 'inputfield'}),
            'Month': forms.Select(attrs={'class': 'inputfield'}),  # Use Select widget for ChoiceField
            'Paid_Date': forms.DateInput(attrs={'class': 'inputfield', 'type': 'date'}),  # Use DateInput widget for DateField
            'Paid_Amount': forms.NumberInput(attrs={'class': 'inputfield'}),  # Use NumberInput widget for IntegerField
            'Roll_No': forms.NumberInput(attrs={'class': 'inputfield'}),
            'Dues': forms.NumberInput(attrs={'class': 'inputfield'}),  # Use NumberInput widget for IntegerField
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher 
        fields = '__all__'
        widgets = {
            'Cnic':forms.TextInput(attrs={'class':'inputfield'}),
            'Full_Name':forms.TextInput(attrs={'class':'inputfield'}),
            'Father_Name':forms.TextInput(attrs={'class':"inputfield"}),
            'Education':forms.TextInput(attrs={'class':'inputfield'}),
            'Degree_Image':forms.ClearableFileInput(attrs={'class':'inputfield'}),
            'Profile_Image':forms.ClearableFileInput(attrs={'class':"inputfield"}),
            'contact':forms.TextInput(attrs={'class':'inputfield'}),
            'Address':forms.TextInput(attrs={'class':"inputfield"}),
            'Home_contact':forms.TextInput(attrs={'class':"inputfield"}),
        }



# Attendence Form 
class StudentAttendenceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendence
        fields = '__all__'
        widgets = {
            'Full_Name':forms.TextInput(attrs={'class':'inputfield'}),
            'Father_Name':forms.TextInput(attrs={'class':"inputfield"}),
            'Class':forms.TextInput(attrs={'class':'inputfield'}),
            'Roll_No':forms.NumberInput(attrs={'class':"inputfield"}),
            'Date':forms.DateInput(attrs={'class':"inputfield","type":"date"}),
            'status':forms.Select(attrs={'class':"inputfield"}),
        }



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'
        widgets = {
        'title':forms.TextInput(attrs={'class':'inputfield'}),
        'tutor':forms.Select(attrs={'class':'inputfield'}),
        'marks':forms.NumberInput(attrs={'class':"inputfield"}),
        }


class MarksRecordForm(forms.ModelForm):
    class Meta:
        model = MarksRecord
        fields = "__all__"
        widgets = {
            'student':forms.TextInput(attrs={'class':'inputfield'}),
            'Class':forms.TextInput(attrs={'class':'inputfield'}),
            'rollno':forms.NumberInput(attrs={'class':'inputfield'}),
            'session':forms.NumberInput(attrs={'class':"inputfield"}),
            'English_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Math_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Bio_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Phy_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Chem_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Science_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Urdu_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Pak_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Isl_Obj_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            'Comp_marks':forms.NumberInput(attrs={'class':'inputfield'}),
            
        }


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        widgets = {
            'Amount':forms.NumberInput(attrs={"class":"inputfield"})
        }
    Class = forms.ChoiceField(
        choices=[
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
        ],
        widget=forms.Select(attrs={'class': "inputfield"})
    )



## expense related forms 

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = ExpenseRecords
        fields = '__all__'
        widgets = {
            'Name':forms.TextInput(attrs={'class':"inputfield"}),
            'Amount':forms.NumberInput(attrs={'class':"inputfield"}),
            'comment':forms.TextInput(attrs={'class':"inputfield"}),
            'Date':forms.DateInput(attrs={'class':"inputfield","type":"date"}),
        }