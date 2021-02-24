# -*- coding: utf-8 -*-

import os
from pathlib import Path

class FileUtils:
    def join_path_filename(self, filename: str, baseFolder: str) -> str:
        '''
            Realiza a juncao do caminho absoluto do C:\ ate essa pasta onde esta o script com a pasta base de leitura do arquivo e o nome dele
        '''
        pathAbsolute =  os.path.dirname(os.path.abspath(__file__))
        return os.path.join(pathAbsolute, baseFolder, filename)

    def exist_file_folder(self, pathfile: str) -> bool:
        '''
            Verifica se o arquivo existe
        '''
        fileObj = Path(pathfile)
        return fileObj.is_file()
    
    def extract_extension(self, filename) -> tuple:
        filename, fileExtension = os.path.splitext(filename)

        return filename, fileExtension
    
    #Configura a escrita do arquivo
    def configureWrite(self, inputFilename: str, outputSufix: str) -> str:
        FOLDER_WRITE = 'output_files'

        outputfilename = self.extract_extension(inputFilename)[0] + '_' + outputSufix
        pathfileWrite = self.join_path_filename(filename=outputfilename, baseFolder=FOLDER_WRITE)

        return pathfileWrite
    
    def listFiles(self, folder: str) -> list:
        return os.listdir(folder)