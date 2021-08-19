# -*- coding: utf-8 -*-

from script_csv import CSV_Read, CSV_Write
from web_scraping import WebScraping
from utils import FileUtils
import progressbar

def countItems(dictCourse: dict) -> int:
    count = 0
    for course in dictCourse:
        count+= len(dictCourse[course])
    
    return count

fileUtils = FileUtils()

folderRead = 'base_csv'


baseFiles = fileUtils.listFiles(folderRead)

for filename in baseFiles:
    # filename = 'new.csv'

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
        # print(listReader)
        numberItems = len(listReader)
        with progressbar.ProgressBar(max_value=numberItems) as bar:
            for indice, item in enumerate(listReader):
                # if 'questionario' in item['OBJETO'].lower():
                #     continue
                linkType, link, course, message = webscraping.scraping(link=item['LINK'], course=item['CURSO'])

                if linkType == 'success':
                    dictSuccesS3 = webscraping.organize_scarping_of_dict(dictOfficial=dictSuccesS3, course=course, link=link, message=message)

                elif linkType == 'error':
                    dictErrosS3 = webscraping.organize_scarping_of_dict(dictOfficial=dictErrosS3, course=course, link=link, message=message)
                
                elif linkType == 'invalid':
                    dictInvalid = webscraping.organize_scarping_of_dict(dictOfficial=dictInvalid, course=course, link=link, message=message)

                elif linkType == 'blank':
                    dictBlanck = webscraping.organize_scarping_of_dict(dictOfficial=dictBlanck, course=course, link=link, message=message)
            
                bar.update(indice+1)
                
        #Salvar os dados obtidos
        # Sucesso
        outputSufix = 'success.csv'
        pathFileWrite = fileUtils.configureWrite(inputFilename=filename, outputSufix=outputSufix)
        csvWrite = CSV_Write(pathFileWrite)
        csvWrite.write(dictSuccesS3)
        print(f'Arquivo: {outputSufix} possui {countItems(dictSuccesS3)} links')

        # Erros
        outputSufix = 'error.csv'
        pathFileWrite = fileUtils.configureWrite(inputFilename=filename, outputSufix=outputSufix)
        csvWrite = CSV_Write(pathFileWrite)
        csvWrite.write(dictErrosS3)
        print(f'Arquivo: {outputSufix} possui {countItems(dictErrosS3)} links')
        
        # Em branco
        outputSufix = 'blank.csv'
        pathFileWrite = fileUtils.configureWrite(inputFilename=filename, outputSufix=outputSufix)
        csvWrite = CSV_Write(pathFileWrite)
        csvWrite.write(dictBlanck)
        print(f'Arquivo: {outputSufix} possui {countItems(dictBlanck)} links')
        
        # Invalidos
        outputSufix = 'invalid.csv'
        pathFileWrite = fileUtils.configureWrite(inputFilename=filename, outputSufix=outputSufix)
        csvWrite = CSV_Write(pathFileWrite)
        csvWrite.write(dictInvalid)
        print(f'Arquivo: {outputSufix} possui {countItems(dictInvalid)} links\n\n')

    else:
        print('Arquivo nao existe, informe outro')
