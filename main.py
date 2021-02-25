#Fabian Enrique Leon Junco - 20171020015
#Diego Nicolas Ramos Zamudio - 20181020167
#HÉCTOR DAVID ALEJANDRO PACHECO MORA - 20182020012

#Importar libreriar
import os
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

#Recibir credenciales
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = '1M6KB8fRL3tncZaoPBdGY4OusPvq6xYlI' #Id de la carpeta Reto en mi drive


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./Documentos"

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/crear/<nombre>")
def Crear(nombre):
    Files = [nombre]
    for Files in Files:
        file_metadata ={
            'name': Files,
            'mimeType' : 'application/vnd.google-apps.folder',
            'parents': [folder_id] 
        }
        service.files().create(body=file_metadata).execute()
    return "Carpeta creada"

@app.route('/subido',methods = ['POST'])
def subir():
   if request.method == 'POST':
       f = request.files['archivo']
       filename = secure_filename(f.filename)
       f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

       file_names = [filename]
       mime_types = ['image/gif','application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
       'image/jpeg', 'application/zip', 'application/pdf', 'image/png', '	application/vnd.ms-excel', 'application/msword', 
       'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
       
       for file_name, mime_type in zip(file_names, mime_types):
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
            }
            media = MediaFileUpload('./Documentos/{0}'.format(file_name), mimetype=mime_type)
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
       return "Archivo subido"


if __name__ == '__main__':
   app.run(debug = True)


