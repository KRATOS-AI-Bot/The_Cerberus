
import os
import re
import json
import math
import argparse

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
        entropy -= prob * math.log2(prob)

    return entropy

def load_patterns(patterns_file):
    """
    Load the patterns from the JSON file.
    """
    with open(patterns_file, 'r') as f:
        patterns = json.load(f)
    return patterns['signatures']

def load_ignore_file(ignore_file):
    """
    Load the ignore file and return a list of paths to skip.
    """
    try:
        with open(ignore_file, 'r') as f:
            ignore_paths = [line.strip() for line in f.readlines()]
        return ignore_paths
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', help='Target folder to scan')
    args = parser.parse_args()

    patterns = load_patterns('patterns.json')
    ignore_paths = load_ignore_file('.cerberusignore')

    results = []
    for root, dirs, files in os.walk(args.target):
        
        # Modifying dirs -- remove .git, venv and others from list
        dirs[:] = [d for d in dirs if d not in ['.git', 'venv', 'node_modules', '.terraform', '__pycache__', '.env']]
        
        for file in files:
            
            # for local testing
            if file in [".env"]:
                continue
            file_path = os.path.join(root, file)
            if file_path in ignore_paths:
                continue

            try:
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue

            # Check for regex matches
            for pattern in patterns:
                matches = re.findall(pattern['pattern'], content)
                if matches:
                    results.append({
                        'message': f"Found potential credential in {file_path}",
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

            # Check for high entropy strings
            for line in content.splitlines():
                entropy = shannon_entropy(line)
                if entropy > 4.5 and len(line) > 20:
                    results.append({
                        'message': f"Found high entropy string in {file_path}",
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

    # Print alerts to console
    for result in results:
        print(f"[ALERT] {result['message']}")

    # Generate SARIF file
    sarif = {
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
        json.dump(sarif, f, indent=4)

if __name__ == '__main__':
    main()
