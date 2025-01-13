from django.shortcuts import render,redirect,get_object_or_404
from .models import CandidateAddress,CandidateDetail,ParentsDetail,SiblingDetail,ReferenceDetail,GuardianDetail,StudentClass,Fee,FeeRecord,Teacher,StudentAttendence,Subjects,MarksRecord,ExpenseRecords,TeacherAttandance
from django.db.models import Q,Count,F 
from .forms import StudentUpdateForm,FeeRecordForm,TeacherForm,StudentAttendenceForm,SubjectForm,MarksRecordForm,FeeForm,ExpensesForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime as dt  
from django.db import IntegrityError
from django.db.models.functions import Lower, Trim
import datetime 
import calendar
#authi 

# Student related model..........
def home(request):
    return render(request,'students/index.html')

def RegisterStudent(request):
    if request.method == "POST":
        # Getting Student Information --------------------------
        studentfirstname = request.POST.get('firstname')
        studentlasttname = request.POST.get('lasttname')
        studentdateofbirth = request.POST.get('dob')
        studentclass = request.POST.get('class')
        studentgender = request.POST.get('gender')
        studentpob = request.POST.get('pob')
        studentnationality = request.POST.get('nationality')
        studentDOA = request.POST.get('DOA',None)
        studentfirstlang=request.POST.get('firstlang')
        studentotherlang = request.POST.get('otherlang')
        studentaddr = request.POST.get('addr')
        studentcity = request.POST.get('city')
        studentstate = request.POST.get('state')
        studentimg = request.FILES.get('image')

        # Saving data into database after getting from the form
        StudentDetailObj = CandidateDetail.objects.create(First_Name=studentfirstname,Last_Name=studentlasttname,Date_of_Birth=studentdateofbirth,Class=studentclass,Gender=studentgender,Place_of_Birth=studentpob,Nationality=studentnationality,First_Langugae=studentfirstlang,Date_of_Admission=studentDOA,other_Languages_known=studentotherlang,Student_Image=studentimg)
        StudentDetailObj.save()
        
        # saving data to candidateaddrres model 
        StudentAddressObject = CandidateAddress.objects.create(Address=studentaddr,city=studentcity,state=studentstate,student=StudentDetailObj)
        StudentAddressObject.save()
        
        fathername = request.POST.get('fathername')
        fatheemail = request.POST.get('femail')
        fqualification = request.POST.get('fqualification')
        fprofession = request.POST.get('fprofession')
        fdesignation = request.POST.get('fdesignation')
        fphone = request.POST.get('fphone')
        mothername = request.POST.get('mothername')
        memail = request.POST.get('memail')
        mqualification = request.POST.get('mqualification')
        mprofession = request.POST.get('mprofession')
        mdesignation = request.POST.get('mdesignation')
        mphone = request.POST.get('mphone')
       
        # Saving the data into model of ParentDetail
        ParentDetailObj = ParentsDetail(Father_Name=fathername,Father_Email=fatheemail,Father_Qualification=fqualification,Father_Profession=fprofession,Father_Designation=fdesignation,Father_Contact_No=fphone,Mother_Name=mothername,Mother_Email=memail,Mother_Qualification=mqualification,Mother_Profession=mprofession,Mother_Designation=mdesignation,Mother_Contact_No=mphone,student=StudentDetailObj)

        ParentDetailObj.save()


       # Guardian detail
        fullname = request.POST.get('fullname') 
        Gemail = request.POST.get('Gemail') 
        relation = request.POST.get('relation') 
        Gphone = request.POST.get('Gphone') 
        frelation = request.POST.get('frelation') 
        Srelation = request.POST.get('Srelation') 
        Sfirstnumber = request.POST.get('Sfirstnumber') 
        Ssecondnumber = request.POST.get('Ssecondnumber')

        # Saving into Guardian Model 
        GuardianDetailObj = GuardianDetail.objects.create(Full_Name=fullname,Email_Address=Gemail,Relation_with_student=relation,phone_no=Gphone,First_relation=frelation,Second_relation=Srelation,Number_one=Sfirstnumber,Number_two=Ssecondnumber,student=StudentDetailObj)

        GuardianDetailObj.save()


        # Sibling detail 
        Sibfullname = request.POST.get('Sibfullname')
        SibDOB = request.POST.get('SibDOB',None)
        Sibgender = request.POST.get('Sibgender')
        Sibclass = request.POST.get('Sibclass')
        Sibschool = request.POST.get('Sibschool')

        if SibDOB:
            pass
        else:
            SibDOB = None
        
        SibDetailObj = SiblingDetail.objects.create(Full_Name=Sibfullname,Date_of_Birth=SibDOB,Gender=Sibgender,Class=Sibclass,School=Sibschool,student=StudentDetailObj)

        SibDetailObj.save()
        
        
        # Second Sibling
        Sibfullname = request.POST.get('Sibfullnamesecond')
        SibDOB = request.POST.get('SibDOBsecond',None)
        Sibgender = request.POST.get('Sibgendersecond')
        Sibclass = request.POST.get('Sibclasssecond')
        Sibschool = request.POST.get('Sibschoolsecond')

        if SibDOB:
            pass
        else:
            SibDOB = None
        
        
        SibDetailObj = SiblingDetail.objects.create(Full_Name=Sibfullname,Date_of_Birth=SibDOB,Gender=Sibgender,Class=Sibclass,School=Sibschool,student=StudentDetailObj)

        SibDetailObj.save()
        
        # third Sibling
        Sibfullname = request.POST.get('Sibfullnamethird')
        SibDOB = request.POST.get('SibDOBthird',None)
        Sibgender = request.POST.get('Sibgenderthird')
        Sibclass = request.POST.get('Sibclassthird')
        Sibschool = request.POST.get('Sibschoolthird')
        
        if SibDOB:
            pass
        else:
            SibDOB = None
        
        SibDetailObj = SiblingDetail.objects.create(Full_Name=Sibfullname,Date_of_Birth=SibDOB,Gender=Sibgender,Class=Sibclass,School=Sibschool,student=StudentDetailObj)

        SibDetailObj.save()
        
        # fourth Sibling
        Sibfullname = request.POST.get('Sibfullnamefourth')
        SibDOB = request.POST.get('SibDOBfourth',None)
        Sibgender = request.POST.get('Sibgenderfourth')
        Sibclass = request.POST.get('Sibclassfourth')
        Sibschool = request.POST.get('Sibschoolfourth')
        
        if SibDOB:
            pass
        else:
            SibDOB = None
        
        SibDetailObj = SiblingDetail.objects.create(Full_Name=Sibfullname,Date_of_Birth=SibDOB,Gender=Sibgender,Class=Sibclass,School=Sibschool,student=StudentDetailObj)

        SibDetailObj.save()
        
        # fifth Sibling
        Sibfullname = request.POST.get('Sibfullnamefifth')
        SibDOB = request.POST.get('SibDOBfifth',None)
        Sibgender = request.POST.get('Sibgenderfifth')
        Sibclass = request.POST.get('Sibclassfifth')
        Sibschool = request.POST.get('Sibschoolfifth')
        
        # saving data
        if SibDOB:
            pass
        else:
            SibDOB = None
        
        SibDetailObj = SiblingDetail.objects.create(Full_Name=Sibfullname,Date_of_Birth=SibDOB,Gender=Sibgender,Class=Sibclass,School=Sibschool,student=StudentDetailObj)

        SibDetailObj.save()

        # Reference model getting data 
        refername = request.POST.get('refername')
        referaddress = request.POST.get('referaddress')
        referphone = request.POST.get('referphone')

        ReferenceDetailObj = ReferenceDetail.objects.create(Reference_Through=refername,Address=referaddress,Tell_No=referphone,student=StudentDetailObj)
        ReferenceDetailObj.save()


        return redirect('home')
    return render(request,'students/Addstudent.html')


