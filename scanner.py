
import os
import re
import json
import argparse
import math

def shannon_entropy(string):
    """
    Calculate the Shannon entropy of a string.
    """
    # Calculate the frequency of each character
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Calculate the entropy
    entropy = 0.0
    for char in freq:
        prob = freq[char] / len(string)
        entropy += prob * math.log2(prob)

    return -entropy

def load_patterns(patterns_file):
    """
    Load patterns from a JSON file.
    """
    with open(patterns_file, 'r') as f:
        patterns = json.load(f)
    return patterns['signatures']

def scan_file(file_path, patterns):
    """
    Scan a file for security credentials.
    """
    results = []
    with open(file_path, 'r') as f:
        content = f.read()
        for pattern in patterns:
            matches = re.findall(pattern, content)
            if matches:
                results.append({
                    'message': f"Security credential found: {pattern}",
                    'locations': [
                        {
                            'physicalLocation': {
                                'address': {
                                    'fullyQualifiedName': file_path
                                }
                            }
                        }
                    ]
                })

        # Check for high entropy secrets
        for line in content.splitlines():
            entropy = shannon_entropy(line)
            if entropy > 4.5 and len(line) > 20:
                results.append({
                    'message': f"High entropy secret found: {line}",
                    'locations': [
                        {
                            'physicalLocation': {
                                'address': {
                                    'fullyQualifiedName': file_path
                                }
                            }
                        }
                    ]
                })

    return results

def scan_directory(directory, patterns, ignore_file):
    """
    Scan a directory for security credentials.
    """
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if ignore_file and file_path in ignore_file:
                continue
            results.extend(scan_file(file_path, patterns))
    return results

def main():
    parser = argparse.ArgumentParser(description='Scan for security credentials')
    parser.add_argument('--target', help='Target directory to scan')
    args = parser.parse_args()

    patterns_file = 'patterns.json'
    patterns = load_patterns(patterns_file)

    ignore_file = None
    if os.path.exists('.cerberusignore'):
        with open('.cerberusignore', 'r') as f:
            ignore_file = [line.strip() for line in f.readlines()]

    results = scan_directory(args.target, patterns, ignore_file)

    # Generate SARIF output
    sarif_output = {
        'version': '2.1.0',
        'runs': [
            {
                'tool': {
                    'driver': {
                        'name': 'Cerberus'
                    }
                },
                'results': results
            }
        ]
    }

    with open('results.sarif', 'w') as f:
        json.dump(sarif_output, f, indent=4)

    # Print alerts to console
    for result in results:
        print(f'[ALERT] {result["message"]}')

if __name__ == '__main__':
    main()
