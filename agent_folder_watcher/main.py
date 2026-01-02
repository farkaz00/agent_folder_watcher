import sys
from pathlib import Path
from argparse import ArgumentParser


class AgentParams:
    """
    Holds all parameters required for the Path Watcher Agent's tasks
    """

    def setPath(self, Path: str):
        self.path = Path

    def validate(self):
        # Validate that input folder is actually a folder
        path = Path(self.path)
        if not (path.exists() and path.is_dir()):
            raise Exception("The supplied path does not exist")


def main() -> None:
    params = process_arguments()
    try:
        params.validate()
    except Exception as e:
        print(e)


def process_arguments() -> AgentParams:
    # Add arguments
    ap = ArgumentParser()
    ap.add_argument("--path", help="an existing path to use")

    # Process arguments
    args = ap.parse_args()
    params = AgentParams()
    params.setPath(args.path)
    return params


if __name__ == "__main__":
    main()