# All students Records rendering to template via pagination 
def All_Student_Records(request):
    query = request.GET.get('q')
    if query ==None:
        students = StudentClass.objects.all().order_by('-id')
        paginator = Paginator(object_list=students,per_page=10,orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        students = StudentClass.objects.filter(Q(Full_Name__icontains=query) | Q(Roll_No__icontains=query) | Q(Class__icontains=query))
        pagninator = Paginator(object_list=students,per_page=10,orphans=1)
        page_number = request.GET.get('page')
        page_obj = pagninator.get_page(page_number)
    return render(request,"students/allrecords.html",{'page_obj':page_obj}) 


def UpdateRollNo(request,id):
    roll = StudentClass.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST,instance=roll)
        if form.is_valid():
            rollno = form.cleaned_data['Roll_No']
            Class = form.cleaned_data['Class']
            stuid = form.cleaned_data['student']
            fullname = form.cleaned_data['Full_Name']
            rollno = form.cleaned_data['Roll_No']
            gender = form.cleaned_data['Gender']
            Class = form.cleaned_data['Class']
            session = form.cleaned_data['session']
            
            try:
                stu = StudentClass.objects.get(Q(Roll_No=rollno) & Q(Class=Class))
                stu.Class=Class
                stu.Full_Name= fullname 
                stu.Gender=gender
                stu.session=session 
                stu.save()
                messages.add_message(request,messages.ERROR,"Already Asigned")
            except:
                form.save()
                messages.add_message(request,messages.SUCCESS,"Record Updated!")
            return redirect('allstudents')
            
    forms = StudentUpdateForm(instance=roll)
    return render(request,"students/updateform.html",context={"forms":forms})



