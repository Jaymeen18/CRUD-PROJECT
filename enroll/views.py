from django.shortcuts import render,HttpResponseRedirect
from .forms import Student_Registrations
from .models import User
from django.db.models import Avg,Sum,Count,Min,Max
from django.db.models import Q

# Create your views here.               

#This function will add new item and show all items
def add_show(request):
    if request.method=='POST':
        student_object=Student_Registrations(request.POST)
        if student_object.is_valid():
            name=student_object.cleaned_data['name']
            email=student_object.cleaned_data['email']
            password=student_object.cleaned_data['password']
            user_object=User(name=name,email=email,password=password)
            user_object.save()
            student_object=Student_Registrations()
    else:
        student_object=Student_Registrations()
    data_queryset=User.objects.all()
    # data_queryset=User.objects.filter(name__startswith='f')
    return render(request,'enroll/addandshow.html',{'form':student_object,'student_data':data_queryset})

#This Function will Update
def update_data(request,id):
    if request.method=='POST':
        update_user=User.objects.get(id=id)
        student_object=Student_Registrations(request.POST,instance=update_user)
        if student_object.is_valid():
            student_object.save()
            return HttpResponseRedirect('/')
    else:
        update_user=User.objects.get(id=id)
        student_object=Student_Registrations(instance=update_user)
    return render(request,'enroll/updatestudent.html',{'form':student_object})


#This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        delete_user=User.objects.get(id=id)
        delete_user.delete()
        return HttpResponseRedirect('/')
    return


def showdata(request):
    # student_data = User.objects.all()
    # student_data = User.objects.filter(name__startswith='j')
    # student_data = User.objects.exclude(name__startswith='j')
    # student_data = User.objects.order_by('id')
    # student_data = User.objects.order_by('-name')
    # student_data = User.objects.order_by('?')
    # student_data = User.objects.order_by('id').reverse()[:5]
    # student_data = User.objects.values('name','email')
    # student_data = User.objects.values_list('id','name',named=True)
    # student_data = User.objects.using('default')


    # student_data = User.objects.get(pk=10)
    # student_data = User.objects.first()
    # student_data = User.objects.last()
    # student_data = User.objects.latest('current_date')
    # student_data = User.objects.earliest('password')
    # student_data = User.objects.dates('current_date','month')
    # student_data = User.objects.create(name='bhargav',email='bhargav@gmail.com',password = '123789')
    # student_data,created = User.objects.get_or_create(name='bhargavi',email='bhargavi13@gmail.com',password = '123789')
    # student_data = User.objects.filter(id =30).update(email='bhargavi12@gmail.com')  
    # student_data = User.objects.update_or_create(id=30,name ='bhargavi') 


    # objs = [
    #     User(name='mehul',email='mehul@gmail.com',password = '1111111'),
    #     User(name='raghav',email='raghav@gmail.com',password = '2222222'),
    #     User(name='tonny',email='tonny@gmail.com',password = '3333333'),
    # ]  
    # student_data = User.objects.bulk_create(objs)


    # student_data = User.objects.filter(name__exact='keval')
    # student_data = User.objects.filter(name__contains='A')
    # student_data = User.objects.filter(name__icontains='A')
    # student_data = User.objects.filter(id__in=[40,42])
    # student_data = User.objects.filter(name__in=['jaymeen','jaydeep','mehul'])
    # student_data = User.objects.filter(id__gte=42)
    # student_data = User.objects.filter(id__lte=42)
    # student_data = User.objects.filter(password__startswith=2)
    # student_data = User.objects.filter(password__endswith=0)


    student_data = User.objects.all()
    # average = student_data.aggregate(Avg('password'))
    # count = student_data.aggregate(Count('password'))
    # max = student_data.aggregate(Max('password'))
    # min = student_data.aggregate(Min('password'))
    # sum = student_data.aggregate(Sum('password'))
    # print('averageaaaaaaaaaaaaa: ', average)


    ans = student_data.annotate(Count('password'))
    context = {'student_data':ans}

    # context = {'student_data':student_data,'average':average,'count':count,'max':max,'min':min,'sum':sum}



    # student_data = User.objects.filter( Q(id=42) & Q(name='jaymeen') )
    # student_data = User.objects.filter( Q(id=42) |  Q(name='jaymeen') )
    # student_data = User.objects.filter(~Q(id=42))

    # student_data = User.objects.all()[:6:2]

    # student_data = User.objects.get(id=37)
    # print('student_data: ', student_data)
    # print('aaaaaaaaaaaa',student_data.query)
    return render(request,'enroll/showdata.html',context)