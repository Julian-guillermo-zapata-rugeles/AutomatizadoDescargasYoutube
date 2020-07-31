"""
descargar Musica y convertirla a MP3

"""

def IniciarDescarga(listaRetorno):
	from selenium import webdriver
	from  selenium.webdriver.common.keys import Keys
	import os
	for donwload in listaRetorno:
		os.system("notify-send 'Iniciando'")
		comannd="https://www.youtube.com/results?search_query="+donwload
		driver = webdriver.Firefox()
		driver.get(comannd)
		os.system("xdotool mousemove 372 320 ")
		os.system("xdotool click 1")
		getlink=driver.current_url
		driver.close()
		descargar(getlink)
		kk=donwload.replace(" ","")
		d="move **.m4a ../"+kk+".m4a"
	os.system("notify-send 'cancion descargada' ")

def descargar(link):
	import os
	systemcomand="youtube-dl -f m4a  --playlist-start 1 --playlist-end 1 "+link
	os.system("notify-send 'Iniciando Descarga'")
	os.system(systemcomand)
	os.system("notify-send 'cancion Descargada' ")

def capturar():
	from selenium import webdriver
	from  selenium.webdriver.common.keys import Keys
	import os
	canciones=[]
	contador=0
	sucess=True
	while sucess==True:
		os.system("clear")
		for x in canciones:
			print(x)
		print("")
		print("####################################")
		print("Ingrese El nombre de Una cancion")
		print("cuando Este listo Presione 0 y Enter")
		print("")

		name=str(input(""))
		if name=="0":
			sucess=False
		else:
			canciones.append(name)
	return canciones
lista=capturar()
IniciarDescarga(lista)
