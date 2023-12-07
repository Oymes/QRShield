from colorama import init, Fore
from modules.qr import decode_qr_code
from modules.virustotal import virustotal_api_request, analyze_results
from modules.AbuseIPDB import get_report


init(autoreset=True)

if __name__ == "__main__":
    image_path = 'img/qr.png'
    print("\033c")  # This clears the terminal screen
    print(f"{Fore.CYAN}QR Code Analyzer\n{Fore.WHITE}{'=' * 18}\n")  # Title with cyan color and white underline

    print(f"{Fore.WHITE}Getting VirusTotal results, this may take some time\n")
    decoded_url = decode_qr_code(image_path)

    decoded_url, detailed_results = virustotal_api_request(decoded_url)

    analyze_results(decoded_url, detailed_results)

    print(f"{Fore.WHITE}\nGetting AbuseIPDB results, this may take some time\n")
    get_report()