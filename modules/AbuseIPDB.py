import requests
import json
from colorama import Fore

def get_report():
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    querystring = {
        'ipAddress': '103.14.48.18',
        'maxAgeInDays': '90'
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': 'API-KEY-HERE'
    }
    
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    
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
        print(f'Request failed with status code {response.status_code}')

get_report()