def StudentDetail(request):
    query:str = request.GET.get('name')
    if query:
        query = query.split()
        first_name=query[0]
        last_name = query[-1]
    if query:
        student = CandidateDetail.objects.get(Q(First_Name=first_name)&Q(Last_Name=last_name))
    else:
        student = CandidateDetail.objects.all() 
    return render(request,'students/StudentDetail.html',{"student":student})



def PromoteStudents(request):
    if request.method == "POST":
        firstclass = request.POST.get('firstclass')
        secondclass= request.POST.get('secondclass')
        current_session = datetime.date.today().year 
        next_session = current_session+1
        try:
            students = StudentClass.objects.filter(Q(Class=firstclass) & Q(session=current_session))
           
            if firstclass == '10th':
                students.update(Class='Passed Out')
            else:
                students.update(Class=secondclass,session=next_session)
            return redirect('allstudents')
        except:
            messages.add_message(request,messages.ERROR,"Something Went Wrong Sorry")
    return render(request,"students/promotestudents.html")






# Add fees views 
def FeeRecordTable(request):
    fees = Fee.objects.all().order_by('id')
    feeform = FeeForm()
    return render(request,"students/Fee.html",context={"fees":fees,"feeform":feeform})



# Adding fees record functions
# Now Review the verifiation status of student existence while inserting the records and use the approach in which first of all reterive the students and then compare the credentials of students either it is true or not. 
def FeeRecords(request):
    current_date = datetime.date.today()
    current_month = calendar.month_name[current_date.month]
    if current_date.month == 1:
        previous_month = 12
        current_year = current_date.year 
    else:
        previous_month = current_date.month-1
        current_year = current_date.year 

    previous_month_name = calendar.month_name[previous_month]
    if request.method == 'POST':
        form = FeeRecordForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['Full_Name']
            fathername = form.cleaned_data['Father_Name']
            rollno = form.cleaned_data['Roll_No']
            Class = form.cleaned_data['Class']
            paid_date = form.cleaned_data['Paid_Date']
            if isinstance(paid_date,str):
                paid_date=datetime.date.fromisoformat(paid_date)
            year  = paid_date.year
            month = form.cleaned_data['Month']
            paid_amount = form.cleaned_data['Paid_Amount']
            dues = form.cleaned_data['Dues']
            tempsession = form.cleaned_data['session']

            
            try:
                StuRecord = get_object_or_404(StudentClass,Roll_No=rollno,Class=Class,session=tempsession)
                try:
                    StuObj = FeeRecord.objects.get(Q(Roll_No=rollno) & Q(Class=Class) & Q(Paid_Date__year=year)& Q(Month=month) &Q(session=tempsession))
                    messages.add_message(request,messages.ERROR,'Record Already Inserted')

                except:
                    try:
                        studentrecord = FeeRecord.objects.get(Q(Roll_No=rollno)&Q(Class=Class)&Q(Month=previous_month_name)&Q(session=tempsession))
                        dues = dues + studentrecord.Dues  
                        obj = FeeRecord.objects.create(Full_Name=fullname,Father_Name=fathername,Class=Class,session=tempsession,Roll_No=rollno,Month=month,Paid_Date=paid_date,Paid_Amount=paid_amount,Dues=dues)
                        obj.save()
                    except FeeRecord.DoesNotExist:
                        form.save()  
                    messages.add_message(request,messages.SUCCESS,"Fee Submited Successfully")
            except StudentClass.DoesNotExist:
                messages.add_message(request,messages.ERROR,"Invalid Credentials, Please Provide Correct Roll No,Name,Class")
            return redirect('feereport')
            
            
    form = FeeRecordForm()
    return render(request,'students/Addfees.html',{'form':form})

