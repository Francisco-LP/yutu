from pytube import YouTube
import os

print("""
             _         
 _   _ _   _| |_ _   _ 
| | | | | | | __| | | |
| |_| | |_| | |_| |_| |
 \\__, |\\__,_|\\__|\\__,_|
 |___/                 
""")



def descargarVideo():
    try:
        link = str(input("Ingresa el link del video: "))
        yt = YouTube(link)
        yt.streams.filter(file_extension="mp4").first().download()
        print(f"Video {yt.title} descargado exitosamente.")
    except Exception as e:
        print(e)
        print("Error intenta denuevo")

def descargarAudio():
    try:
        link = str(input("Ingrese el link del audio: "))
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first().download()
        nuevoNombre = os.path.splitext(audio)
        os.rename(audio, nuevoNombre[0] + ".mp3")
        print("Audio descargado!!!!")
    except Exception as e:
        print(e)
        print("Error intenta denuevo")

def descargarListaVideo(link):
    try:
        yt = YouTube(link)
        yt.streams.filter(file_extension="mp4").first().download()
        print(f"Video {yt.title} descargado exitosamente.")
    except Exception as e:
        print(f"Error al descargar {link}: {e}")


def descargarVideosDesdeArchivo():
    try:
        with open("linksVideos.txt", "r") as file:
            for link in file:
                descargarListaVideo(link.strip())
    except FileNotFoundError:
        print("El archivo 'links.txt' no se encontró.")
    except Exception as e:
        print(f"Error: {e}")
        
def descargarListaAudio(link):
    try:
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first().download()
        nuevoNombre = os.path.splitext(audio)
        os.rename(audio, nuevoNombre[0] + ".mp3")
        print(f" {yt.title} descargado exitosamente.")
    except Exception as e:
        print(e)
        print("Error intenta denuevo")
        
def descargarAudioDesdeArchivo():
    try:
        with open("linksAudios.txt", "r") as file:
            for link in file:
                descargarListaAudio(link.strip())
    except FileNotFoundError:
        print("El archivo 'linksAudios.txt' no se encontró.")
    except Exception as e:
        print(f"Error: {e}")


while True:
    print("""
    Menú: 

    1. Descargar video
    2. Descargar audio
    3. Descargar videos desde una lista
    4. Descargar audio desde una lista
    5. Salir
    """)
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        descargarVideo()
    elif opcion == '2':
        descargarAudio()
    elif opcion == '3':
        descargarVideosDesdeArchivo()
    elif opcion == '4':
        descargarAudioDesdeArchivo()
    elif opcion == '5':
        print("Saliendo!!")
        break
    else:
        print("Opción no válida, elige una opción válida del 1 al 5.")

