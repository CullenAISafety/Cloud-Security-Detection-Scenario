# Cloud Security Detection Scenario

**Objective:** Demonstrate detection, triage, and response to cloud-based security incidents in a simulated GCP/AWS/Azure environment.

## Project Scope
- Analyze cloud audit logs for suspicious activity
- Detect unauthorized login attempts or privilege escalation
- Develop detection rules / queries
- Document investigation and response actions

## Skills Demonstrated
- Cloud security logging and analysis
- Threat detection and triage
- Incident response planning
- Rule/query creation for cloud SOC
- Report generation for technical and executive audiences

## Project Structure
- `logs/` → Raw audit and alert logs
- `analysis/` → Analysis notes and mitigation steps
- `detection/` → Detection queries and Sigma/YARA rules
- `iocs/` → Indicators of Compromise
- `reports/` → Final polished incident report

## How to Use
1. Review sample logs in `logs/`
2. Follow analysis steps in `analysis/`
3. Run detection queries in `detection/`
4. Check IOCs in `iocs/`
5. Review final report in `reports/`
