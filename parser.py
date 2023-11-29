#! /bin/python3

import perf_stat
from perf_stat import PerfStatParser
import os

def get_avg_in_dir(path, output):
    print(path)
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
        print(time_threads)
        output.write("\n" + time_threads[-2] + "," + time_threads[-1] + "," + avg.get_csv())
        # print(avg.get_csv())

result = "data.csv"
try:
    with open(result, 'w') as file:
        file.write("base_slice," + "threads," + perf_stat.get_csv_header())
        get_avg_in_dir("result", file)
        file.close()
except Exception as e:
    print(f"Error: {e}")
