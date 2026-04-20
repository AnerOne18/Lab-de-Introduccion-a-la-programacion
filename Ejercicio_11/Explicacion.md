## Explicacion de codigo del lector de codigo de barras y QR

import streamlit as st # = esto lo uso para crear la página web donde se va a ver todo.
import cv2 # = es OpenCV, sirve para trabajar con imágenes (dibujar, texto, etc.).
from pyzbar import pyzbar # = este es el que detecta los códigos de barras y QR.
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase # = esto me permite usar la cámara en tiempo real dentro de Streamlit.
import av # = sirve para convertir las imágenes a formato de video que Streamlit pueda mostrar.

# Luego pongo el título de la app:
st.title("LECTOR DE CODIGO DE BARRAS Y QR") = El titulo sin mas.

# Después creo una clase:
class BarcodeScanner(VideoProcessorBase): = Procesa lo que ve la camara.

# Dentro de esa clase está lo importante:
def recv(self, frame): = Esta función se ejecuta todo el tiempo, frame por frame O sea, cada imagen que capta la cámara pasa por aquí.

# Paso el frame a un formato que OpenCV pueda entender:
img = frame.to_ndarray(format="bgr24")

# En este busca los codigos en la imagen para dar el resultado de busqueda:
barcodes = pyzbar.decode(img)

# Por si hay varios códigos en pantalla:
for barcode in barcodes:

# Saco su posición:
x, y, w, h = barcode.rect

# Le pongo un cuadro verde al código para que se vea que lo detectó:
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Obtengo la info del código: numero, link, qr, etc.
barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
# Armo el texto:
text = f"{barcode_data} ({barcode_type})"

# Lo dibujo en la pantalla: Esto pone el texto arriba del código
cv2.putText(img, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

# Al final regreso la imagen: Ya con el cuadro y el texto, para que se muestre en la app
return av.VideoFrame.from_ndarray(img, format="bgr24")

# Y por último activo la cámara:
webrtc_streamer(
    key="barcode-scanner",
    video_processor_factory=BarcodeScanner
)
# Esto: prende la cámara, usa mi clase para procesar el video, muestra todo en la pagina.
