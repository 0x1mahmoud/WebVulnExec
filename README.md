# WebVulnExec

# Build Status

[![Build Status](https://travis-ci.org/ContinuumIO/ciocheck.svg?branch=master)](https://travis-ci.org/ContinuumIO/ciocheck)
[![Build status](https://ci.appveyor.com/api/projects/status/ylipp3kgn5t4hpdw?svg=true)](https://ci.appveyor.com/project/ContinuumAnalytics/ciocheck)

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

