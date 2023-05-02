from django.shortcuts import render
from .models import Form 
from django.http import HttpResponse
# from fpdf import FPDF
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail




# Create your views here.

def index(request):
    return render(request,'index.html')


def home(request):
    id = request.POST['id']
    seller_name = request.POST['slrname']
    seller_phone = request.POST['slrphone']
    seller_email = request.POST['slremail']
    buyer_name = request.POST['byrname']
    buyer_email = request.POST['byremail']

    new_data = Form(id,seller_name,seller_phone,seller_email,buyer_name,buyer_email)

    
    new_data.save()

    send_mail('This is the confirmation mail',seller_name,'settings.EMAIL_HOST_USER',[buyer_email],fail_silently=False)
    

    if request.method == 'POST':
        # Get the form data from the request
        seller_name = request.POST.get('slrname')
        buyer_name = request.POST.get('byrname')
        id = request.POST.get('id')

        # Create a new PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        pdf_canvas = canvas.Canvas(response)
        
        # Add the submitted data to the PDF
        pdf_canvas.drawString(100, 750, 'Invoice Id: {}'.format(id))
        pdf_canvas.drawString(100, 700, 'Seller Name: {}'.format(seller_name))
        pdf_canvas.drawString(100, 650, 'Buyer Name: {}'.format(buyer_name))
        
        
        y = 600
        
        
        # Save the PDF and return the response
        pdf_canvas.save()
        
        return response
        
        
        
    return HttpResponse('<p>Data has been stored successfully</p>')
