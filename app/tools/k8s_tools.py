import subprocess

def run(cmd):
    return subprocess.getoutput(cmd)

def get_pods():
    return run("kubectl get pods -A")

def describe_pod(pod):
    return run(f"kubectl describe pod {pod}")

def get_logs(pod):
    return run(f"kubectl logs {pod}")

def get_events():
    return run("kubectl get events --sort-by=.lastTimestamp")