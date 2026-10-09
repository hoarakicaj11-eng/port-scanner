# LOR GPT v1.0 - Port Scanner

A lightweight penetration testing tool that scans target systems to identify open ports and active services.

## What It Does

Scans a target IP addres or hostname to find which ports are open and listening. This helps identify what services are running on a system.
 
## How It Works 

Attempts to connect to each port on the target system using socket connection. if a connection succeeds, the port is marked as OPEN. Uses a configurable timeout to handle slow or unresponsive services

## Why It Matters

Identifying open ports is essential for:
- Security assessments and penetration testing
- Network vulnerability scanning
- Understanding active services on a system
- Network administration and monitoring

## Usage

'''bash
python3 lor_gpt.py

## Example Output

Lori_GPT V1.0
Penetration Testing Suite
==========================

[*] Enter target IP on hostname: 192.168.1.1
[*] Target:192.168.1.1
[*] Start time: 2026-10-09 23:45:10.544236
[*] Scanning 192.168.1.1 for open ports...
[*] Port 53 is OPEN
[*] Port 80 is OPEN
[*] Port 443 is OPEN
[*] Found 3 open ports: [53, 80, 443]
[*] End time: 2026-10-09 23:53:31.607142

## Security & Ethics
Only scan systems you own or have explicit permision to test
Unouthorised port scanning may be ilegal in your jurisdiction

# Author 
LORI HASANAJ | LEARNING PROJECT
