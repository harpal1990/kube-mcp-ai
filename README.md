# kube-mcp-ai


📘 What is This Project?

KubeMCP AI is an AI-powered Kubernetes troubleshooting assistant.

It uses:

KIND Kubernetes Cluster
MCP Server (FastAPI)
Ollama Local LLM
Telegram Bot Client

This project allows you to:

List Kubernetes pods
Analyze failing pods
Detect root cause
Suggest fixes
Control Kubernetes from Telegram
🧠 What is MCP?
MCP Server

The MCP Server is the backend brain.

It:

Talks to Kubernetes
Fetches logs and events
Sends data to Ollama
Returns AI analysis

In this project:

FastAPI = MCP Server
MCP Client

The MCP Client is the interface users interact with.

It:

Sends commands
Displays results

In this project:

Telegram Bot = MCP Client
⚙️ Architecture
Telegram User
      ↓
Telegram Bot (MCP Client)
      ↓
FastAPI MCP Server
      ↓
kubectl → KIND Cluster
      ↓
Ollama (LLM)
      ↓
AI Response
🔥 Features

✅ List all Kubernetes pods ✅ Analyze failing pods ✅ Analyze all failing workloads ✅ View logs remotely ✅ View pod descriptions ✅ AI-generated root cause analysis ✅ AI-generated fix recommendations ✅ Fully local setup ✅ No cloud cost ✅ Great for learning Kubernetes + AI

📁 Folder Structure
kube-mcp-ai/
│
├── app/
│   ├── main.py
│   ├── tools/
│   │   ├── k8s_tools.py
│   │   ├── ai_tools.py
│   │   ├── analyzer.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │
│   ├── schemas/
│   │   ├── request.py
│   │   ├── response.py
│
├── telegram_bot/
│   ├── bot.py
│   ├── config.py
│
├── runbooks/
│   ├── crashloop.yaml
│   ├── imagepull.yaml
│
├── scripts/
│   ├── setup_kind.sh
│
├── requirements.txt
├── .env
├── README.md
🛠️ Requirements
Python 3.11+
Docker
KIND
kubectl
Ollama
Telegram Account
