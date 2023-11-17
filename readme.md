### Usage

```command
> ./package_statistics.py arm64
1.  devel/piglit                 53007
2.  science/esys-particle        18408
3.  math/acl2-books              17023
4.  libdevel/libboost1.81-dev    15456
5.  libdevel/libboost1.74-dev    14333
6.  lisp/racket                  9599
7.  net/zoneminder               8161
8.  electronics/horizon-eda      8130
9.  libdevel/libtorch-dev        8089
10. libdevel/liboce-modeling-dev 7458
```

Options:
- `-v` to validate the downloaded file checksum
- `-m http://www.nic.funet.fi/debian/` your favourite mirror
- `-h` usage

### Checklist

- [x] document assumptions
- [x] this readme
- [x] testing
- [x] cover all supported Python versions
- [x] validate downloaded file checksums
- [x] algorithm

### Assumptions

- Use Python standard library only, no 3rd party dependencies
- Allow any supported Python version, today 3.8 ~ 3.12
- Distribute as a single file, `package_statistics.py`
- Keep dev-time stuff (tests, test data, scaffolding) separate
- Is *section* important in the package name?
  - The tool is built for distro maintainers, verbose is better than smart
- What's the magical `all` architecture?
  - Leave this to the user, they know better

### Testing

```command
> poetry run pytest
```

- [x] test scaffold
- [x] unit tests
- [x] test data
- [x] functional tests
- [x] continuous testing

### Misc

Develop GitHub Actions on Mac:

```command
# Install a docker runtime, e.g. Docker for Mac
> brew install act
> act --container-architecture linux/x64
```

The latter is needed because `ubuntu-latest` only provides `arm64` Python packages for the latest versions.

### Time Spent

* ½h: pyproject, ruff, pre-commit, github actions, pytest
* 2h: research the format, write the algorithm and tests
* 2h: manual & functional tests, cleanup, error handling

### To Do

When using `act` locally:

```
[test.yaml/pytest-3] ⭐ Run Post actions/setup-python@v4.7.1
[test.yaml/pytest-3]   🐳  docker exec cmd=[node /var/run/act/actions/actions-setup-python@v4.7.1/dist/cache-save/index.js] user= workdir=
| OCI runtime exec failed: exec failed: unable to start container process: exec: "node": executable file not found in $PATH: unknown
[test.yaml/pytest-3]   ❌  Failure - Post actions/setup-python@v4.7.1
```

Why is the post-action failing when everything else works fine?
`node` is implicit, the rest is a mystery.
https://github.com/nektos/act/issues/973
