import pprint

class PerfStatParser:
    def __init__(self, file_path=None) -> None:
        if file_path is None:
            self.file = file_path
            self.extra_data = ""
            self.command = ""
            self.task_clock_cpu_utilized = 0
            self.task_clock_time_ms = 0
            self.context_switches = 0
            self.cpu_migrations = 0
            self.page_faults = 0
            self.cycles = 0
            self.stalled_cycles_frontend = 0
            self.stalled_cycles_backend = 0
            self.stalled_cycles_per_insn = 0
            self.instructions = 0
            self.branches = 0
            self.branch_misses = 0
            self.seconds_time_elapsed = 0
            self.seconds_user = 0
            self.seconds_sys = 0
        else:
            self.file = file_path
            self.extra_data = ""
            self.command = ""
            self.parse_object()

    def __remove_blanks_from_list(self, src):
        filtered_list = [item for item in src if item.strip() != '']
        return filtered_list

    def parse_object(self):
        if self.file is not None:
            with open(self.file, 'r') as file:
                for line in file:
                    if 'Performance counter stats for' in line:
                        self.command = line.split('\'')[1]
                    elif 'task-clock' in line:
                        task_clock = self.__remove_blanks_from_list(line.split(' '))
                        self.task_clock_cpu_utilized = float(task_clock[4].replace(',', ''))
                        self.task_clock_time_ms = float(task_clock[0].replace(',', ''))
                    elif 'context-switches' in line:
                        cs = self.__remove_blanks_from_list(line.split(' '))
                        self.context_switches = float(cs[0].replace(',', ''))
                    elif 'cpu-migrations' in line:
                        cm = self.__remove_blanks_from_list(line.split(' '))
                        self.cpu_migrations = float(cm[0].replace(',', ''))
                    elif 'page-faults' in line:
                        cm = self.__remove_blanks_from_list(line.split(' '))
                        self.page_faults = float(cm[0].replace(',', ''))
                    elif 'cycles     ' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.cycles = float(data[0].replace(',', ''))
                    elif 'stalled-cycles-frontend' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.stalled_cycles_frontend = float(data[0].replace(',', ''))
                    elif 'stalled-cycles-backend' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.stalled_cycles_backend= float(data[0].replace(',', ''))
                    elif 'instructions' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.instructions = float(data[0].replace(',', ''))
                    elif 'stalled cycles per insn' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.stalled_cycles_per_insn = float(data[1].replace(',', ''))
                    elif '   branches' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.branches = float(data[0].replace(',', ''))
                    elif 'branch-misses' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.branch_misses = float(data[0].replace(',', ''))
                    elif 'seconds time elapsed' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.seconds_time_elapsed = float(data[0].replace(',', ''))
                    elif 'seconds user' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.seconds_user = float(data[0].replace(',', ''))
                    elif 'seconds sys' in line:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        self.seconds_sys = float(data[0].replace(',', ''))
                    else:
                        data = self.__remove_blanks_from_list(line.split(' '))
                        if len(data) != 0:
                            self.extra_data = self.extra_data + line

    def print_object(self):
        pprint.pprint(vars(self))

    def add_values(self, val):
        self.task_clock_cpu_utilized += val.task_clock_cpu_utilized
        self.task_clock_time_ms += val.task_clock_time_ms
        self.context_switches += val.context_switches
        self.cpu_migrations += val.cpu_migrations
        self.page_faults += val.page_faults
        self.cycles += val.cycles
        self.stalled_cycles_frontend += val.stalled_cycles_frontend
        self.stalled_cycles_backend += val.stalled_cycles_backend
        self.stalled_cycles_per_insn += val.stalled_cycles_per_insn
        self.instructions += val.instructions
        self.branches += val.branches
        self.branch_misses += val.branch_misses
        self.seconds_time_elapsed += val.seconds_time_elapsed
        self.seconds_user += val.seconds_user
        self.seconds_sys += val.seconds_sys

    def div(self, val):
        if val == 0:
            return
        self.task_clock_cpu_utilized /= val
        self.task_clock_time_ms /= val
        self.context_switches /= val
        self.cpu_migrations /= val
        self.page_faults /= val
        self.cycles /= val
        self.stalled_cycles_frontend /= val
        self.stalled_cycles_backend /= val
        self.stalled_cycles_per_insn /= val
        self.instructions /= val
        self.branches /= val
        self.branch_misses /= val
        self.seconds_time_elapsed /= val
        self.seconds_user /= val
        self.seconds_sys /= val

    def get_csv(self):
        csv = ""
        csv += str(self.task_clock_cpu_utilized) + ","
        csv += str(self.task_clock_time_ms) + ","
        csv += str(self.context_switches) + ","
        csv += str(self.cpu_migrations) + ","
        csv += str(self.page_faults) + ","
        csv += str(self.cycles) + ","
        csv += str(self.stalled_cycles_frontend) + ","
        csv += str(self.stalled_cycles_backend) + ","
        csv += str(self.stalled_cycles_per_insn) + ","
        csv += str(self.instructions) + ","
        csv += str(self.branches) + ","
        csv += str(self.branch_misses) + ","
        csv += str(self.seconds_time_elapsed) + ","
        csv += str(self.seconds_user) + ","
        csv += str(self.seconds_sys) + ","
        return csv

def get_csv_header():
    csv = ""
    csv += "task_clock_cpu_utilized"+ ","
    csv += "task_clock_time_ms"+ ","
    csv += "context_switches"+ ","
    csv += "cpu_migrations"+ ","
    csv += "page_faults"+ ","
    csv += "cycles"+ ","
    csv += "stalled_cycles_frontend"+ ","
    csv += "stalled_cycles_backend"+ ","
    csv += "stalled_cycles_per_insn"+ ","
    csv += "instructions"+ ","
    csv += "branches"+ ","
    csv += "branch_misses"+ ","
    csv += "seconds_time_elapsed"+ ","
    csv += "seconds_user"+ ","
    csv += "seconds_sys"+ ","
    return csv

def take_average_of_data(stat_list):
    count = 0
    perf_avg = PerfStatParser()
    for stat in stat_list:
        count = count + 1
        try:
            perf_avg.add_values(stat)
        except Exception as e:
            print(f"An Error occurred: {e}")
            perf_avg.print_object()
            stat.print_object()
            exit(-1)
    perf_avg.div(count)
    return perf_avg


if __name__ == "__main__":
    parser = PerfStatParser("./result/10ms/104/exp1")
    parser.print_object()
    parser.parse_object()
    parser.print_object()
