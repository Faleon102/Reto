from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = '1M6KB8fRL3tncZaoPBdGY4OusPvq6xYlI' #Id de la carpeto Reto en mi drive

carpetas = ['Hola', 'Chao']

'''for carpeta in carpetas:
    file_metadata = {
        'name': carpeta,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [folder_id] 
    }

    service.files().create(body=file_metadata).execute()'''

#file_names = ['inserte documento', '']
file_names = ['out-transparent-29.gif', 'Piedras de Barenziah.docx', 'Teri1.jpg']
#mine_types = ['tipo de documento','']
mime_types = ['image/gif','application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/jpeg']

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

