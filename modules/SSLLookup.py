import os
import requests
from colorama import Fore
from urllib.parse import urlparse

def ssl_lookup(target):
    try:
        # Extracting the domain from the target
        domain = urlparse(target).netloc

        # Defining the output folder path
        output_folder = f'output/{domain}'

        # Defining the path for the SSL output file
        ssl_output_file = os.path.join(output_folder, 'ssl.txt')

        # Defining the crt.sh API endpoint
        crt_sh_url = f'https://crt.sh/?q={domain}&output=json'

        # Sending a GET request to the crt.sh API
        response = requests.get(crt_sh_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            certificates = response.json()

            if certificates:
                # Create the output folder if there are certificates
                os.makedirs(output_folder, exist_ok=True)

                # Open the SSL output file in write mode
                with open(ssl_output_file, "w") as log_file:
                    log_file.write(f'SSL Certificates for {domain}:\n')

                    # Iterating through each certificate in the response
                    for cert in certificates:
                        # Write certificate details to the log file
                        log_file.write(f'  - Subject: {cert.get("name_value", "N/A")}\n')
                        log_file.write(f'    Issuer: {cert.get("issuer_name", "N/A")}\n')
                        log_file.write(f'    Valid From: {cert.get("not_before", "N/A")}\n')
                        log_file.write(f'    Valid To: {cert.get("not_after", "N/A")}\n')

                        # Check if 'fingerprint_sha1' is present in the response
                        if 'serial_number' in cert:
                            log_file.write(f'    SHA-1 Fingerprint: {cert["serial_number"]}\n')
                        else:
                            log_file.write(f'    SHA-1 Fingerprint: N/A\n')

                        log_file.write('\n')

                print(f'{Fore.CYAN}SSL Certificates for {domain} found. Details written to \'{Fore.WHITE}{ssl_output_file}{Fore.CYAN}\'{Fore.RESET}')

            else:
                print(f'No SSL certificates found for {domain}')

        else:
            print(f'Request failed with status code {response.status_code}')

    except Exception as e:
        # Print an error message if an exception occurs
        print(f'{Fore.RED}Error in ssl_lookup function: {e}{Fore.RESET}')
