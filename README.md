# Linux-Log-Analyzer
Read logs, count error types, flag anomalies, output a summary report.

---

## What Problem This Solves

Linux systems generate large volumes of logs that can be difficult to scan manually.  
This tool provides a quick way to:

- Identify errors and warnings
- Summarize log severity levels
- Review recent log activity
- Support troubleshooting workflows

It’s intended as a learning and demonstration tool rather than a production log pipeline.

---

## Example Input

Sample log file:

Jan 10 10:17:45 system ERROR Failed to connect to database

Jan 10 10:18:22 system INFO Retrying connection

Jan 10 10:19:01 system ERROR Connection timeout

---

## Example Output

=== Log Summary ===

ERROR: 2

INFO: 1

=== Recent Log Entries ===

Jan 10 10:17:45 system ERROR Failed to connect to database

Jan 10 10:18:22 system INFO Retrying connection

Jan 10 10:19:01 system ERROR Connection timeout

---

## Why I Built This

My professional work has involved Linux infrastructure, automation, and debugging workflows.  
I wanted a small project to:

- Reinforce log analysis skills
- Practice building Linux-friendly CLI tools
- Explore observability concepts
- Demonstrate systems-oriented thinking publicly

---

## What I Learned

- Structured log parsing techniques
- Practical Linux troubleshooting workflows
- Importance of logging consistency
- CLI usability considerations
- Writing clear technical documentation

---

## How to Run

Clone the repo:

```bash
git clone <your-repo-url>
cd linux-log-analyzer
```

Run the analyzer:

```bash
python log_analyzer.py sample_logs/system.log
```

## Possible Future Enhancements

- Regex-based parsing
- Timestamp filtering
- Service-specific analysis
- Integration with journalctl
- Output formatting improvements

## ⚠️ Note

This project is intended for learning, demonstration, and portfolio purposes.
It does not process sensitive production logs.
