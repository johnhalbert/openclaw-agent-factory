import subprocess


def run_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)


def docker_diagnose():
    results = {}

    results["containers"] = run_command(["docker", "ps", "-a"])
    results["images"] = run_command(["docker", "images"])

    return results


def system_network():
    return run_command(["ip", "a"])


def troubleshoot(agent: str):
    report = {}

    if agent == "docker":
        report["docker"] = docker_diagnose()
        report["network"] = system_network()

    return report
