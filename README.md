# webscanner

IPv4 domain scanner. Intended to parse through https://ipinfo.io/account/data-downloads JSON, readying for masscan -iL.

masscan & zgrab2 required. Saves zgrab jsons for further parsing/investigation. Enumerates IP - Title by default, easy to manipulate for whatever intended results you're searching for. Limited to 80,443 unless revised. Works with IPv6 although some range adjustment is needed and not included.
