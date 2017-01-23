from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.shortcuts import redirect
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this


# Create your views here.

#def upload(request):
 #   if request.method == 'POST':
  #      r = request.POST.get('webcam')
   # return HttpResponse("Do something")

    #datauri = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='

 #   imgstr = re.search(r'base64,(.*)', r).group(1)

  #  output = open('output.png', 'wb')

   # output.write(imgstr.decode('base64'))

    #output.close()

    #return render(request, 'app/upload.html')

 
@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def upload(request):
  
    return render(request, 'app/upload.html')

def home(request):
    return render(request, 'app/index.html' )
