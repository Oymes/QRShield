# QR-Code-Decoder

This Python script analyzes QR codes by decoding the URL encoded within them and retrieving information from the VirusTotal and AbuseIPDB APIs. It provides insights into the potential maliciousness of the decoded URL and additional details about the associated IP address.

## Features

- **QR Code Decoding:** Decode QR codes from images to extract URLs.
- **VirusTotal Integration:** Submit decoded URLs to the VirusTotal API for analysis and retrieve information on malicious detections by various antivirus engines.
- **AbuseIPDB Integration:** Query the AbuseIPDB API to obtain information about the IP address associated with the decoded URL.

## Dependencies

- [colorama](https://pypi.org/project/colorama/): For terminal text coloring.
- [requests](https://pypi.org/project/requests/): For making HTTP requests.
- [opencv-python](https://pypi.org/project/opencv-python/): For image processing.
- [pyzbar](https://pypi.org/project/pyzbar/): For decoding QR codes.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/qr-code-analyzer.git
