# SPDX-License-Identifier: CC0-1.0
# Requires sed -r; use sed -i -r -f 'blockbench_to_minetest.sed' 'model.obj' for easiest results

# Remove comments
/^#\s.*$/d

# Minetest doesn't use materials
/mtllib.*/d
/usemtl.*/d

# If we find a cube called "mat<n>", replace it with "g <n>"
# You can use this to specify where a texture group starts, name a cube e.g. "mat1" to tell MT the second tile is used from thereon.
s/o mat([0-9]+)/g \1/g

# Remove redundant named objects
/o .*/d

# Remove empty lines
/^\s*$/d
