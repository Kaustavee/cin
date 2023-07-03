import subprocess
import os
import re


# regular expression
regx = {
    "quit": r'^(\s)*(quit|exit)(\s)*$',
    "include": r'^#include(\s)*<[a-z]+.h>(\s)*$',
    "statement": r'.*;',
    "print": r'printf(.*);',
}


def build_src(includes, statements):
    include_src = "\n".join(includes)
    statement_src = "\n".join(statements)
    return f"{include_src}\nint main() {{\n{statement_src}\nreturn 0;\n}}"


def compile(src_path):
    subprocess.run(["gcc", src_path, "-o", "run"])
    finnaly_I_can_sleep_now = subprocess.run(["./run"], capture_output=True)
    return True, finnaly_I_can_sleep_now.stdout.decode()


def main():
    logo = "c interpreter v0.0.1"
    print(logo)
    print('_' * len(logo))
    print()

    # include files
    includes = [
        "#include <stdio.h>",
    ]

    statements = []

    while True:
        raw_input = input("> ")

        if re.search(regx["quit"], raw_input):
            break;

        elif re.search(regx["print"], raw_input):
            current_dir_path = os.getcwd()
            file_path = os.path.join(current_dir_path, "temp.c")

            with open(file_path, "w") as f:
                f.write(build_src(includes, statements + [raw_input]))

            ok, out = compile(file_path)
            if ok:
                print(out)

        elif re.search(regx["include"], raw_input):
            includes.append(raw_input)

        elif re.search(regx["statement"], raw_input):
            statements.append(raw_input)

        else:
            print(f"input `{raw_input}` not supported\ntype `quit` or `exit` to exit program")
        
if __name__ == "__main__":
    main()
