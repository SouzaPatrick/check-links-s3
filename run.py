# -*- coding: utf-8 -*-

from script_csv import CSV_Read, CSV_Write
from web_scraping import WebScraping
from utils import FileUtils


folderRead = 'base_csv'
filename = 'november.csv'

fileUtils = FileUtils()
pathFile = fileUtils.join_path_filename(filename=filename, baseFolder=folderRead)

#Verifica se o arquivo existe dentro da pasta
if fileUtils.exist_file_folder(pathFile):
    print(f'O arquivo que esta sendo lido é: {filename}')
    csvRead = CSV_Read(pathFile)
    listReader = csvRead.read_file()

    webscraping = WebScraping()

    dictSuccesS3 = {}
    dictErrosS3 = {}
    dictInvalid = {}
    dictBlanck = {}

    for item in listReader:
        linkType, link, course, message = webscraping.scraping(link=item['LINK'], course=item['CURSO'])

        if linkType == 'success':
            dictSuccesS3 = webscraping.organize_scarping_of_dict(dictOfficial=dictSuccesS3, course=course, link=link, message=message)

        elif linkType == 'error':
            dictErrosS3 = webscraping.organize_scarping_of_dict(dictOfficial=dictErrosS3, course=course, link=link, message=message)
        
        elif linkType == 'invalid':
            dictInvalid = webscraping.organize_scarping_of_dict(dictOfficial=dictInvalid, course=course, link=link, message=message)

        elif linkType == 'blank':
            dictBlanck = webscraping.organize_scarping_of_dict(dictOfficial=dictBlanck, course=course, link=link, message=message)
            
    #Salvar os dados obtidos
    prefix = 'novembro_'
    # Sucesso
    filename = prefix + 'success.csv'
    folderWrite = 'output_files'
    pathFileWrite = fileUtils.join_path_filename(filename=filename, baseFolder=folderWrite)
    csvWrite = CSV_Write(pathFileWrite)
    csvWrite.write(dictSuccesS3)
    
    # Erros
    filename = prefix + 'error.csv'
    folderWrite = 'output_files'
    pathFileWrite = fileUtils.join_path_filename(filename=filename, baseFolder=folderWrite)
    csvWrite = CSV_Write(pathFileWrite)
    csvWrite.write(dictErrosS3)
    
    # Em branco
    filename = prefix + 'blank.csv'
    folderWrite = 'output_files'
    pathFileWrite = fileUtils.join_path_filename(filename=filename, baseFolder=folderWrite)
    csvWrite = CSV_Write(pathFileWrite)
    csvWrite.write(dictBlanck)
    
    # Invalidos
    filename = prefix + 'invalid.csv'
    folderWrite = 'output_files'
    pathFileWrite = fileUtils.join_path_filename(filename=filename, baseFolder=folderWrite)
    csvWrite = CSV_Write(pathFileWrite)
    csvWrite.write(dictInvalid)

else:
    print('Arquivo nao existe, informe outro')
