from django.http.response import FileResponse, HttpResponse
from django.shortcuts import render
import mysql.connector
from fpdf import FPDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


# Create your views here.

def index(request):
    return render(request, 'index.html')

def certi(request):
    if request.method == 'POST':
        data=request.POST
        email=data['email']
        suggestion=data['suggestion']
        city=data['city']
        rating=data['rating']
        
        try:
            db= mysql.connector.connect(
            host='remotemysql.com',
            user="Q5YBGRz5jD",
            password='Fkw1X5TztF',
            port='3306',
            database="Q5YBGRz5jD"
           )
            try:
                cur=db.cursor()
                cur.execute("SELECT * FROM ead_2020 WHERE ead_2020.email=%s AND ead_2020.place=%s",(email,city))
                info=cur.fetchall()
                print(info)


                if info:
                    name=info[0][0]
                    date=info[0][2]
                    # return render(request, 'certi.html',{'email':email,'desc':desc,'city':city,'rating':rating})
                    pdf = FPDF()  
                    pdf.add_font('RealityPress','','static/font/Facile Sans.ttf',uni=True);
                    pdf.add_page("L")
                    pdf.image('static\images\ead_certificate.jpg', x=10, y=8, w=275)
                    pdf.set_font("RealityPress", size=18)
                    pdf.ln(74)
                    if len(name)>25:
                        pdf.set_font("RealityPress", size=12)

                        pdf.cell(1,10.5,name.rjust(130," "),0,1)
                        pdf.set_font("RealityPress", size=18)

                        pdf.ln(1)
                    else:
                        
                        pdf.cell(1,11,name.rjust(89," "),0,1)   
                        pdf.ln(1) 

                    pdf.cell(1,3,city.rjust(95," "),0,1)
                    pdf.ln(2)
                    pdf.cell(1,8,date.rjust(52," "),0,1)
                    cur.execute("UPDATE ead_2020 SET ead_2020.suggestion=%s,ead_2020.rating = %s WHERE ead_2020.email=%s AND ead_2020.place=%s ", (suggestion, rating,email,city))
                    db.commit()
                    pdf.output('certi.pdf', 'F')
                    x=open('certi.pdf', 'rb')
                    return FileResponse(x,  content_type='application/pdf')#as_attachment=True,
                else:
                    context={'error':'Invalid Email or City'}
                    return render(request, 'certi.html',context)    
            except Exception as e:
                print(e)

                return render(request, 'certi.html',{'error',e})
                
        except Exception as e:
            print(e)

            return render(request, 'certi.html',{'error',e})
        
    else:
        return render(request, 'index.html')

def PILcerti(request):
    if request.method == 'POST':
        data=request.POST
        email=data['email']
        suggestion=data['suggestion']
        city=data['city']
        rating=data['rating']
        
        try:
            db= mysql.connector.connect(
            host='remotemysql.com',
            user="Q5YBGRz5jD",
            password='Fkw1X5TztF',
            port='3306',
            database="Q5YBGRz5jD"
           )
            try:
                cur=db.cursor()
                cur.execute("SELECT * FROM ead_2020 WHERE ead_2020.email=%s AND ead_2020.place=%s",(email,city))
                info=cur.fetchall()
                print(info)


                if info:
                    name=info[0][0]
                    date=info[0][2]
                    templateCert = ImageReader('static\images\ead_certificate.jpg')
                    buffer = io.BytesIO()

                    # Create the PDF object, using the buffer as its "file."
                    p = canvas.Canvas(buffer)

                    # Draw things on the PDF. Here's where the PDF generation happens.
                    # See the ReportLab documentation for the full list of functionality.
                    p.drawImage(templateCert, 10, 350, mask='auto')
                    p.drawString(100, 350, "Hello world.")

                    # Close the PDF object cleanly, and we're done.
                    p.showPage()
                    p.save()

                    # FileResponse sets the Content-Disposition header so that browsers
                    # present the option to save the file.
                    buffer.seek(0)
                    return FileResponse(buffer, filename='hello.pdf')
                    # return render(request, 'certi.html',{'email':email,'desc':desc,'city':city,'rating':rating})
                    # pdf = FPDF()  
                    # pdf.add_font('RealityPress','','static/font/Facile Sans.ttf',uni=True);
                    # pdf.add_page("L")
                    # pdf.image('static\images\ead_certificate.jpg', x=10, y=8, w=275)
                    # pdf.set_font("RealityPress", size=18)
                    # pdf.ln(74)
                    # if len(name)>25:
                    #     pdf.set_font("RealityPress", size=12)

                    #     pdf.cell(1,10.5,name.rjust(130," "),0,1)
                    #     pdf.set_font("RealityPress", size=18)

                    #     pdf.ln(1)
                    # else:
                        
                    #     pdf.cell(1,11,name.rjust(89," "),0,1)   
                    #     pdf.ln(1) 

                    # pdf.cell(1,3,city.rjust(95," "),0,1)
                    # pdf.ln(2)
                    # pdf.cell(1,8,date.rjust(52," "),0,1)
                    # cur.execute("UPDATE ead_2020 SET ead_2020.suggestion=%s,ead_2020.rating = %s WHERE ead_2020.email=%s AND ead_2020.place=%s ", (suggestion, rating,email,city))
                    # db.commit()
                    # pdf.output('certi.pdf', 'F')
                    # x=open('certi.pdf', 'rb')
                    # return FileResponse(x,  content_type='application/pdf')#as_attachment=True,
                else:
                    context={'error':'Invalid Email or City'}
                    return render(request, 'certi.html',context)    
            except Exception as e:
                print(e)

                return render(request, 'certi.html',{'error',e})
                
        except Exception as e:
            print(e)

            return render(request, 'certi.html',{'error',e})
        
    else:
        return render(request, 'index.html')
