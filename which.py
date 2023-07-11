def which(program_name : str)-> str | None:
    pass
import os
import sys
def which(prog_name:str) -> bool | str :
    env_var_path = os.getenv("PATH")
    if env_var_path is None :
        return None
    is_windows = sys.platform == "win32"
    search_paths = env_var_path.split(";" if is_windows else ":")
    if is_windows and not prog_name.endswith(".exe") :
        prog_name = prog_name + ".exe"
    for path in search_paths :
        full_path  = os.path.join(path,prog_name)
        if os.path.isfile(full_path) :
            return True, full_path
    return False," ".join(search_paths)