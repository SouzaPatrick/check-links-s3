# -*- coding: utf-8 -*-

'''
    Fazer a leitura do csv e deixalo dentro de um dicionario
'''
import os
import csv  

class CSV_Read:
    pathFile = ''

    def __init__(self, pathFile: str):
        #Insere o nome do arquivo
        self.pathFile = pathFile
    
    def clear(self, row: dict):
        #Retira a / no final da unidade
        row['UNIDADE'] = row['UNIDADE'].replace('/', '')

        return row

    
    def read_file(self):
        listReader = []
        with open(self.pathFile, mode='r') as csvFile:
            csvReader = csv.DictReader(csvFile)

            for row in csvReader:
                row = self.clear(row)
                filename, fileExtension = os.path.splitext(row['OBJETO'])
                #Retirava o doc no momento da leitura pois eram arquivos que nao queria analizar
                # if '.doc' in fileExtension:
                #     continue
                listReader.append(row)
            return listReader

class CSV_Write:
    def __init__(self, pathFile: str):
        #Insere o nome do arquivo
        self.pathFile = pathFile

    def write(self,dictData: dict):
        with open(self.pathFile, mode='w') as csvFile:
            csvWrite = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvWrite.writerow(['Curso', 'Link'])      
            for course in dictData.keys():
                for dataCourse in dictData[course]:
                    csvWrite.writerow([course, dataCourse['link']])