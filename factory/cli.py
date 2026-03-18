from pathlib import Path
import argparse

from factory.generator import AgentGenerator


def main():
    parser = argparse.ArgumentParser(description="OpenClaw Agent Factory CLI")
    parser.add_argument("command", choices=["generate"])
    parser.add_argument("spec")

    args = parser.parse_args()

    root = Path.cwd()
    generator = AgentGenerator(root)

    if args.command == "generate":
        output = generator.generate(Path(args.spec))
        print(f"Generated agent at: {output}")


if __name__ == "__main__":
    main()
