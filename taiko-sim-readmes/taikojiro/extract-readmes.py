# extract-readmes.py by IID on 2025-04-18 UTC+8
# Please adjust computer timezone to UTC+9 before running this
# Requires 7z to be installed. Requires version 22.00 or later to restore ns-precision timestamps

import argparse
import os
from pathlib import PurePath
import re
import subprocess
import sys
import traceback
from typing import Dict, List, Tuple

_7z = 'C://Program Files/7-Zip/7z.exe'

ptn_taikojiro_zip = re.compile(r'^taikojiro(\d)(\d\d[a-z]?).*\.zip$')


def extract_readme_for_zip(ver_suffix: str, fpath_zip: str, dir_output: str) -> None:
    # list
    proc = subprocess.run([_7z, 'l', fpath_zip, '-r', '*.txt', '*.html', '*.css'], capture_output=True)
    if proc.returncode >= 2: # fatal error
        print(f"{fpath_zip} might not be a valid zip file: {proc.stderr.decode()}", file=sys.stderr)
    if proc.returncode == 1: # warning
        print(proc.stderr.decode(), file=sys.stderr)

    # output:
    # [insert 7z messages] [insert archive info]
    #    Date      Time    Attr         Size   Compressed  Name
    #------------------- ----- ------------ ------------  ------------------------
    #2009-12-28 13:57:48 ....A          867          619  taikojiro292/course/exp.txt
    #2012-02-18 14:10:56 ....A         4598         2279  taikojiro292/faq.html
    #2011-01-19 00:06:54 ....A        16685         5167  taikojiro292/img/exp.txt
    #2013-09-12 01:09:17 ....A        21406         8338  taikojiro292/readme.html
    #2013-09-12 01:07:38 ....A        54015        19222  taikojiro292/readme.txt
    #2009-10-17 05:19:54 ....A         3123          712  taikojiro292/rms.css
    #2011-01-19 06:30:22 ....A          689          407  taikojiro292/snd/exp.txt
    #------------------- ----- ------------ ------------  ------------------------
    #2013-09-12 01:09:17             101383        36744  7 files

    fpath_zip_readmes: List[str] = []

    state_parse = 'pre'
    for line in proc.stdout.splitlines():
        if state_parse == 'pre':
            if line.split() == [b'Date', b'Time', b'Attr', b'Size', b'Compressed', b'Name']:
                state_parse = 'head'
            continue
        if state_parse == 'head':
            if line.startswith(b'-'):
                continue
            state_parse = 'file'
        # state == 'file'
        if line.startswith(b'-'): # -> 'foot'
            break

        (b_date, b_time, b_attr, b_size, b_compressed, b_name) = line.split()
        fpath_zip_readmes.append(b_name.decode())

    # extract
    for fpath_zip_readme in fpath_zip_readmes:
        # generate compiled name
        path = PurePath(fpath_zip_readme)
        if path.parts[0].startswith('taikojiro'):
            path = PurePath(*path.parts[1:])
        dir_suffix = ''.join((f'-{x}' for x in path.parts[:-1]))
        fname_out = f'{path.stem}{dir_suffix}{ver_suffix}{path.suffix}'
        fpath_out = os.path.join(dir_output, fname_out)

        # extract with original name
        dir_tmp = os.path.join(dir_output, 'tmp')
        fpath_tmp = os.path.join(dir_tmp, fpath_zip_readme)
        os.makedirs(dir_tmp, exist_ok=True)
        proc = subprocess.run([_7z, 'x', fpath_zip, f'-o{dir_tmp}', fpath_zip_readme, '-aos'], capture_output=True)
        if proc.returncode >= 2: # fatal error
            print(f"not fully successful to extract {fpath_zip_readme} from {fpath_zip}, proceeded: {proc.stderr.decode()}", file=sys.stderr)
        if proc.returncode == 1: # warning
            print(proc.stderr.decode(), file=sys.stderr)

        # rename to compiled name
        os.rename(fpath_tmp, fpath_out)
        print(f"Extracted `{fpath_zip_readme}` -> `{fname_out}` from `{fpath_zip}`")


def extract_readme_for_dir(dir_input: str, dir_output: str) -> None:
    os.makedirs(dir_output, exist_ok=True)
    for fname in os.listdir(dir_input):
        matched = ptn_taikojiro_zip.match(fname)
        if matched is None:
            continue

        ver_suffix = f'-v{matched.group(1)}.{matched.group(2)}'
        fpath = os.path.join(dir_input, fname)
        try:
            extract_readme_for_zip(ver_suffix, fpath, dir_output)
            print(f"Extracted from `{fname}`")
        except Exception:
            traceback.print_exc()
            print(f"Error extracting from `{fpath}`. Continued.", file=sys.stderr)


ptn_versioned = re.compile(r'^(.*)-(v\d\.\d\d[a-z]?)(\..*)$')

def merge_same_readme_for_dir(dir_output: str) -> None:
    # count
    mtime_to_versions: Dict[Tuple[str, str, int], List[Tuple[str, str]]] = {}
    for fname in os.listdir(dir_output):
        fpath = os.path.join(dir_output, fname)
        if not os.path.isfile(fpath):
            continue
        matched = ptn_versioned.match(fname)
        if matched is None:
            continue

        (fstem, version, fext) = matched.groups()
        statinfo = os.stat(fpath)
        mtime_to_versions.setdefault((fstem, fext, statinfo.st_mtime_ns), []).append((version, fpath))

    # merge
    for ((fstem, fext, ns_mtime), versions) in mtime_to_versions.items():
        if len(versions) <= 1:
            continue
        versions.sort() # vd.dd(x); just use lexicographic order

        # merge as first
        fname_merged = f'{fstem}-{versions[0][0]}-{versions[-1][0]}{fext}'
        fpath_merged = os.path.join(dir_output, fname_merged)
        os.rename(versions[0][1], fpath_merged)
        print(f"Merged as {fname_merged}: {', '.join((v[0] for v in versions))}")

        # delete others
        while len(versions) > 1:
            os.remove(versions[-1][1])
            del versions[-1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_directory', nargs='?', default='.',
        help=f'where the TaikoJiro zip files are located (default: .)')
    parser.add_argument('output_directory', nargs='?', default='.',
        help=f'where the extracted readme files will be saved (default: .)')
    args = parser.parse_args()

    print(f"Input directory: {args.input_directory}")
    print(f"Output directory: {args.output_directory}")

    extract_readme_for_dir(args.input_directory, args.output_directory)
    merge_same_readme_for_dir(args.output_directory)

if __name__ == "__main__":
    main()
