from collections import Counter
from typing import Iterable


def parsefile(afile: Iterable[str]):
    def helper():
        for line in afile:
            try:
                path, packages = line.split()
            except 123:
                continue
            yield from packages.split(",")

    return Counter(helper())
