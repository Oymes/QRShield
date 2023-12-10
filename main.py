from colorama import init, Fore
from modules.qr import decode_qr_code
from modules.virustotal import virustotal_api_request, analyze_results
from modules.AbuseIPDB import get_report
from modules.SSLLookup import ssl_lookup
import json
import os  # Import the 'os' module for file-related operations

init(autoreset=True)

def get_api_keys():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        return config.get('virustotal'), config.get('abuseipdb')
    except FileNotFoundError:
        print(f"{Fore.RED}Error: 'config.json' file not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Unable to decode 'config.json'. Check the file format.")
        return None, None

if __name__ == "__main__":
    try:
        print("\033c")  # This clears the terminal screen
        virustotal_key, abuseipdb_key = get_api_keys()
        image_path = input("QR Image Location: ")

        # Check if the file path is valid
        if not os.path.isfile(image_path):
            print(f"{Fore.RED}Error: The specified file does not exist.")
        else:
            if virustotal_key is None or abuseipdb_key is None:
                print(f"{Fore.RED}Error: Unable to load API keys. Please check the 'config.json' file.")
            else:
                print(f"{Fore.CYAN}\nQR Shield\n{Fore.WHITE}{'=' * 9}\n")  # Title with cyan color and white underline

                print(f"{Fore.WHITE}Getting VirusTotal results, this may take some time\n")
                decoded_url = decode_qr_code(image_path)

                if decoded_url:
                    decoded_url, detailed_results = virustotal_api_request(decoded_url, virustotal_key)
                    analyze_results(decoded_url, detailed_results)

                    # Check against AbuseIPDB
                    print(f"{Fore.WHITE}\nGetting AbuseIPDB results, this may take some time\n")
                    get_report(abuseipdb_key, decoded_url)

                    # Passive SSL lookup
                    print(f"{Fore.WHITE}\nSSL Lookup\n")
                    ssl_lookup(decoded_url)
            
                else:
                    print(f"{Fore.RED}No URL decoded from the QR code.")
    
    except Exception as e:
        print(f"{Fore.RED}Error in main script: {e}")
