from app.tools.ai_tools import ask_llm

def rule_check(data):
    if "ImagePullBackOff" in data:
        return "Fix image tag using kubectl set image"
    if "CrashLoopBackOff" in data:
        return "Check logs: kubectl logs <pod>"
    return None

def analyze(data):
    rule = rule_check(data)
    if rule:
        return f"[Rule]\n{rule}"

    prompt = f"""
    You are a Kubernetes SRE expert.
    Analyze issue and provide:
    - root cause
    - fix
    - commands

    Data:
    {data}
    """
    return ask_llm(prompt)