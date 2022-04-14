# WebVulnExec


[![CI](https://github.com/dlint-py/dlint/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/dlint-py/dlint/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/dlint-py/dlint/badge.svg?branch=master)](https://coveralls.io/github/dlint-py/dlint?branch=master)
[![Python Versions](https://img.shields.io/pypi/pyversions/dlint.svg)](https://pypi.org/project/dlint/)
[![PyPI Version](https://img.shields.io/pypi/v/dlint.svg)](https://pypi.org/project/dlint/)


## Description
Python Automated tool. Created to test and detect the parameters that could be vulnerable with injection vulnerabilities.

## The Supported Vulnerabilities:
- SQL Injection (Error Based)
- SQL Injection (Time Based)
- Cross-Site Scripting (XSS)
- Local File Inclusion (LFI) / Path Traversel

## Why WebVulnExec?
Automated first then manual. for reviewing the results from automation tool first makes it then easy for you "NOT ALWAYS" but there's things 
you have to automate it. that's why WebVulnExec is here to check the vulnerable parameters that could be vulnerable with injection vulnerabilities.

## Usage:
`python3 webvulnexec http://vulnerable.com/page.php?id=sqli`

