from fastapi import FastAPI
from app.tools import k8s_tools
from app.tools.analyzer import analyze

app = FastAPI()

@app.get("/pods")
def list_pods():
    return {"pods": k8s_tools.get_pods()}

@app.get("/analyze/{pod}")
def analyze_pod(pod: str):
    data = "\n".join([
        k8s_tools.describe_pod(pod),
        k8s_tools.get_logs(pod),
        k8s_tools.get_events()
    ])
    return {"analysis": analyze(data)}

@app.get("/analyze-all")
def analyze_all():
    pods = k8s_tools.get_pods()
    failing = []

    for line in pods.split("\n"):
        if "CrashLoopBackOff" in line or "Error" in line:
            failing.append(line.split()[1])

    results = []
    for pod in failing:
        data = k8s_tools.describe_pod(pod) + k8s_tools.get_logs(pod)
        results.append(f"{pod}:\n{analyze(data)}")

    return {"analysis": "\n\n".join(results) or "No issues"}