#!/bin/bash
sudo masscan -p80,443 -iL list --rate=10000 --exclude 255.255.255.255 --wait 0 -oL masscan_results.txt &&
awk '{ if ($3 == 80) print $4 >> "open_ips80.txt"; else if ($3 == 443) print $4 >> "open_ips443.txt" }' masscan_results.txt &&
zgrab2 http --port 80 --input-file open_ips80.txt --max-redirects 0 --output-file zgrab_results_80.json &&
zgrab2 http --port 443 --input-file open_ips443.txt --max-redirects 0 --output-file zgrab_results_443.json &&
python3 new.py > opendomains
echo "Success"
