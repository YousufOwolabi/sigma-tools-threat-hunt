# Sigma Tools Threat Hunt

This repository contains Sigma detection rules and Python conversion scripts to translate Sigma rules into Splunk queries for threat hunting.

## 🔍 About

This repo focuses on detecting suspicious tools and techniques often used in threat hunts, such as:

- PowerShell abuse
- Downloading tools with `wget`, `curl`, etc.
- Living-off-the-land binaries (LOLBins)
- Credential dumping tools (e.g. Mimikatz)

## 🐍 Python Conversion Script

The script `convert_tools_threathunt.py` takes a Sigma YAML rule and converts it to a Splunk query.

### Usage

Make sure you’re inside your Python virtual environment (if you use one):

```bash
source ~/sigma-rules-Ghost/sigma-env/bin/activate

Then run the conversion script:
python convert_tools_threathunt.py

Example output:
CommandLine IN ("*mimikatz*", "*rundll32*", "*regsvr32*") | table CommandLine

📂 Files in This Repo
convert_tools_threathunt.py – Python script to convert Sigma rules to Splunk queries

tools_threathunt.yml – Example Sigma rule to detect suspicious tool usage

🔗 Related Repos
sigma-rule-detections — My previous Sigma detection rules and conversion scripts

✨ Future Work
Add support for more backends (Elastic, Sentinel, etc.)

Expand the Sigma rule set

Integrate into larger threat hunting workflows

Author: Yusuf Owolabi



