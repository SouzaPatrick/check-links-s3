# -*- coding: utf-8 -*-

import os
from pathlib import Path

class FileUtils:
    def join_path_filename(self, filename: str, baseFolder: str):
        '''
            Realiza a juncao do caminho absoluto do C:\ ate essa pasta onde esta o script com a pasta base de leitura do arquivo e o nome dele
        '''
        pathAbsolute =  os.path.dirname(os.path.abspath(__file__))
        return os.path.join(pathAbsolute, baseFolder, filename)

    def exist_file_folder(self, pathFile: str):
        '''
            Verifica se o arquivo existe
        '''
        fileObj = Path(pathFile)
        return fileObj.is_file()
    
