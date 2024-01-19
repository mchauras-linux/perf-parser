#! /bin/python3

import perf_stat
from perf_stat import PerfStatParser
import os

def parse_ebizzy_data_get_records(parser):
    count = 0
    record = 0
    for stat in parser:
        count += 1
        for line in stat.extra_data.split("\n"):
            if "records" in line:
                record += int(line.split(" ")[0])
    return str(record/count)

def get_avg_in_dir(path, output):
    # print(path)
    parsed = False
    parser = []
    for entry in os.scandir(path):
        if entry.is_dir():
            get_avg_in_dir(str(path) + '/' + entry.name, output)
        elif entry.is_file():
            parsed = True
            parser.append(PerfStatParser(str(path) + '/' + entry.name))
    if parsed:
        avg = perf_stat.take_average_of_data(parser)
        time_threads = path.split('/')
        output.write("\n" + time_threads[-2] + "," + time_threads[-1] + "," + avg.get_csv() + parse_ebizzy_data_get_records(parser))
        # print(avg.get_csv())

result = "data.csv"
try:
    with open(result, 'w') as file:
        file.write("base_slice," + "threads," + perf_stat.get_csv_header() + "records")
        get_avg_in_dir("result", file)
        file.close()
except Exception as e:
    print(f"Error: {e}")
