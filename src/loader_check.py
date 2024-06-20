import gc
import time
from langchain_community.document_loaders import (
    PDFMinerLoader,
    UnstructuredPowerPointLoader,
)
from langchain_community.document_loaders.base import BaseLoader
import tracemalloc
import objgraph
from src.base import get_dir_path, scan_dir

_target_extension = ".pdf"
# _target_extension = ".pptx"


def _get_loader(file_path: str) -> BaseLoader:
    if _target_extension == ".pdf":
        return PDFMinerLoader(file_path, concatenate_pages=False)
    elif _target_extension == ".pptx":
        return UnstructuredPowerPointLoader(file_path, mode="paged")


def loader_process(file_path: str) -> None:
    """BaseLoaderのlazy_load()でIteratorを取得し、要素を処理は空のforループで展開するだけ"""
    loader = _get_loader(file_path)
    docs = loader.lazy_load()
    for doc in docs:
        del doc
    del docs
    del loader


def main() -> None:
    folder_path = get_dir_path(_target_extension)
    for file_path in scan_dir(folder_path):
        print(file_path)
        # 評価対象の処理
        loader_process(file_path)
    gc.collect()


if __name__ == "__main__":
    time.sleep(5)
    main()
    time.sleep(5)
