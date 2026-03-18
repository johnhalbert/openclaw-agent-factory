from collections import defaultdict

ROUTES = {
    "docker": ["docker", "container", "containers", "image", "images", "volume", "volumes", "bind mount", "compose"],
    "home-assistant": ["home assistant", "homeassistant", "automation", "automations", "entity", "entities", "integration", "integrations", "dashboard"],
    "aws": ["aws", "iam", "ec2", "s3", "vpc", "lambda", "cloudwatch", "role", "policy"],
}


def route_question(question: str):
    q = question.lower()
    scores = defaultdict(int)

    for agent, keywords in ROUTES.items():
        for k in keywords:
            if k in q:
                scores[agent] += max(1, len(k.split()))

    if not scores:
        return "general"

    return max(scores.items(), key=lambda item: item[1])[0]