#update FeeRecord 

def UpdateFeeRecord(request,id):
    studentrecord = FeeRecord.objects.get(pk=id)
    if request.method == 'POST':
        form = FeeRecordForm(request.POST,instance=studentrecord)
        if form.is_valid():
            form.save()
            return redirect('feereport')
    else:
        form = FeeRecordForm(instance=studentrecord)
    return render(request,"students/Addfees.html",{"form":form})




def FeeRecReport(request):
    query = request.GET.get('q')
    if query:
        feereport = FeeRecord.objects.filter(Q(Roll_No__icontains=query)|Q(Full_Name__icontains=query)|Q(Class__icontains=query)|Q(Month__icontains=query))
    else:
        feereport = FeeRecord.objects.all() 
    return render(request,"students/FeeReport.html",{"feereport":feereport})


# Adding function to update Fee per class 
def AddFee(request):
    feeform = FeeForm()
    fee = Fee.objects.all()
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee')
        else:
            return render(request,'students/Fee.html',context={"feeform":feeform})
    return render(request,"students/Fee.html",context={"feeform":feeform,"fees":fee})  


# Update Fee Per Class data if needed:

def UpdateClassFee(request,id):
    feerecord = Fee.objects.get(pk=id)
    fee = Fee.objects.all()
    if request.method == "POST":
        form = FeeForm(request.POST,instance=feerecord)
        if form.is_valid():
            form.save()
            return redirect('fee')
        else:
            messages.add(request,messages.ERROR,f"Form Not Valid {form.errors}")
    else:
        feeform = FeeForm(instance=feerecord)
        return render(request,'students/updatefee.html',context={"feeform":feeform})

def FeeVoucher(request):
    query_class = request.GET.get('Class')
    query_month = request.GET.get('Month')
    query_year = dt.strptime(request.GET.get('date'),'%Y-%m-%d').year
    if query_month == 'January':
        query_year = query_year - 1
        query_month = 'December'
    Month_fee_per_class:int = Fee.objects.get(Class=query_class).Amount
    try:
        fee_records = FeeRecord.objects.filter(Q(Class=query_class) & Q(Month=query_month)& Q(Paid_Date__year=query_year))
        return render(request, 'students/vouchers.html', {'fee_records': fee_records,"Month_fee_per_class":Month_fee_per_class})
    except:
        messages.add(request,messages.ERROR,"Somthing is mising from records")

def CheckDefaulterstudent(request):
    class_ = request.GET.get('Class')
    current_month = datetime.date.today().month
    if current_month == 1:
        previous_month = 12
        previous_monnth_1 = 11
    else:
        previous_month = current_month-1
        previous_monnth_1 = previous_month - 1
    previous_month_name = calendar.month_name[previous_month]
    previous_monnth_1_name = calendar.month_name[previous_monnth_1]
    
    students_1 = FeeRecord.objects.filter(
    Q(Class=class_),
    Q(Paid_Amount=0),
    Q(Month=previous_month_name),
    Q(Paid_Date__year=datetime.date.today().year)).values_list('Roll_No', flat=True)

    students_2 = FeeRecord.objects.filter(
    Q(Class=class_)& Q(Paid_Amount=0)&Q(Month=previous_monnth_1_name)&Q(Paid_Date__year=datetime.date.today().year)).values_list('Roll_No', flat=True)
    
    common_roll_numbers = set(students_1).intersection(set(students_2))

    common_students = FeeRecord.objects.filter(Roll_No__in=common_roll_numbers,Class=class_,Month__in=[previous_month_name,previous_monnth_1_name]).values('Full_Name', 'Father_Name', 'Roll_No', 'Class','Month','session')

    
    context = {'students': common_students}        
    return render(request,"students/defaultstudents.html",context)

