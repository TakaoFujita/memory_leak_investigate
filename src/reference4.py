import gc
import time
import tracemalloc
import objgraph
from src.base import get_dir_path, scan_dir

# _target_extension = ".pdf"
_target_extension = ".pptx"


def loader_process() -> None:
    """単純にメモリを消費する処理。"""
    for _ in range(10):
        hoge = "hoge" * 10000000
        del hoge
    

def main() -> None:
    folder_path = get_dir_path(_target_extension)
    for file_path in scan_dir(folder_path):
        print(file_path)
        # 評価対象の処理
        loader_process()
    gc.collect()


if __name__ == "__main__":
    time.sleep(5)
    main()
    gc.collect()
    time.sleep(5)
