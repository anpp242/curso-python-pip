import os
import shutil

extensions_dict = {
    '.txt':'documentos',
    '.docx': 'documentos',
    '.pdf': 'documentos',
    '.xls': 'documentos',
    '.xlsx': 'documentos',
    '.ppt': 'documentos',
    '.pptx': 'documentos',
    '.jpg': 'imagenes',
    '.jpeg': 'imagenes',
    '.svg': 'imagenes',
    '.py': 'scripts',
    '.png': 'imagenes',
    '.gif': 'imagenes',
    '.webp': 'imagenes',
    '.mp3': 'audio',
    '.wav': 'audio',
    '.dmg': 'instaladores',
    '.zip': 'compress',
    '.tgz': 'compress',
    '.app': 'apps',
    '.csv': 'csv',
}

default = 'otros'
file_organizer_path = r'/Users/omarpava/Downloads'

files_path = os.listdir(file_organizer_path)

#cicle all files in the files_organizer_path
for file in files_path:
    origin_file = os.path.join(file_organizer_path, file)
    if os.path.isfile(origin_file):
        _, extension =  os.path.splitext(file)
        file_name = extensions_dict.get(extension.lower(), default)
        destination_file = os.path.join(file_organizer_path, file_name)

        if not os.path.exists(destination_file):
            os.makedirs(destination_file)

        shutil.move(origin_file, destination_file)