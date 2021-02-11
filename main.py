import PyPDF2
from io import BytesIO

def extract_stream(file):

    base = './dataset/'
    path = f'{base}{file}'

    pdf = PyPDF2.PdfFileReader(path)
    page = pdf.getPage(0)
    content = page.getContents()
    content.getObject()

    if isinstance(content, list):
        data = b''
        for c in content:
            data += c.getObject().getData()
        return BytesIO(data)

    return BytesIO(content.getData())

def export_to_txt(stream, filename='output.txt'):

    with open(filename, 'w') as file:
        for line in stream.readlines():
            file.write(line.decode('utf-8').strip()+'\n')
    file.close()

if __name__ == '__main__':

    # pdf generated via microsoft word (save as)
    stream = extract_stream('example-via-save-as.pdf')
    export_to_txt(stream, 'example-via-save-as.txt')

    # pdf generated via print to pdf (ctrl + p)
    stream = extract_stream('example-via-print-to-pdf.pdf')
    export_to_txt(stream, 'example-via-print-to-pdf.txt')
