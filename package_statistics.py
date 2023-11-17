#!/usr/bin/env python
from argparse import ArgumentParser, ArgumentError
from collections import Counter
from typing import Iterable, Dict, List, Tuple, Any
from urllib.request import urlopen, Request
from hashlib import sha256
import io
import gzip
import operator
import warnings


def parsefile(afile: Iterable[str]) -> Dict[str, int]:
    def helper():
        for line in afile:
            try:
                path, packages = line.rsplit(None, 1)
            except Exception as e:
                warnings.warn("Bad data in a file: %s" % e)
                print("bad line")
                print(line)
            yield from packages.split(",")

    return Counter(helper())


def summary(data: Dict[str, int], *, n=10) -> List[Tuple[str, int]]:
    """Return `n` largest items, sorted"""
    return sorted(data.items(), key=operator.itemgetter(-1), reverse=True)[:n]


def tabulate(data: Iterable[Tuple[Any, Any]]) -> str:
    """Make a table from `data`; returns newline-separated string"""
    data = list(data)
    if not data:
        return ""
    fmt = "%%-%ss %%s" % max(len(str(k)) for k, _ in data)
    lines = [fmt % datum for datum in data]
    return "\n".join(
        "%-3s %s" % ("%s." % (i + 1), line) for i, line in enumerate(lines)
    )


parser = ArgumentParser(description="Report top packages by file count for given arch.")
parser.add_argument("-v", "--validate", action="store_true", help="Validate checksums")
parser.add_argument("-m", "--mirror", type=str, help="Specify a mirror to use")
parser.add_argument("arch", type=str, help="Package architecture to query")

PRIMARY = "http://ftp.uk.debian.org/debian/dists/stable/main/"

ARCHES = (
    "all",
    "amd64",
    "arm64",
    "armel",
    "armhf",
    "i386",
    "mips64el",
    "mipsel",
    "ppc64el",
    "s390x",
    "source",
)


def validate_download(mirror: str, body: bytes, etag: str):
    """
    This part is questionable / far from perfect.

    Why would a downloaded file be bad?
    - a man-in-the-middle attack: the by-hash path can be faked as well
    - data changed by proxy or firewall: will be detected
    - truncated download: will be detected
    """
    hash = sha256(body).hexdigest()
    url = "%s/by-hash/SHA256/%s" % (mirror.rstrip("/"), hash)
    with urlopen(Request(url, method="HEAD")) as r:
        if r.status != 200:
            warnings.warn("Unable to validate download, code %s", r.status)
        if r.headers.get("ETag") != etag:
            # Since Bug#473392 was resolved, ETag is consistent
            warnings.warn("Unable to validate download, ETag mismatch")


def download(url: str) -> Tuple[str, bytes]:
    with urlopen(url) as r:
        if r.status != 200:
            raise Exception("Failed to download", url, r.status)
        return r.headers.get("ETag"), r.read()


def main(mirror: str, arch: str, validate: bool = False):
    if arch not in ARCHES:
        warnings.warn("Unknown architecture %r" % arch)

    url = "%s/Contents-%s.gz" % (mirror.rstrip("/"), arch)
    etag, body = download(url)
    if validate:
        validate_download(mirror, body, etag)

    with gzip.open(io.BytesIO(body), "rt") as f:
        print(tabulate(summary(parsefile(f))))


if __name__ == "__main__":
    try:
        args = parser.parse_args()
    except ArgumentError:
        parser.print_help()
        raise SystemExit(1)

    main(args.mirror or PRIMARY, args.arch, args.validate)
