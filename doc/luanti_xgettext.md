# `luanti_xgettext`

This script is a simple wrapper around `xgettext` that additionally passes
Luanti-specific options. In particular, it lets `xgettext` recognize keywords
that are used for client-side translations in Luanti.

In addition to `core.translate` and `core.translate_n`, this script follows the
following convention:

* `S(str, ...)` is a wrapper for `core.translate(str, ...)`
* `PS(str, str_plural, n)` is a wrapper for `core.translate_n(str, str_plural, n, ...)`.
* `FS` and `FPS` are wrappers that additionally formspec-escape the result of `S` and `PS`, respectively.
* `NS` and `NFS` are similar to `S` and `FS`, respectively, but they do not translate the string and instead allow the string to be translated later.

Refer to https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html for further information on the usage of `xgettext`.
