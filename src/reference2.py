import gc
import time
from typing import Iterator
import tracemalloc
import objgraph
from langchain.docstore.document import Document
from src.base import get_dir_path, scan_dir

# _target_extension = ".pdf"
_target_extension = ".pptx"


def lazy_load() -> Iterator[Document]:
    for _ in range(10):
        yield Document(page_content="hoge" * 10000000)


def loader_process(file_path: str) -> None:
    """BaseLoaderのlazy_load()でIteratorを取得し、要素を処理は空のforループで展開するだけ"""
    for doc in lazy_load():
        del doc
    

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
    gc.collect()
    time.sleep(5)
