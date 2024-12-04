#!/bin/sh
xgettext -L lua --from-code=utf-8 \
	-kS -kNS -kFS -kNFS -kPS:1,2 -kFPS:1,2 \
	-kcore.translate:1c,2 -kcore.translate_n:1c,2,3 \
	"$@"
