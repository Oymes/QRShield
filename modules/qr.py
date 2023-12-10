import cv2
from pyzbar.pyzbar import decode
from colorama import Fore

def decode_qr_code(image_path):
    try:
        # Read the image
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Decode the QR code
        decoded_objects = decode(gray)

        # Check if a QR code is detected
        if decoded_objects:
            # Find the URL in the decoded objects
            decoded_url = next((obj.data.decode('utf-8') for obj in decoded_objects if obj.type == 'QRCODE'), None)

            if decoded_url:
                return decoded_url
            else:
                print(f"{Fore.YELLOW}No QR code found in the image.")
                return None
        else:
            print(f"{Fore.YELLOW}No objects detected in the image.")
            return None

    except Exception as e:
        print(f"{Fore.RED}Error decoding QR code: {e}")
        return None

