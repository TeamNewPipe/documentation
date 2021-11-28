#! /bin/bash

set -e
set -o pipefail
set -x

this_dir="$(readlink -f -- "$(dirname -- "${BASH_SOURCE[0]}")")"
image="python:3-alpine"

# as we use a pipe to stdin and thus cannot use -it, Ctrl-C does not work by default
# turns out that combining -i with --init solves that problem
# see https://stackoverflow.com/a/60812082
docker run --rm -i -v "$this_dir"/..:/ws -w /ws --init "$image" sh <<\EOF
    pip install -r requirements.txt
    python linkcheck.py
EOF
