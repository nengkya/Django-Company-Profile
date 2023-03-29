from django.shortcuts import render

def index(request):
    context={
        'title':'Solution',
        'heading':'Build and customize your project here',
        'subheading':'Your dificulty is our challanges, HaGa IT Solution is always here to make your software and digital electronic project come true.',
    }

    return render(request,'index.html',context)
