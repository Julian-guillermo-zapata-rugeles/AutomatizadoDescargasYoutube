# AutomatizadoDescargasYoutube

(REQUISITOS)
* sudo pip3 install selenium
* sudo apt-get install xdotool
* sudo pip3 install youtube-dl
* sudo chmod +x /usr/local/bin/geckodriver # ejecutar para dar permisos

ejecutar python3 ColossoYoutube.py para descargar :D

PD :(se incluye el archivo Geckodriver) el cual deberan copiar en la siguiente ruta (Ubuntu)
---> en el directorio fuente Iniciar terminal de comandos y ejecutar

* sudo cp geckodriver /usr/local/bin/geckodriver #

Script que recibe un listado que contiene nombre de canciones y su artista , una vez obtenida la lista este se ejecuta para controlar al navegador web y usando Xdotool , selenium toma control remoto para descargar las canciones pasadas en la lista.
el proceso es automatico y no hay necesidad de intervenir para seleccionar los archivos a descargar.

funciona así.
* al iniciar solicita el nombre de una cancion / video y su artista (de ser posible con claridad para la busqueda)
* al precionar ENTER el proceso se repite para agregar repetitivamente elementos a la lista de descarga
* una vez completada con los X elementos se preciona 0 para iniciar la descarga 
* el proceso es automatico y no requiere supervision 


#2 POSIBLES ERRORES

Debido a la resolucion de algunos monitores las cordenadas (X,Y) pueden variar generando un click
en el navegador impidiendo abrir corectamente el vinculo que lleva al enlace de la cancion/video a descargar
para solucionarlo es necesario qué:
  * al tener instalado las dependencias se procede asi:
    una vez abierto el navegador firefox ingresar a:
    * https://youtube.com
    * realziar una busqueda corriente (cuaquier cancion )
    * ubicar el mouse sobre el primer enlace del video , ejecutrar una terminal de comandos (sin perder la ubicacion del cursor) 
    * ejecutar : xdotool getmouselocation 
    *obtendrá dos coordenadas como estas : x:647 y:440 screen:0 window:67110170 de las cuales debera extraer solo 647 440
    * en la linea os.system("xdotool mousemove 372 320 ") de la funcion IniciarDescarga(listaRetorno)
    reemplazar os.system("xdotool mousemove 372 320 ") por os.system("xdotool mousemove xxx yyy ") donde xxx yyy son las respectivas coordenadas que obtuvieron luego de ejecutar el comando 
    * solo en caso de ser necesario (aplicar esta guia de posibles errores)
    
    
    Cualquier duda pueden escribirme a
    juliang.zapata@udea.edu.co 
    
    Gracias y espero sea de utilidad.
    
    
    
    
