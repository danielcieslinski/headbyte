from pathlib import Path
import json
import time
from datetime import datetime
import os
from typing import List
import moment


# chrometime = lambda base:
# base = moment.utc(1601,0,1)
# base.
#
# def chrometime(x: str):
#     return base +

# x = moment.utc(1601, 0, 1)

# Date(Date.UTC(1601,0,1) + timeValue / 1000);

def rm_dup(b, key):
    tmp = set()
    out = []
    for x in b:
        try:
            elem = x[key]
            if elem not in tmp:
                tmp.add(x[key])
                out.append(x)
        except:
            pass
    return out


def get_str_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def get_modified_time(file: Path) -> str:
    return time.ctime(os.path.getmtime(file))

# def chrome_date_parser()

def read_json_files(paths: List[Path]) -> List[dict]:
    # Loads from
    files, out = [], []
    for p in paths:
        with open(p, 'r') as f:
            files.append(f.read())

    for f in files:
        json.loads(f, object_hook=lambda x: out.append(x))

    return out


def print_jcheck(j):
    for i in j.keys():
        print('Count:', j[i]['count'], j[i]['keys'])

def jcheck(li: List[dict]):
    out = {}
    for r in li:
        hash_set = frozenset(r.keys())
        if hash_set not in out.keys():
            out[hash_set] = {}
            out[hash_set]['keys'] = list(hash_set)
            out[hash_set]['count'] = 0
            out[hash_set]['example'] = r

        else:
            out[hash_set]['count'] += 1

    return out

def ensure_dirs_on_path(path: str):
    sp = path.count('/')
    if sp > 0:
        os.makedirs('/'.join(path.split('/')[:-1]), exist_ok=True)


# ----------
# CLI
# ----------
from rich.table import Table


def auto_table(data: List[dict], title=''):
    table = Table(title=title, show_header=True)
    keys = []
    for c in data[0].keys():
        keys.append(c)
        table.add_column(c)

    for f in data:
        row = [str(f[k]) for k in keys]
        table.add_row(*row)

    return table
