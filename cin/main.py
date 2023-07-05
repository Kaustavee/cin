import subprocess
import os
import re
import typer

from . import __version__

from . import dirs, source

app = typer.Typer()

# regular expression
regx = {
    "quit": r"^(\s)*(quit|exit)(\s)*$",
    "include": r"^#include(\s)*<[a-z]+.h>(\s)*$",
    "statement": r".*;",
    "print": r"printf(.*);",
}


@app.callback(invoke_without_command=True)
def main():
    # project cache directory will be used
    # to create temp.c file and
    # to compile it

    cache_d = dirs.project_cache_dir("cin")

    if not os.path.isdir(cache_d):
        os.mkdir(cache_d)

    src_file_path = os.path.join(cache_d, "temp.c")
    exe_path = os.path.join(cache_d, "run")

    includes = source.Header()
    assert includes.append("#include <stdio.h>")

    statements = source.Statement()

    logo = "c interpreter v" + __version__
    print(logo)
    print("_" * len(logo))
    print()

    while True:
        raw_input = input("> ")

        if re.search(regx["quit"], raw_input):
            break

        elif re.search(regx["print"], raw_input):
            with open(src_file_path, "w") as f:
                f.write(
                    source.build_source(
                        includes, statements + source.Statement(raw_input)
                    )
                )

            subprocess.run(["gcc", src_file_path, "-o", exe_path])
            r = subprocess.run([exe_path], capture_output=True)
            print(r.stdout.decode())

        elif includes.append(raw_input):
            pass

        elif statements.append(raw_input):
            pass

        else:
            print(
                f"input `{raw_input}` not supported\ntype `quit` or `exit` to exit program"
            )