# Teacher related Portion 

def AddTeacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request,messages.SUCCESS,"Registered Successfully")
            except IntegrityError:
                messages.add_message(request,messages.ERROR,'This Teacher is Already registered')
            except Exception as e:
                messages.add_message(request,messages.ERROR,f"Error: {str(e)}")
            return redirect('addteacher')
    else:
        form = TeacherForm()
    return render(request,'students/AddTeacher.html',{"form":form})






# Attendence of Students on daily basis
def MarkAttendenceStudents(request):
    q = request.GET.get('q')
    if q:
        # current_session = datetime.date.today().year
        current_session = request.GET.get('session')
        students = StudentClass.objects.filter(Q(Class=q) & Q(session=current_session))
        if request.method == 'POST':
            for student in students:
                status = request.POST.get(f'status_{student.id}')
                StudentAttendence.objects.create(
                    Full_Name=student.Full_Name,
                    Class=student.Class,
                    Father_Name= student.Father_Name,
                    Roll_No=student.Roll_No,
                    Date=datetime.date.today(),
                    status=status
                )
            return redirect('allstudents')  # Redirect to a success page or the same page with a success message
        context = {'students': students,'date':datetime.date.today()}
        return render(request, "students/Attendence.html", context)
    else:
        return render(request, "students/Attendence.html")
    
def AttendanceReport(request):
    context = dict()
    context_total = dict()
    current_date = request.GET.get('current_date')
    #current_date = datetime.date.today()
    CLASSES = ['Nursery','Prep','One','Two','Three','Four','Five','Six','Eight','9th','10th']
    try:
        for class_ in CLASSES:
            context_total[f'{class_}'] = list()
            context_total[f'{class_}'].append(StudentClass.objects.filter(Class=class_).count())
            context_total[f'{class_}'].append(StudentAttendence.objects.filter(Q(Class=class_) & Q(status='P') & Q(Date=current_date)).count())
            context_total[f'{class_}'].append(StudentAttendence.objects.filter(Q(Class=class_) & Q(status='A') & Q(Date=current_date)).count())
            context_total[f'{class_}'].append(StudentAttendence.objects.filter(Q(Class=class_) & Q(status='L') & Q(Date=current_date)).count())
        
        context['context_total'] = context_total
    except:
        messages.add_message(request,messages.ERROR,'Mark the attendence First')

    return render(request,'students/AttendanceReport.html',context)

def AttendanceStatics(request):
    Class= request.GET.get('Class')
    current_date = request.GET.get('current_date')
    status = request.GET.get('status')
    context = {}
    try:
        studentrecord = StudentAttendence.objects.filter(Q(Class=Class)& Q(Date=current_date) & Q(status=status))
        if len(studentrecord) == 0:
            messages.add_message(request,messages.ERROR,'Mark The Attendance First')       
        context["students"] = studentrecord 
    except:
        messages.add_message(request,messages.ERROR,'Class Does Not Exists')
    return render(request,"students/AttendanceReport.html",context)

