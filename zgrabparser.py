import json
from bs4 import BeautifulSoup

# Configuration
OUTPUT_ZGRAB_80 = "zgrab_results_80.json"
OUTPUT_ZGRAB_443 = "zgrab_results_443.json"

def extract_titles(output_file):
    with open(output_file, 'r') as file:
        for line in file:
            try:
                result = json.loads(line.strip())
                if 'data' in result and 'http' in result['data']:
                    ip = result['ip']
                    http_data = result['data']['http']
                    if 'result' in http_data and 'response' in http_data['result']:
                        response = http_data['result']['response']
                        if 'body' in response:
                            body = response['body']
                            if body:
                                soup = BeautifulSoup(body, 'html.parser')
                                title = soup.title.string if soup.title else "No title found"
                                print(f"IP: {ip} - Title: {title}")
                        else:
                            print(f"IP: {ip} - No response body found")
                    else:
                        print(f"IP: {ip} - No response found")
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
            except KeyError as e:
                print(f"Missing expected key: {e}")

def main():
    extract_titles(OUTPUT_ZGRAB_80)
    extract_titles(OUTPUT_ZGRAB_443)

if __name__ == "__main__":
    main()
