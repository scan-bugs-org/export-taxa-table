# export-taxa-table
### exports the taxa table and other relevant, associated fields from a symbiota database

This requires access to a symbiota database configured in .my.cnf in the user's home directory in the following format:
```
[client]
user = ...
password = ...
host = ...
database = ...
```

1. Install python dependencies (requires
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) to be installed):
    - `conda env create -f environment.yml`
    - `conda activate export-taxa-table`
2. If you want to automatically zip the output file, which can be quite large, set `zipped_output = True` at the top of
main() in [main.py](./main.py). This will leave you with a zip archive containing the csv output file.
3. Run `python main.py`

The output file is in the following format:
```
"tid","parenttid","rankname","sciname","author"
1,1,"Kingdom","Animalia","Linnaeus, 1758"
2,1,"Phylum","Arthropoda","Latreille, 1829"
4,1,"Subphylum","Hexapoda","Latreille, 1825"
4,2,"Subphylum","Hexapoda","Latreille, 1825"
...
```