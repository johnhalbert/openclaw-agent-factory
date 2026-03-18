from orchestrator.router_simple import route_question


def handle(question: str):
    agent = route_question(question)

    print(f"Routing to agent: {agent}")

    if agent == "docker":
        collection = "docker_docs"
    elif agent == "home-assistant":
        collection = "home_assistant_docs"
    elif agent == "aws":
        collection = "aws_docs"
    else:
        collection = None

    return agent, collection


if __name__ == "__main__":
    import sys

    q = " ".join(sys.argv[1:])

    agent, collection = handle(q)

    print("Agent:", agent)
    print("Docs collection:", collection)
