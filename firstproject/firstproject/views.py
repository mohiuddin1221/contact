from django.shortcuts import render,redirect
from tuition.models import contact
def home(request):
    names = ['Mohiuddin', 'Ahhmmed', 'Topu']
    context = {
        'names': names,
    }
    return render(request, 'home.html', context)

#from django.shortcuts import render, 

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        description = request.POST['description']
        
        print(name)
        print(number)
        print(description)
        return redirect('contact')  # Redirect to a success page after processing the form
        obj = contact(name=name,number= number,description= description)
        obj.save()
    return render(request, 'contact.html')

