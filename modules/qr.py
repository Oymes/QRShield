import cv2
from pyzbar.pyzbar import decode
from colorama import Fore

def decode_qr_code(image_path):
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray)
        decoded_url = next((obj.data.decode('utf-8') for obj in decoded_objects if obj.type == 'QRCODE'), None)
        return decoded_url
    except Exception as e:
        print(f"{Fore.RED}Error decoding QR code: {e}")
        return None