# Percentage Attandence
def StudentPercentage(request):
    Class = request.GET.get('Class')
    current_date = request.GET.get('current_date')
    first_date = datetime.date.today().replace(day=1)
    attendance_records = StudentAttendence.objects.filter(Date__range=[first_date,current_date],status='P',Class=Class).values('Roll_No').annotate(present_count=(Count('id')))
    context = {}
    for student in attendance_records:
        context[f'{student['Roll_No']}']=[]
        context[f'{student['Roll_No']}'].append(student['Roll_No'])
        context[f'{student['Roll_No']}'].append(StudentClass.objects.get(Q(Roll_No=student['Roll_No'])&Q(Class=Class)).Full_Name)
        context[f'{student['Roll_No']}'].append(StudentClass.objects.get(Q(Roll_No=student['Roll_No'])&Q(Class=Class)).Father_Name)
        context[f'{student['Roll_No']}'].append(round(((student['present_count']/datetime.date.today().day)*100),2))
        context[f'{student['Roll_No']}'].append(Class)
        context[f'{student['Roll_No']}'].append(datetime.date.today().year)
 
   
    return render(request,'students/percentagedetail.html',{"detail":context})




def deletestudent(request,id):
    student = StudentClass.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('allstudents')
    return render(request,'students/delete.html',{"obj":student})


