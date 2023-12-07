import requests
import time
from colorama import Fore

def virustotal_api_request(decoded_url):
    if decoded_url:
        try:
            url = "https://www.virustotal.com/api/v3/urls"
            headers = {
                "x-apikey": "API_KEY_HERE",
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded"
            }
            response = requests.post(url, headers=headers, data={"url": decoded_url})
            analysis_id = response.json().get("data", {}).get("id")

            if analysis_id:
                analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
                while True:
                    analysis_response = requests.get(analysis_url, headers=headers)
                    analysis_status = analysis_response.json().get("data", {}).get("attributes", {}).get("status")

                    if analysis_status == "completed":
                        detailed_results = analysis_response.json().get("data", {}).get("attributes", {}).get("results", {})
                        return decoded_url, detailed_results
                    elif analysis_status in ["queued", "in-progress"]:
                        time.sleep(5)
                    else:
                        return decoded_url, {"error": f"Analysis Status: {analysis_status}"}
            else:
                return decoded_url, {"error": "Analysis ID not found in the API response."}
        except Exception as e:
            print(f"{Fore.RED}Error making Virustotal API request: {e}")
            return decoded_url, {"error": f"Virustotal API request failed: {e}"}
    else:
        return None, {"error": "No URL decoded from the QR code."}

def analyze_results(decoded_url, detailed_results):
    if "error" in detailed_results:
        print(f"{Fore.RED}Error in analysis results: {detailed_results['error']}")
    else:
        num_detections = sum(1 for result in detailed_results.values() if result['category'] == 'malicious')
        print(f"{Fore.CYAN}Decoded URL: {Fore.WHITE}{decoded_url}")
        print(f"{Fore.CYAN}Number of Detections: {Fore.WHITE}{num_detections}")

        if num_detections > 0:
            print(f"{Fore.CYAN}Engines detecting as malicious:")
            for engine, result in detailed_results.items():
                if result['category'] == 'malicious':
                    print(f"{Fore.WHITE}  - {engine}")
        else:
            print(f"{Fore.CYAN}No engines detected the URL as malicious.")

        threshold = 3
        if num_detections >= threshold:
            print(f"{Fore.CYAN}Likely Malicious: {Fore.WHITE}Yes")
        else:
            print(f"{Fore.CYAN}Likely Malicious: {Fore.WHITE}No")
