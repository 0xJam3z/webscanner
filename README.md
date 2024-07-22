# webscanner

IPv4 domain scanner. Parser.py is intended to parse through https://ipinfo.io/account/data-downloads JSON, readying for masscan -iL. country_asn.json required from previous link. Can be tuned to sort for different information from json, although my copy iterates through by country.

Masscan required. 
git clone https://github.com/robertdavidgraham/masscan.git

zgrab2 required.
git clone https://github.com/zmap/zgrab2.git

After parsing ASN ranges by country or company, output scan to a file called list. Masscan will then parse through entire ASN range(s) and output two files. ips_80.txt and ip_443.txt. zgrab then begins to pull data and output two seperate json files. zgrabparser then loads zgrab jsons for further parsing/investigation. Enumerates IP - Title by default, easy to manipulate for whatever intended results you're searching for. Limited to 80,443 unless revised. Works with IPv6 although some range adjustment is needed and not included.
