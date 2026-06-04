import PyPDF2
import io

def extract_text_from_pdf(file_bytes:bytes) -> str:
#func that takes raw pdf bytes, returns text string
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    #convert raw bytes into something pypdf2 can read

    
    text = ""
    #start with empty string, we'll add to it

    for page in pdf_reader.pages:
        text+= page.extract_text()
    #loop through every page and add the text to our string

    return text
    #return the full text of the resume as a string