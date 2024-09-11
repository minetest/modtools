#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2024 Lars Müller
# License: LGPLv2.1 or later (see LICENSE file for details)

import argparse
import json
import sys
import base64
import re

parser = argparse.ArgumentParser(
        prog = "gltfutil",
        description = "Utility for dealing with embedded images in glTF files")

parser.add_argument("action", choices = ["extract", "strip"])
parser.add_argument("-i", "--input",
        help = "input file (default stdin)")
parser.add_argument("-o", "--output",
        help = "output directory / file (default CWD / stdout)")

args = parser.parse_args()

gltf = None
if args.input:
    with open(args.input) as f:
        gltf = json.load(f)
else:
    gltf = json.load(sys.stdin)

if args.action == "extract":
    print("Extracting embedded base64-encoded images")
    for i, image in enumerate(gltf["images"] or []):
        m = re.match(r"data:image/(.+?);base64,(.+)", image["uri"])
        if not m:
            print(f"Skipping image {i}")
            continue
        format, data = m.group(1, 2)
        path = (args.output or ".") + f"/{i}.{format}"
        print(f"Writing {path}")
        with open(path, "wb") as f:
            f.write(base64.b64decode(data))
elif args.action == "strip":
    for texture in gltf["textures"] or []:
        if "source" in texture:
            del texture["source"]
    if "images" in gltf:
        del gltf["images"]
    if args.output:
        with open(args.output, "w") as f:
            json.dump(gltf, f, separators = (',', ':'))
    else:
        json.dump(gltf, sys.stdout, separators = (',', ':'))
else:
    assert(False)
