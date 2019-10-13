# export-taxa-table

1. Install python dependencies (requires [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
installed):
    - `conda env create -f environment.yml`
    - `conda activate export-taxa-table`
2. If you want to automatically zip the output file, which can be quite large, set `zipped_output = True` at the top of
main() in [main.py](./main.py)
3. `python main.py`