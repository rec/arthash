import json, os
from os import makedirs

open = __builtins__['open']


def write(journal_file, page):
    exists = os.path.exists(journal_file)
    if not exists:
        makedirs(os.path.dirname(journal_file), exist_ok=True)

    with open(journal_file, 'w') as fp:
        json.dump(page, fp, indent=2)

    if exists:
        return


def read(journal_file):
    return json.load(open(journal_file))


def _write_index_file(filename, body):
    with open(filename, 'w') as fp:
        fp.write(TEMPLATE.format(body=body))


TEMPLATE = """<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html><head>
<title>arthash</title>
</head>

<body>
{body}
</body> </html>
"""