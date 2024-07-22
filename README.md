# webscanner

IPv4 domain scanner. Parser.py is intended to parse through https://ipinfo.io/account/data-downloads JSON, readying for masscan -iL. country_asn.json required from previous link. Can be tuned to sort for different information from json, although my copy iterates through by country.

Masscan required. 

```git clone https://github.com/robertdavidgraham/masscan.git```

zgrab2 required.

```git clone https://github.com/zmap/zgrab2.git```

After parsing ASN ranges by country or company, output scan to a file called list. Masscan will then parse through entire ASN range(s) and output two files. ips_80.txt and ip_443.txt. zgrab then begins to pull data and output two seperate json files. zgrabparser.py then Enumerates IP - Title by default, easy to manipulate for whatever intended results you're searching for. 

Works with IPv6 although some range adjustment is needed and not included.

This program is intended for mapping similar to Shodan and can be used to scan any port range and ASN range available on the net. Keeping your country_asn.json up to date from ipinfo.io is important for future use. This project was created as a fast automated system that retains IP lists for future use as well as raw json data from zgrab for revision.

In time, I will be working on developing a C++ application that uses these same concepts, especially SYN scans, and turns this into an AIO scanning application that can pull from multiple servers with the use of parallel processing. I will also be using compression mechanisms on the final output file as these IP - Title files can get up to hundreds of gigabytes in plaintext.
