from fpdf import FPDF
from gtts import gTTS
import os
from tempfile import TemporaryFile
#from urllib.request import urlopen
import urllib.request

def create_pdf(list_of_results,id_wcw):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=30)
    pdf.set_text_color(255,0,0)  
    pdf.cell(2, 10, txt= "Not for official purposes", ln=100, align = "l")
    heading_text =  "Wine lands collage academic record for student: " + str(id_wcw)
    pdf.set_font("Arial", size=20)
    pdf.set_text_color(0,0,0) 
    pdf.cell(2, 20, txt=heading_text , ln=100, align = "l")
    pdf.set_font("Arial", size=20)
    pdf.set_text_color(0,0,0) 
    for mark in list_of_results:
        pdf.cell(2, 10, txt= mark, ln=100, align = "l")
    pdf.output("Academic_Transcript_"+str(id_wcw)+".pdf")

def create_audio(ist_of_results,id_wcw):
    convert = "For sudent " + str(id_wcw) + " here are the results."
    for i in ist_of_results:
        convert+= " " + i + " "
    tts = gTTS(text=convert, lang='en')
    tts.save(str(id_wcw)+"_marks.mp3")

def delete_used(id):
    os.remove("Academic_Transcript_"+str(id)+".pdf")
    os.remove(str(id)+"_marks.mp3")
#Call this
def check_internet():
    try:
        url = "http://www.google.com/"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        response.read()
        return True
    except:
        return False 



# create_pdf(['E&I\t\t75%','Maths\t\t60%', "CS\t\t60%", 'Looking at Andrew\t\t90%'],69)
# create_audio(['E&I\t\t75%','Maths\t\t60%', "CS\t\t60%", 'Looking at Andrew\t\t90%'],69)
# delete_used(69)
print(check_internet())



