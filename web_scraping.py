import requests

class WebScraping:
    def scraping(self, link: str, course:str):
        linkType = 'success'
        message = 'Link ok'

        try: 
            request = requests.get(link)
            header = request.headers
            
            if 'X-Cache' in header.keys():
                if 'Error from cloudfront'.lower() in header['X-Cache'].lower():
                    linkType = 'error'
                    message = 'Não foi possível acessar o link fornecido'
                    
            elif 'X-Cache'.lower() in header.keys():
                if 'Error from cloudfront'.lower() in header['X-Cache'.lower()].lower():
                    linkType = 'error'
                    message = 'Não foi possível acessar o link fornecido'
            elif request.status_code != 200:
                linkType = 'error'
                message = 'Não foi possível acessar o link fornecido'
        except:
            if link != '':
                linkType = 'invalid'
                message = 'Link invalido'
            else:
                linkType = 'blank'
                message = 'Link em branco'            
        
        return linkType, link, course, message
    
    # Organizar os dados obtidos do scraping em um dicionario
    def organize_scarping_of_dict(self, course: str, message: str, link: str, dictOfficial: dict):
        listAux = []

        if course not in dictOfficial.keys():
            listAux = [{
                'course': course,
                'link': link,
                'message': message
            }]
            dictOfficial[course] = listAux
        else:
            listAux = dictOfficial[course]
            listAux.append({
                'course': course,
                'link': link,
                'message': message
            })

            dictOfficial[course] = listAux
        
        return dictOfficial
                