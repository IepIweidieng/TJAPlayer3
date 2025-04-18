#!/usr/bin/env bash
# export-utf-8.sh by IID on 2025-04-18 UTC+8

shopt -s globstar

for file in **/*.*; do
    dir_out="$(dirname "${file}")/utf-8"
    mkdir -p "${dir_out}"
    fout="${dir_out}/$(basename "${file}")"
    if ! { iconv -f Shift-JIS "${file}" -o "${fout}" && ! diff -q "${file}" "${fout}"; } >/dev/null 2>&1; then
        rm "${fout}" 2>/dev/null || true # remove if exist
    fi
    rmdir "${dir_out}" 2>/dev/null || true # remove if empty
done
