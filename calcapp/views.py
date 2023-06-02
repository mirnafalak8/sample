from django.shortcuts import render

# Create your views here.
def loadcalculator(request):
    return render(request,'calculator.html')

def calc(request):
    c=''
    try:
        if request.method=='POST':
            n1= int(request.POST.get('num1'))
            n2= int(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                c=n1+n2

            elif opr=="-":
                c=n1-n2

            elif opr=="*":
                c=n1*n2

            elif opr=="/":
                c=n1/n2
    except:
        c="invalid operation"
    print(c)
    return render(request,'calculator.html',{'result':c})