Cerberus Enterprise Edition is a powerful tool designed to protect your repositories from security breaches by detecting and alerting on potential secrets and high-entropy strings in your code. This tool combines the strengths of regex pattern matching, Shannon entropy analysis, and SARIF integration to provide a comprehensive security solution.

Features:
Regex Pattern Matching: Cerberus uses a predefined set of high-confidence patterns to identify potential secrets such as AWS keys, Gemini keys, OpenAPI keys, and more.
Shannon Entropy Analysis: In addition to regex matching, Cerberus also analyzes strings for high entropy, which can indicate the presence of secrets or sensitive information.
SARIF Integration: Cerberus generates results in the SARIF format, allowing for easy integration with GitHub's Security tab and other security tools.

How it works:
1. Cerberus scans your repository for files containing potential secrets or high-entropy strings.
2. It uses a combination of regex pattern matching and Shannon entropy analysis to identify potential security risks.
3. The results are generated in the SARIF format and uploaded to GitHub, where they can be viewed in the Security tab.
4. Cerberus also prints alerts to the console, providing immediate feedback to developers.

Benefits:
Protect your repository from security breaches by detecting and alerting on potential secrets and high-entropy strings.
Improve your overall security posture by identifying and remediating potential security risks.
Integrate with GitHub's Security tab for a comprehensive view of your repository's security.

Getting Started:
1. Install Cerberus by cloning this repository and installing the required dependencies.
2. Configure Cerberus by creating a patterns.json file containing your custom regex patterns.
3. Run Cerberus using the scanner.py script, providing the target repository as an argument.
4. View the results in the Security tab of your GitHub repository.

Cerberus is named after the three-headed dog of Greek mythology that guarded the gates of the underworld, protecting it from security breaches. Similarly, Cerberus Enterprise Edition is designed to protect your repository from security breaches, providing a powerful and comprehensive security solution.