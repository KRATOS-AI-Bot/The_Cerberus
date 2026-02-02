
import os
import re
import json
import argparse
import math

def calculate_shannon_entropy(data):
    entropy = 0.0
    for x in range(256):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def load_patterns(patterns_file):
    with open(patterns_file, 'r') as f:
        patterns = json.load(f)
    return patterns

def load_ignore_file(ignore_file):
    try:
        with open(ignore_file, 'r') as f:
            ignore_paths = [line.strip() for line in f.readlines()]
        return ignore_paths
    except FileNotFoundError:
        return []

def scan_folder(target_folder, patterns, ignore_paths):
    results = []
    for root, dirs, files in os.walk(target_folder):
        for dir in dirs:
            if dir in ['.git', 'venv', 'node_modules', '.terraform', '__pycache__']:
                dirs.remove(dir)
        for file in files:
            if file.endswith(('.jpg', '.png', '.gif', '.zip', '.bin', '.exe')):
                continue
            file_path = os.path.join(root, file)
            if any(file_path.startswith(ignore_path) for ignore_path in ignore_paths):
                continue
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                for pattern in patterns['signatures']:
                    if re.search(pattern, content):
                        results.append({
                            'message': f'[ALERT] {pattern} found in {file_path}',
                            'locations': [{'physicalLocation': {'address': file_path}}]
                        })
                        print(f'[ALERT] {pattern} found in {file_path}')
                entropy = calculate_shannon_entropy(content)
                if entropy > 7.0:
                    results.append({
                        'message': f'[ALERT] High entropy found in {file_path}',
                        'locations': [{'physicalLocation': {'address': file_path}}]
                    })
                    print(f'[ALERT] High entropy found in {file_path}')
            except Exception as e:
                print(f'Error scanning {file_path}: {e}')
    return results

def generate_sarif(results):
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
    return sarif

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', help='Target folder or URL')
    args = parser.parse_args()
    patterns = load_patterns('patterns.json')
    ignore_paths = load_ignore_file('.cerberusignore')
    results = scan_folder(args.target, patterns, ignore_paths)
    sarif = generate_sarif(results)
    with open('results.sarif', 'w') as f:
        json.dump(sarif, f, indent=4)

if __name__ == '__main__':
    main()
