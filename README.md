# 🚀 KubeMCP AI – AI-Powered Kubernetes SRE Assistant

## 📦 Recommended GitHub Repository Names

### 🔥 Best Option
```text
kube-mcp-ai
```

---

## Other Good Repository Names

```text
ai-kubernetes-troubleshooter
kubernetes-ai-agent
ollama-k8s-mcp
k8s-ai-sre-assistant
telegram-k8s-ai-bot
mcp-kubernetes-agent
ai-devops-mcp
```

---

## ✅ Recommended Final Naming

### GitHub Repository
```text
kube-mcp-ai
```

### Project Name
```text
KubeMCP AI
```

### YouTube Title
```text
AI-Powered Kubernetes Troubleshooting with Ollama + MCP
```

---

> Control, Debug & Analyze Kubernetes using Telegram + MCP + Ollama + KIND 🤖

---

# 🎥 YouTube Video Title Ideas

## 🔥 Recommended Title
**I Built an AI Kubernetes Engineer Using MCP + Ollama + Telegram 🤖**

---

## Alternative Titles
- AI DevOps Agent for Kubernetes (Local & Free)
- Control Kubernetes from Telegram using AI 🚀
- AI-Powered Kubernetes Troubleshooting with Ollama + MCP
- I Built an AI SRE Assistant for Kubernetes
- Kubernetes + AI + Telegram = DevOps Automation 🔥

---

# 🖼️ Thumbnail Text Suggestions

## Main Text
```text
AI KUBERNETES ENGINEER
```

## Small Text
```text
MCP + OLLAMA + TELEGRAM
```

## Corner Text
```text
ASK → ANALYZE → FIX
```

---

# 📘 What is This Project?

KubeMCP AI is an AI-powered Kubernetes troubleshooting assistant.

It uses:
- KIND Kubernetes Cluster
- MCP Server (FastAPI)
- Ollama Local LLM
- Telegram Bot Client

This project allows you to:
- List Kubernetes pods
- Analyze failing pods
- Detect root cause
- Suggest fixes
- Control Kubernetes from Telegram

---

# 🧠 What is MCP?

## MCP Server
The MCP Server is the backend brain.

It:
- Talks to Kubernetes
- Fetches logs and events
- Sends data to Ollama
- Returns AI analysis

In this project:
```text
FastAPI = MCP Server
```

---

## MCP Client
The MCP Client is the interface users interact with.

It:
- Sends commands
- Displays results

In this project:
```text
Telegram Bot = MCP Client
```

---

# ⚙️ Architecture

```text
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
```

---

# 🔥 Features

✅ List all Kubernetes pods
✅ Analyze failing pods
✅ Analyze all failing workloads
✅ View logs remotely
✅ View pod descriptions
✅ AI-generated root cause analysis
✅ AI-generated fix recommendations
✅ Fully local setup
✅ No cloud cost
✅ Great for learning Kubernetes + AI

---

# 📁 Folder Structure

```text
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
```

---

# 🛠️ Requirements

- Python 3.11+
- Docker
- KIND
- kubectl
- Ollama
- Telegram Account

---

# 🚀 Step 1 – Install KIND

## Install KIND

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

---

# 🚀 Step 2 – Install kubectl

```bash
sudo snap install kubectl --classic
```

Verify:

```bash
kubectl version --client
```

---

# 🚀 Step 3 – Create KIND Cluster

```bash
kind create cluster --name mcp-cluster
```

Verify:

```bash
kubectl get nodes
```

Expected:

```text
mcp-cluster-control-plane   Ready
```

---

# 🚀 Step 4 – Install Ollama

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Start Ollama

```bash
ollama serve
```

---

## Pull LLM Model

```bash
ollama pull llama3
```

Test:

```bash
ollama run llama3
```

---

# 🚀 Step 5 – Clone Project

```bash
git clone https://github.com/your-username/kube-mcp-ai.git
cd kube-mcp-ai
```

---

# 🚀 Step 6 – Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 🚀 Step 7 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

```text
fastapi
uvicorn
ollama
python-telegram-bot
requests
python-dotenv
```

---

# 🚀 Step 8 – Configure Telegram Bot

## Create Telegram Bot

1. Open Telegram
2. Search for:

```text
@BotFather
```

3. Run:

```text
/newbot
```

4. Copy BOT TOKEN

---

# 🔐 Create .env File

```env
BOT_TOKEN=YOUR_BOT_TOKEN
MCP_URL=http://localhost:8000
```

---

# 🚀 Step 9 – Start MCP Server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

# 🚀 Step 10 – Start Telegram Bot

```bash
cd telegram_bot
python3 bot.py
```

Expected:

```text
Telegram bot started successfully
```

---

# 🧪 Step 11 – Create Test Pod

Create file:

```text
bad-pod.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bad-pod
spec:
  containers:
  - name: app
    image: nginx:wrongtag
```

Apply:

```bash
kubectl apply -f bad-pod.yaml
```

Verify:

```bash
kubectl get pods
```

Expected:

```text
bad-pod   ImagePullBackOff
```

---

# 🤖 Telegram Commands

## List Pods

```text
/pods
```

---

## Analyze Single Pod

```text
/analyze bad-pod
```

---

## Analyze All Failing Pods

```text
/analyze_all
```

---

## View Logs

```text
/logs bad-pod
```

---

## Describe Pod

```text
/describe bad-pod
```

---

# 🧠 Example AI Output

```text
🔴 Issue: ImagePullBackOff

Root Cause:
Invalid image tag

Fix:
kubectl set image deployment/app app=nginx:latest
```

---

# 📜 Main Project Files

## app/main.py
Handles all FastAPI routes.

---

## app/tools/k8s_tools.py
Runs kubectl commands.

---

## app/tools/ai_tools.py
Connects to Ollama.

---

## app/tools/analyzer.py
Combines:
- Rule-based checks
- AI analysis

---

## telegram_bot/bot.py
Telegram client for interacting with MCP server.

---

# 🚨 Common Issues

## kubectl connection refused

Fix kubeconfig:

```bash
mkdir -p ~/.kube
sudo cp /root/.kube/config ~/.kube/config
sudo chown $(id -u):$(id -g) ~/.kube/config
```

---

## Telegram Invalid Token

Generate new token using BotFather.

---

## Ollama Looping

Trim logs before sending to LLM.

Example:

```python
logs = logs[-2000:]
```

---

# 🎬 YouTube Video Flow

## Intro
- Problem statement
- Why AI + Kubernetes?

---

## Demo
- Create failing pod
- Show Telegram bot
- Run:

```text
/pods
/analyze bad-pod
```

- AI explains root cause

---

## Architecture Explanation
- MCP Server
- MCP Client
- Ollama
- KIND

---

## Final Demo
- Restart or fix workload
- Pod becomes healthy

---

# 🚀 Future Improvements

- Auto-fix mode
- Multi-cluster support
- Monitoring integration
- Slack integration
- Web dashboard
- Prometheus integration
- Alerting system

---

# ⭐ Support

If you like this project:

✅ Star the repository
✅ Share with DevOps community
✅ Subscribe on YouTube

---

# 👨‍💻 Author

Harpal Gohil

DevOps | Kubernetes | AI Automation

---

# 🏁 Final Thought

> This is not just Kubernetes automation.
>
> This is your local AI SRE teammate. 🚀

