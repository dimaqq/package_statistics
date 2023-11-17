### Checklist

- [ ] document assumptions
- [ ] this readme
- [ ] testing
- [ ] cover all supported Python versions
- [ ] validate downloaded file checksums
- [ ] algorithm

### Assumptions

- Use Python standard library only, no 3rd party dependencies
- Allow any supported Python version, today 3.8 ~ 3.12
- Distribute as a single file, `package_statistics.py`
- Keep dev-time stuff (tests, test data, scaffolding) separate

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
* ...