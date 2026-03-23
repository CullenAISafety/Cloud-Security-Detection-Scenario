# Example Python query to filter suspicious cloud log events
import json

with open('../logs/gcp_audit_sample.log') as f:
    logs = f.readlines()

for line in logs:
    if 'Unauthorized login attempt' in line or 'Privilege escalation attempt' in line:
        print(f"Suspicious event detected: {line.strip()}")
