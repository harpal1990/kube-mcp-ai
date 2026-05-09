# 🚀 KubeMCP AI – AI-Powered Kubernetes SRE Assistant

## 📘 What is This Project?

KubeMCP AI is an AI-powered Kubernetes troubleshooting assistant.

It uses:

- KIND Kubernetes Cluster
- MCP Server (FastAPI)
- Ollama Local LLM
- Telegram Bot Client

This project allows you to:

- List Kubernetes pods
- Analyze failing pods
- Detect root causes
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

- ✅ List all Kubernetes pods
- ✅ Analyze failing pods
- ✅ Analyze all failing workloads
- ✅ View logs remotely
- ✅ View pod descriptions
- ✅ AI-generated root cause analysis
- ✅ AI-generated fix recommendations
- ✅ Fully local setup
- ✅ No cloud cost
- ✅ Great for learning Kubernetes + AI

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

Verify installation:

```bash
kubectl version --client
```

---

# 🚀 Step 3 – Create KIND Cluster

```bash
kind create cluster --name mcp-cluster
```

Verify cluster:

```bash
kubectl get nodes
```

Expected output:

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

Test the model:

```bash
ollama run llama3
```

---

# 🚀 Step 5 – Clone Repository

```bash
git clone https://github.com/your-username/kube-mcp-ai.git
cd kube-mcp-ai
```

---

# 🚀 Step 6 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Step 7 – Configure Telegram Bot

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

4. Copy the generated BOT TOKEN

---
## Replace token telegram_bot\config.py file

```
BOT_TOKEN=YOUR_BOT_TOKEN
MCP_URL=http://localhost:8000
```

---

# 🚀 Step 8 – Start MCP Server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

# 🚀 Step 9 – Start Telegram Bot

```bash
cd telegram_bot
python3 bot.py
```

Expected output:

```text
Telegram bot started successfully
```

---

# 🧪 Step 10 – Create Test Pod

Create a file named:

```text
bad-pod.yaml
```

Add the following content:

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

Apply the pod:

```bash
kubectl apply -f bad-pod.yaml
```

Verify pod status:

```bash
kubectl get pods
```

Expected output:

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

# 📂 Main Project Files

## `app/main.py`

Handles all FastAPI routes.

---

## `app/tools/k8s_tools.py`

Runs Kubernetes (`kubectl`) commands.

---

## `app/tools/ai_tools.py`

Connects to Ollama.

---

## `app/tools/analyzer.py`

Combines:

- Rule-based checks
- AI analysis

---

## `telegram_bot/bot.py`

Telegram client for interacting with MCP server.

---

# 🚨 Common Issues

## kubectl connection refused

Fix kubeconfig permissions:

```bash
mkdir -p ~/.kube
sudo cp /root/.kube/config ~/.kube/config
sudo chown $(id -u):$(id -g) ~/.kube/config
```

---

## Telegram Invalid Token

Generate a new token using `@BotFather`.

---

## Ollama Looping

Trim logs before sending them to the LLM.

Example:

```python
logs = logs[-2000:]
```

---

# 🎯 Future Enhancements

- Kubernetes event monitoring
- Namespace support
- Slack integration
- Web dashboard
- Grafana integration
- Prometheus alerts
- Multi-cluster support
- AI-generated remediation commands

---

# 📜 License

MIT License

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 📺 Share it on YouTube or LinkedIn

---

# 👨‍💻 Author

Built for learning Kubernetes + AI + SRE automation using local LLMs.
