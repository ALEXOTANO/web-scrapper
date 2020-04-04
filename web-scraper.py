import requests
import socket
from bs4 import BeautifulSoup
import urllib
import time

socket.setdefaulttimeout(8)


def run():
	host = 'https://www.monkeyuser.com'
	uri = '/2016/project-lifecycle'
	
	for i in range(1, 100):
		error = False
		time.sleep(1)
		try:
			response = requests.get(host + uri)
			print('Conectando a: {}'.format(host + uri))
			soup = BeautifulSoup(response.content, 'html.parser')
		except Exception as error:
			print('Error al conectar')
			error = True
		finally:
			if error: 
				print('No se pudo conectar')
				break;
		if (uri.find('ad-litteram') == -1): 
			if not error :
				try:
					imageContainer = soup.find('p')
					imageUrl = imageContainer.find("img")['src']
					imageName = imageUrl.split('/')[-1]
					print('Descargando la imagen {}'.format(imageName))
					urllib.request.urlretrieve(imageUrl, 'imagenesDescargadas/'+imageName)
				except Exception:
					print('Error al descargar imagen')
					error = True
					
				if not error :

					try:
						nextPageContainer = soup.find("div", {"class":"next"})
						uri = nextPageContainer.find("a")['href']
					except Exception:
						print('Error al obtner nueva URI')
						print(Exception)
						error = True
					finally:
						if error: 
							print('No se pudo obtener nueva URI')
							break;
		else:
			print('Encontramos Ad .. saltando')
			try:
				nextPageContainer = soup.find("div", {"class":"next"})
				uri = nextPageContainer.find("a")['href']
			except Exception:
				print('Error al obtner nueva URI')
				print(Exception)
				error = True
			finally:
				if error: 
					print('No se pudo obtener nueva URI')
					break;
		print('-----------------------------------------------')



if __name__ == '__main__':
	run()
