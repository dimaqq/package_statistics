### Checklist

- [ ] this readme
- [ ] testing
- [ ] cover all supported Python versions
- [ ] validate downloaded file checksums
- [ ] algorithm

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