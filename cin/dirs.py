import os
import sys


def __home_prefixed(dir_name) -> str:
    home_d = os.getenv("HOME")

    if not home_d:
        # WARNING: it should not happen
        raise Exception("HOME environment variable not found")

    return os.path.join(home_d, dir_name)


def __linux_config_dir() -> str:
    config_d = os.getenv("XDG_CACHE_HOME")

    # if `XDG_CONFIG_HOME` enviornment variable is set then return it
    # otherwise config directory is $HOME/.config
    return config_d if config_d else __home_prefixed(".config")


def __linux_cache_dir() -> str:
    config_d = os.getenv("XDG_CACHE_HOME")

    # if `XDG_CACHE_HOME` enviornment variable is set then return it
    # otherwise cache directory is $HOME/.cache
    return config_d if config_d else __home_prefixed(".cache")


def __windows_config_dir() -> str:
    return "implementation pending"


def __windows_cache_dir() -> str:
    return "implementation pending"


# return's path to user config directory
def config_dir() -> str:
    if sys.platform.startswith("linux"):
        return __linux_config_dir()

    elif sys.platform.startswith("win32"):
        return __windows_config_dir()

    else:
        raise Exception("only linux supported")


# return's path to user cache directory
def cache_dir() -> str:
    if sys.platform.startswith("linux"):
        return __linux_cache_dir()

    elif sys.platform.startswith("win32"):
        return __windows_cache_dir()

    else:
        raise Exception("only linux supported")


# return's OS_USER_CONFIG_DIR/project_name
def project_config_dir(project_name: str) -> str:
    return os.path.join(config_dir(), project_name)


# return's OS_USER_CACHE_DIR/project_name
def project_cache_dir(project_name: str) -> str:
    return os.path.join(cache_dir(), project_name)
