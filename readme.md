### Checklist

- [x] document assumptions
- [x] this readme
- [x] testing
- [x] cover all supported Python versions
- [ ] validate downloaded file checksums
- [x] algorithm

### Assumptions

- Use Python standard library only, no 3rd party dependencies
- Allow any supported Python version, today 3.8 ~ 3.12
- Distribute as a single file, `package_statistics.py`
- Keep dev-time stuff (tests, test data, scaffolding) separate
- Is *section* important in the package name?
  - The tool is built for distro maintainers, verbose is better than smart

### Testing

```command
> poetry run pytest
```

- [x] test scaffold
- [ ] unit tests
- [ ] test data
- [ ] functional tests
- [x] continuous testing

### Misc

Develop Github Actions on Mac:

```command
# Install a docker runtime, e.g. Docker for Mac
> brew install act
> act --container-architecture linux/x64
```

The latter is needed because `ubuntu-latest` only provides `arm64` Python packages for the latest versions.

### Time Spent

* ½h: pyproject, ruff, pre-commit, github actions, pytest
* 2h: research the format, write the algorithm and tests

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