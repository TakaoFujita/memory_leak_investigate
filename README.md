# Python メモリプロファイリング
## 手順
1. 環境準備  
pythonは 3.11 or 3.12  
`python -m venv .venv`  
`source .venv/bin/activate`  
`poetry install --sync --no-root`

2. ファイル準備  
pdf...ワークスペース直下にpdfsフォルダを作成し、pdfファイルを格納する。
pptx...ワークスペース直下にpptxsフォルダを作成し、pptxファイルを格納する。

3. 実行  
`mprof run src/xxxx.py`  
`mprof plot`

## 検証用の各ファイルの説明
loader_check.py  
　　langchainのBaseLoader継承クラスを使ってメモリ使用量を調査
referenceX.py  
　　比較対象のコードでメモリ使用量を調査。  
　　これでメモリリークがない状態を確認。