def AllTeachersRecords(request):
    query = request.GET.get('q')
    context = {}
    if query:
        teachers = Teacher.objects.filter()
        
        paginator = Paginator(object_list=teachers,per_page=10,orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj']=page_obj
    else:
        teachers = Teacher.objects.all()
        paginator = Paginator(object_list=teachers,per_page=10,orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] =page_obj
    return render(request,'students/allteachersrecord.html',context)


def deleteteachers(request,id):
    teacher = Teacher.objects.get(pk=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('allteachers')
    return render(request,'students/delete.html',{"obj":teacher})

def TeacherDetail(request):
    query = request.GET.get('name')
    context = dict()
    if query:
        try:
            teacher = Teacher.objects.get(Full_Name__icontains=query)
            context["teacher"]=teacher
        except:
            messages.add_message(request,messages.ERROR,'Sorry Invalid Name')
    return render(request,"students/Teacherdetails.html",context)


# Subject portion 

def Subject(request):
    subjects = Subjects.objects.all()
    return render(request,"students/subjects.html",context={"subjects":subjects})

# add subject 
def AddSubject(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        subject = request.POST.get('subject')
        teacher = Teacher.objects.get(Cnic=request.POST.get('teacher'))
        mark = request.POST.get('marks')
        class_ = request.POST.get('class')
        SubObj = Subjects.objects.create(title=subject,Class=class_,tutor=teacher,marks=mark)
        SubObj.save()
        return redirect('subjects')
    return render(request,"students/Addsubject.html",{"teachers":teachers})


# update subject
def UpdateSubject(request,id):
    updatesubjectcall = Subjects.objects.get(pk=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST,instance=updatesubjectcall)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm(instance=updatesubjectcall)
    return render(request,"students/subjects.html",{"form":form,"updatesubjectcall":True})


# Accounts portion 
def Accounts(request):
    Total_students = StudentClass.objects.all().count()
    Total_teachers = Teacher.objects.all().count()
    Records = FeeRecord.objects.filter(Month=calendar.month_name[datetime.date.today().month])
    expenserecords = ExpenseRecords.objects.filter(Date__month=datetime.date.today().month)
    Total_fee:int = 0
    
    for record in Records:
        fee = record.Paid_Amount 
        Total_fee+=fee

    return render(request,"students/Totalincome.html",{"Total_students":Total_students,"Total_teachers":Total_teachers,"Total_fee":Total_fee,"records":expenserecords})

# Peding Dues of This Month 
def PendingDues(request):
    current_month = calendar.month_name[datetime.date.today().month]
    class_ = request.GET.get('Class')
    all_students = StudentClass.objects.filter(Class=class_)
    paid_students= FeeRecord.objects.filter(Q(Class=class_) & Q(Month=current_month)& Q(Paid_Date__year=datetime.date.today().year)).exclude(Paid_Amount=0).values_list('Full_Name',flat=True)
    Not_paid_students = all_students.exclude(Full_Name__in=paid_students)
    return render(request,"students/pendingdues.html",{"students":Not_paid_students})


# Exam portion 

def AddExam(request):
    subjects = Subjects.objects.all()
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        class_ = request.POST.get('class')
        rollno = request.POST.get('rollno')
        session = request.POST.get('session')
        eng = request.POST.get('eng')
        math = request.POST.get('math')
        bio = request.POST.get('Bio')
        sci = request.POST.get('Sci')
        phy = request.POST.get('Phy')
        com = request.POST.get('com')
        chem = request.POST.get('chem')
        pak = request.POST.get('pak')
        isl = request.POST.get('isl')
        urdu = request.POST.get('urdu')
        try:
            StuObj = StudentClass.objects.get(Q(Roll_No=rollno)&Q(Class=class_)&Q(Full_Name=fullname))
            if StuObj is not None:
                
                if class_ == '9th' or class_ =='10th':
                    Student = MarksRecord(student=StuObj,Class=class_,rollno=rollno,session=StuObj.session,English_Obj_marks=eng,Math_Obj_marks=math,Bio_Obj_marks=bio,Phy_Obj_marks=phy,Chem_Obj_marks=chem,Science_Obj_marks=sci,Urdu_Obj_marks=urdu,Pak_Obj_marks=pak,Isl_Obj_marks=isl,Comp_marks=com)
                    Student.save()
                else:
                    Student = MarksRecord(student=StuObj,Class=class_,rollno=rollno,session=StuObj.session,English_Obj_marks=eng,Math_Obj_marks=math,Science_Obj_marks=sci,Urdu_Obj_marks=urdu,Pak_Obj_marks=pak,Isl_Obj_marks=isl)
                    Student.save()
                return redirect('home')
        except StudentClass.DoesNotExist:
            messages.add_message(request,messages.ERROR,"Student Does Not Exists or invalid credentials")
        except Exception as e:
            messages.add_message(request,messages.ERROR,f"Something Went Wrong {e}") 

        return redirect("addexam")
    return render(request,"students/Addexam.html")

# Show marks 

def ShowMarksRecord(request):
    class_ = request.GET.get('class')
    records = MarksRecord.objects.filter(Class=class_)
    sub = Subjects.objects.filter(Class=class_)
    total:int = 0
    for mark in sub:
        total += mark.marks 
    return render(request,"students/Showmarks.html",{"records":records,"Total_marks":total})


## Expenses Related Records...
def ExpensesManagement(request):
    form = ExpensesForm()
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    else:
        return render(request,"students/expsenses.html",{"form":form})
    
def UpdateExpense(request,id):
    record = ExpenseRecords.objects.get(pk=id)
    if request.method == "POST":
        form = ExpensesForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    else:
        form = ExpensesForm(instance=record)
        return render(request,"students/expsenses.html",{"form":form})
    
def TeacherAttendanceModule(request):
    all_records = Teacher.objects.all()
    if request.method == 'POST':
        for teacher in all_records:
                status = request.POST.get(f'status_{teacher.Cnic}')
                TeacherAttandance.objects.create(
                    Full_Name=teacher.Full_Name,
                    Father_Name= teacher.Father_Name,
                    Cnic=teacher.Cnic,
                    Date=datetime.date.today(),
                    status=status
                )
    return render(request,"students/TeacherAttendance.html",{"teachers":all_records,"date":datetime.date.today(),"choice":"Markattendance"})

def TeacherAttenaceReport(request):
    context_total = dict()
    current_date = datetime.date.today()
    context_total['Total']=TeacherAttandance.objects.all().count()
    context_total['Present']=TeacherAttandance.objects.filter(Q(status='P') & Q(Date=current_date)).count()
    context_total['Absent']=TeacherAttandance.objects.filter(Q(status='A') & Q(Date=current_date)).count()
    context_total['Leave']=TeacherAttandance.objects.filter(Q(status='L') & Q(Date=current_date)).count()
    return render(request,"students/TeacherAttendance.html",context_total)

def TeacherAttendancestatistics(request):
    current_date = request.GET.get('current_date')
    status = request.GET.get('status')
    context = {}
    try:
        teacherrecord = TeacherAttandance.objects.filter(Q(Date=current_date) & Q(status=status))
        if len(teacherrecord) == 0:
            messages.add_message(request,messages.ERROR,'Mark The Attendance First')       
        context["teachers"] = teacherrecord 
    except:
        messages.add_message(request,messages.ERROR,'Class Does Not Exists')
    return render(request,"students/TeacherAttendance.html",context)
