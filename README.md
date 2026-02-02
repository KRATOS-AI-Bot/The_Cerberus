Cerberus: The Repository Guardian
================================

Protect your repositories from security breaches with Cerberus, a powerful tool that scans for sensitive credentials and notifies you of potential threats.

Usage
-----

To use Cerberus, simply run the following command in your terminal:
python scanner.py --target <folder_or_url>

This will scan the specified folder or repository for sensitive credentials and output the results in a SARIF file.

Features
--------

* Scans for high-confidence patterns of AWS Keys, Gemini Keys, OpenAPI keys, Groq Keys, GitHub Tokens, Slack Tokens, Discord Tokens, Private Keys (RSA/DSA), Stripe or RazorPay Keys
* Uses Shannon Entropy to detect high-entropy words that may indicate sensitive information
* Excludes common folders like .git, venv, node_modules, .terraform, and __pycache__
* Excludes image, zip, and binary files
* Allows users to ignore specific folders or files using a .cerberusignore file
* Outputs results in SARIF format for easy integration with security tools
* Prints alerts to the console for immediate notification

Security
--------

Cerberus is designed with security in mind. It uses best practices to minimize false positives and maximize detection of sensitive credentials.

Getting Started
---------------

1. Clone the Cerberus repository to your local machine.
2. Run python scanner.py --target <folder_or_url> to scan your repository.
3. Review the results in the output SARIF file.

GitHub Actions
---------------

To use Cerberus in your GitHub Actions workflow, add the following code to your .github/workflows/cerberus.yml file:
name: Cerberus Scan
on:
  push:
    branches:
      - main
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Run Cerberus
        run: python scanner.py --target .
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif

This will run Cerberus on every push to the main branch and upload the results to GitHub.

About
-----

Cerberus is a tool designed to protect your repositories from security breaches. It is named after the three-headed dog that guards the gates of the underworld in Greek mythology. Just as Cerberus protected the underworld, our tool protects your repository from sensitive credentials and other security threats.