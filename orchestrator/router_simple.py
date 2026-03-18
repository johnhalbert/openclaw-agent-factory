ROUTES = {
    "docker": ["docker", "container", "image", "volume"],
    "home-assistant": ["home assistant", "automation", "entity"],
    "aws": ["aws", "iam", "ec2", "s3"],
}


def route_question(question: str):
    q = question.lower()

    for agent, keywords in ROUTES.items():
        for k in keywords:
            if k in q:
                return agent

    return "general"
