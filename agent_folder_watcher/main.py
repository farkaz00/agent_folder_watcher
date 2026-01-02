from pathlib import Path
from argparse import ArgumentParser


class AgentParams:
    """
    Holds all parameters required for the Path Watcher Agent's tasks.

    - path: path to the resource to watch over
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
        watch_path(params.path)
    except Exception as e:
        print(e)


def process_arguments() -> AgentParams:
    """
    Maps the input arguments to an AgentParams object
    """
    ## Add arguments
    ap = ArgumentParser()

    # path: path to the resource to watch
    ap.add_argument("-p", "--path", required=True, help="an existing path to use")

    # Process arguments
    args = ap.parse_args()
    params = AgentParams()
    params.setPath(args.path)
    return params


def watch_path(path: str) -> None:
    """
    Controls the watcher's main loop
    """
    p = Path(path)
    # while True:
    # Iterate over the path if it's a directory
    for root, dirnames, filenames in p.walk():
        print(f"ROOT: {root}")
        print(f"DIRNAMES: {dirnames}")
        print(f"FILENAMES: {filenames}")
    """
    for child in p.iterdir():
        if child.is_dir():
            watch_dir(child)
        elif child.is_file():
            watch_file(child)
    """


def watch_dir(dir: Path) -> None:
    """
    Iterates over the input directory
    """
    print(f"PATH: {dir.name}")
    if not dir.is_dir():
        raise Exception("the input path is not a directory")

    for child in dir.iterdir():
        if child.is_dir():
            watch_dir(child)
        elif child.is_file():
            watch_file(child)


def watch_file(f: Path) -> None:
    """
    Processes the input file
    """
    if not f.is_file():
        raise Exception("the input path is not a file")

    print(f"FILE:{f.name}")


if __name__ == "__main__":
    main()
