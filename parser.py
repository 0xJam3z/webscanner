import json
import ipaddress

def parse_json(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = [json.loads(line) for line in file]
    return data

def is_ipv4(address):
    try:
        return type(ipaddress.ip_address(address)) is ipaddress.IPv4Address
    except ValueError:
        return False

def format_data(data):
    formatted_data = []
    for item in data:
        if is_ipv4(item['start_ip']) and is_ipv4(item['end_ip']):
            ip_range = f"{item['start_ip']}-{item['end_ip']}"
            country_name = item['country_name']
            as_name = item['as_name']
            formatted_data.append((ip_range, country_name, as_name))
    return formatted_data

def sort_data_by_country(formatted_data):
    return sorted(formatted_data, key=lambda x: x[1])

def main(json_file):
    data = parse_json(json_file)
    formatted_data = format_data(data)
    sorted_data = sort_data_by_country(formatted_data)
    
    for ip_range, country_name, as_name in sorted_data:
        print(f"{ip_range} | {country_name} | {as_name}")

if __name__ == "__main__":
    main('country_asn.json')

