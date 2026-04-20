import streamlit as st
import cv2
from pyzbar import pyzbar
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

st.title("LECTOR DE CODIGO DE BARRAS Y QR")

class BarcodeScanner(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
            x, y, w, h = barcode.rect

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            text = f"{barcode_data} ({barcode_type})"

            cv2.putText(img, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="barcode-scanner",
    video_processor_factory=BarcodeScanner
)
