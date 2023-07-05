import re


class Statement:
    def __init__(self, source: (str | None) = None) -> None:
        self.__inner = []

        if source is not None and re.search(r".*;", source):
            self.__inner.append(source)

    def append(self, source: str) -> bool:
        if re.search(r".*;", source):
            self.__inner.append(source)
            return True
        else:
            return False

    def __str__(self) -> str:
        return "\n".join(self.__inner)

    def __add__(self, other):
        s = Statement()
        s.__inner = self.__inner + other.__inner
        return s


class Header:
    def __init__(self) -> None:
        self.__inner = []

    def append(self, source: str) -> bool:
        if re.search(r"^#include(\s)*<[a-z]+.h>(\s)*$", source):
            self.__inner.append(source)
            return True
        else:
            return False

    def __str__(self) -> str:
        return "\n".join(self.__inner)


def build_source(headers: Header, statements: Statement) -> str:
    return """%s
int main(int argc, char **argv, char **envp) {
%s
return 0;
}""" % (
        headers,
        statements,
    )
