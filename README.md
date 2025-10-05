# 🛠️ NginxLogWatcher – Real-Time Nginx Log Analysis & Optimization Tool

> ⚡ A lightweight Python CLI tool for **real-time Nginx log monitoring**, **traffic analysis**, and **performance optimization insights** — built for Linux system administrators and DevOps engineers.

---

## 📖 Overview

**NginxLogWatcher** simplifies the process of analyzing Nginx server logs by providing a command-line interface that can:

- 📡 **Monitor logs in real-time** – see requests as they happen  
- 📊 **Analyze traffic patterns** – track top IPs, endpoints, and response codes  
- 🚨 **Detect anomalies** – identify spikes in errors or unusual traffic  
- 🧠 **Lay the foundation for automation** – prepare for future security & performance recommendations

This project is designed to help sysadmins **debug issues faster**, **optimize performance**, and **improve security visibility** — all from the terminal.

---

## 🌟 Features

| Feature | Description |
|--------|-------------|
| 📁 **Log Parsing** | Parses Nginx access logs and extracts useful fields (IP, method, status, endpoint, etc.) |
| 📈 **Traffic Analytics** | Shows top IPs, most visited endpoints, and response code breakdowns |
| 🔎 **Real-Time Monitoring** | Continuously tails the Nginx log file and prints events as they happen |
| 🧠 **Error Tracking** | Detects and counts `4xx` and `5xx` errors for better troubleshooting |
| ⚙️ **Configurable CLI** | Choose between one-time analysis or continuous monitoring modes |

---

## 🏗️ Project Structure

🔧 Core Features
Feature	Description
🔍 Real-Time Metrics	CPU, RAM, Disk, Network usage collected every few seconds
📜 Nginx Log Monitoring	Auto-parses logs for 4xx/5xx, brute-force, high latency requests
🧠 Anomaly Detection	Flags unusual spikes in requests, CPU, or memory
🚨 Auto Alert System	Sends Slack/email alerts with detailed cause & suggestion
📊 Historical Analytics	Stores data for trend visualization (daily, weekly)
🛡️ Security Insights	Detects common attacks (e.g., repeated 401s, slowloris attempts)
📡 REST API	Exposes metrics & anomalies for integration with Grafana or CI/CD


