import darshan as dsh
import pandas as pd
import sqlite3 as sql3
import simple_parsing

from pathlib import Path
from ConversionArgs import ConversionArgs
from LogMetadata import LogMetadata

def gather_metadata(log):
    ...


def convert_standard_module(record):
    df = pd.DataFrame()
    for item in record:
        records = item.to_df()
        print(records)
        for counters in records:
            print(counters)
        # print(record_df)
        # if not record_df.empty():
        #     pd.concat([df, record_df])

    return df
    

def convert_dxt_module(record):
    ...
    # raise NotImplementedError()
    return None


def gather_data(log):
    print(f"Getting data for {log}")
    report = dsh.DarshanReport(str(log))
    metadata = gather_metadata(log)

    log_dfs = {"metadata": metadata}

    # gather data
    for key in report.records.keys():

        df = None
        if "DXT" in key:
            df = convert_dxt_module(report.records[key])
        else:
            df = convert_standard_module(report.records[key])

        log_dfs[key] = df

    for key,df in log_dfs.items():
        print(key)
        print(df)

    return log_dfs


def process_log(args: ConversionArgs):
    log_directory = Path(args.log_file_directory)
    logs = log_directory.glob("*.darshan")

    for log in logs:
        data = gather_data(log)


if __name__ == "__main__":
    args = simple_parsing.parse(ConversionArgs)
    process_log(args)