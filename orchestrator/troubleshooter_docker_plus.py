import subprocess


def run_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        out = (result.stdout or "") + (result.stderr or "")
        return out.strip()
    except Exception as e:
        return str(e)


def docker_diagnose_plus():
    results = {}
    results["containers"] = run_command(["docker", "ps", "-a"])
    results["images"] = run_command(["docker", "images"])
    results["networks"] = run_command(["docker", "network", "ls"])
    results["volumes"] = run_command(["docker", "volume", "ls"])
    results["compose_ps"] = run_command(["docker", "compose", "ps"])
    return results


def system_network():
    return run_command(["ip", "a"])


def troubleshoot(agent: str):
    report = {}
    if agent == "docker":
        report["docker"] = docker_diagnose_plus()
        report["network"] = system_network()
    return report
