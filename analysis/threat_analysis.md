# Threat Analysis

## Overview
- Analyzed GCP audit logs for suspicious activity
- Detected failed login attempts followed by a privilege escalation
- Event aligns with attacker techniques: unauthorized access followed by privilege abuse

## Findings
1. Source IP 203.0.113.50 triggered failed login attempts
2. Source IP 198.51.100.23 performed a successful privilege escalation
3. User accounts: `user@lab.com`, `admin@lab.com`
4. Actions indicate potential lateral movement attempt

## MITRE ATT&CK Mapping
- T1078: Valid Accounts
- T1078.004: Cloud Accounts
- T1071: Application Layer Protocol (Cloud login)
