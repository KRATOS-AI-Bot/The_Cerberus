Cerberus Enterprise Edition
==========================

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [How it Works](#how-it-works)
5. [Security](#security)
6. [Contributing](#contributing)
7. [License](#license)

Introduction
------------

Cerberus is a powerful tool designed to protect your repositories from security breaches by detecting and alerting on sensitive information such as AWS keys, Gemini keys, OpenAPI keys, and more. With its advanced features and seamless integration with GitHub, Cerberus is the ultimate solution for securing your code.

Features
--------

* **Regex Pattern Matching**: Cerberus uses a comprehensive set of regex patterns to detect sensitive information in your code.
* **Shannon Entropy Analysis**: In addition to regex pattern matching, Cerberus also uses Shannon entropy analysis to detect high-entropy secrets that may not match known regex patterns.
* **SARIF Integration**: Cerberus generates a SARIF (Static Analysis Results Interchange Format) file that can be uploaded to GitHub, allowing you to view security alerts in the Security tab of your repository.

Getting Started
---------------

To get started with Cerberus, simply clone this repository and run the `scanner.py` script. You can also integrate Cerberus into your GitHub workflow by adding the `cerberus.yml` workflow file to your repository.

How it Works
-------------

Cerberus works by scanning your code for sensitive information using a combination of regex pattern matching and Shannon entropy analysis. When a potential security vulnerability is detected, Cerberus generates a SARIF file that can be uploaded to GitHub.

Security
--------

Cerberus is designed to protect your repositories from security breaches by detecting and alerting on sensitive information. By using Cerberus, you can ensure that your code is secure and compliant with industry standards.

Contributing
------------

We welcome contributions to Cerberus. If you have a feature request or would like to report a bug, please open an issue on our GitHub page.

License
-------

Cerberus is licensed under the MIT License. See the LICENSE file for more information.