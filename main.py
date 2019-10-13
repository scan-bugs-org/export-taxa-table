import configparser
import csv
import numpy as np
import os
import pandas as pd
from datetime import date


SQL_EXPORT_TBL = """
SELECT t.tid as tid, te.parenttid as parenttid, u.rankname as rankname, t.sciname as sciname, t.author as author
FROM taxa t 
INNER JOIN taxaenumtree te on t.tid = te.tid 
INNER JOIN taxonunits u on t.rankid = u.rankid 
ORDER BY t.tid;
"""

FILE_SQL_CONFIG = os.path.join(os.environ["HOME"], ".my.cnf")

FILE_OUTPUT = "{}_taxa.csv"

DTYPES_TAXA = {
    "tid": np.int_,
    "parenttid": np.int_,
    "rankname": np.unicode,
    "sciname": np.unicode,
    "author": np.unicode,
}


def get_sql_uri_from_cnf(my_cnf_file):
    """
    :param mysql_config_file: Path to .my.cnf
    :param my_cnf_file: Path to .my.cnf
    :return: SQL URI for querying db using mysql_config_file params
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(my_cnf_file)
    sql_config = config_parser["client"]
    return "mysql+pymysql://{}:{}@{}/{}".format(
        sql_config["user"],
        sql_config["password"],
        sql_config["host"],
        sql_config["database"]
    )


def main():
    date_today = date.today().strftime("%Y-%m-%d")
    db_uri = get_sql_uri_from_cnf(FILE_SQL_CONFIG)
    print("Reading taxa table from database...")
    taxa_export_df = pd.read_sql(SQL_EXPORT_TBL, db_uri)
    print("Exporting taxa table to csv...")
    taxa_export_df.to_csv(
        FILE_OUTPUT.format(date_today),
        columns=DTYPES_TAXA.keys(),
        index=False,
        quoting=csv.QUOTE_NONNUMERIC
    )
    print(taxa_export_df.head())
    print("Done.")


if __name__ == "__main__":
    main()
