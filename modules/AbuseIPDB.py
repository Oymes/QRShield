import requests
import socket
import json
from colorama import Fore
from urllib.parse import urlparse

def get_report(abuseipdb_key, url):
    try:
        # Extracting the domain from the URL
        domain = urlparse(url).netloc
        
        # Resolving the IP address from the domain
        ip_address = socket.gethostbyname(domain)
        
        # Defining the api-endpoint
        api_url = 'https://api.abuseipdb.com/api/v2/check'
        
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': '90'
        }
        
        headers = {
            'Accept': 'application/json',
            'Key': abuseipdb_key
        }
        
        response = requests.get(url=api_url, headers=headers, params=querystring)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            decodedResponse = json.loads(response.text)
            
            # Extract and print the different values
            print(f'{Fore.CYAN}IP Address:{Fore.WHITE} {decodedResponse["data"]["ipAddress"]}')
            print(f'{Fore.CYAN}Abuse Confidence Score:{Fore.WHITE} {decodedResponse["data"]["abuseConfidenceScore"]}')
            print(f'{Fore.CYAN}Country Code:{Fore.WHITE} {decodedResponse["data"]["countryCode"]}')
            print(f'{Fore.CYAN}ISP:{Fore.WHITE} {decodedResponse["data"]["isp"]}')
            print(f'{Fore.CYAN}Domain:{Fore.WHITE} {decodedResponse["data"]["domain"]}')
            print(f'{Fore.CYAN}Is Tor:{Fore.WHITE} {decodedResponse["data"]["isTor"]}')
            print(f'{Fore.CYAN}Total Reports:{Fore.WHITE} {decodedResponse["data"]["totalReports"]}')
            print(f'{Fore.CYAN}Number of Distinct Users:{Fore.WHITE} {decodedResponse["data"]["numDistinctUsers"]}')
            print(f'{Fore.CYAN}Last Reported At:{Fore.WHITE} {decodedResponse["data"]["lastReportedAt"]}')
        else:
            print(f'{Fore.RED}Request failed with status code {response.status_code}')
    except socket.gaierror as e:
        print(f'{Fore.RED}Error: Unable to resolve the IP address for {url}. Check the URL or try again later. {e}')
    except requests.RequestException as e:
        print(f'{Fore.RED}Error in making the request: {e}')
    except json.JSONDecodeError as e:
        print(f'{Fore.RED}Error decoding JSON response: {e}')
    except Exception as e:
        print(f'{Fore.RED}Unexpected error in get_report function: {e}')

# Example usage:
abuseipdb_key = 'your_abuseipdb_key'
url = 'https://example.com'
get_report(abuseipdb_key, url)
