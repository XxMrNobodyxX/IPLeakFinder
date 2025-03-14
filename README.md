# Internal IP Disclosure Scanner

A Python-based security tool designed to detect internal IP address disclosure vulnerabilities in web applications. This tool helps identify instances where internal IP addresses might be exposed through HTTP redirect responses.

## Description

The Internal IP Disclosure Scanner checks for scenarios where applications might inadvertently reveal internal network information through HTTP 302 redirects. This can be a security concern as it might expose internal network architecture to potential attackers.

## Features

- Scan multiple targets from a file
- Optional proxy support for request routing
- Custom HTTP headers to bypass common restrictions
- Timeout controls to handle unresponsive targets
- Detailed output showing vulnerable and non-vulnerable targets

## Prerequisites

- Python 3.x
- Required Python packages:
  - urllib3 (version 1.26.15 recommended)
  - requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Internal-IP-Disclosure.git
cd Internal-IP-Disclosure
```

2. Install required packages:
```bash
python3 -m pip install --upgrade --user urllib3==1.26.15
pip3 install requests
```

## Usage

Basic usage:
```bash
python3 Internal_IP_Disclosure.py -f targets.txt
```

With proxy:
```bash
python3 Internal_IP_Disclosure.py -f targets.txt -p http://127.0.0.1:8080
```

### Command Line Arguments

- `-f, --file`: Required. File containing list of IPs/domains to scan
- `-p, --proxy`: Optional. Proxy URL (e.g., http://127.0.0.1:8080)
- `-h, --help`: Show help message and exit

### Input File Format

The input file should contain one target per line:
```
example.com
192.168.1.1
test.domain.com
```

## Output Format

The tool provides two types of output:

1. For vulnerable targets (displayed in bright green):
```
target.com ---- Vulnerable: Internal Location: http://internal-ip/path
```

2. For non-vulnerable targets (displayed in bright red):
```
target.com ---- Not Vulnerable
```

Note: The output is color-coded in terminal environments that support ANSI color codes:
- Vulnerable targets are highlighted in bright green
- Non-vulnerable targets are highlighted in bright red

## Security Considerations

- The tool disables SSL verification by default for testing purposes
- It's recommended to use this tool only in authorized testing environments
- Be cautious when testing against production systems

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for obtaining proper authorization before testing any systems they don't own or have explicit permission to test. 