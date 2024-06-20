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


def main_with_tracemalloc() -> None:
    folder_path = get_dir_path(_target_extension)
    # メモリプロファイルの初期状態
    tracemalloc.start(10)
    current_snapshot = tracemalloc.take_snapshot()
    for file_path in scan_dir(folder_path):
        print(file_path)
        # 評価対象の処理
        loader_process(file_path)
        next_snapshot = tracemalloc.take_snapshot()
        top_stats = next_snapshot.compare_to(current_snapshot, 'lineno')
        for stat in top_stats[:10]:
            print(stat.traceback.format())
    gc.collect()
    print("gc.collect()後")
    next_snapshot = tracemalloc.take_snapshot()
    top_stats = next_snapshot.compare_to(current_snapshot, 'lineno')
    for stat in top_stats[:10]:
        print(stat.traceback.format())


if __name__ == "__main__":
    time.sleep(5)
    main()
    # main_with_tracemalloc()
    time.sleep(5)
