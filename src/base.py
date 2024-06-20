import os

_SRC_DIR_PATH = os.path.dirname(__file__)
_PARENT_DIR_PATH = os.path.dirname(_SRC_DIR_PATH)


def get_dir_path(target_extension: str) -> str:
    if target_extension == ".pdf":
        path = os.path.join(_PARENT_DIR_PATH, "pdfs")
    elif target_extension == ".pptx":
        path = os.path.join(_PARENT_DIR_PATH, "pptxs")
    else:
        raise ValueError(f"Invalid target extension: {target_extension}")
    return path


def scan_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                yield entry.path
            elif entry.is_dir():
                yield from scan_dir(entry.path)
