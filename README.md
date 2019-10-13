# export-taxa-table
### exports the taxa table, after joining with taxaenumtree to determine parenttid, from a symbiota database

This requires access to a symbiota database configured in .my.cnf in the user's home directory in the following format:
```
[client]
user = ...
password = ...
host = ...
database = ...
```

1. Install python dependencies (requires [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
installed):
    - `conda env create -f environment.yml`
    - `conda activate export-taxa-table`
2. If you want to automatically zip the output file, which can be quite large, set `zipped_output = True` at the top of
main() in [main.py](./main.py)
3. Run `python main.py`
