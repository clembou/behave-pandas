# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [0.5.0] - 2023-02-09
### Changed
- add explicit support for python 3.8, 3.9, 1.10 (#22)
- drop support for python 3.5 (#22)
- switch to Github Actions instead of Travis for CI (#22)
- add support for pandas 1.5 and numpy 1.24 (#20) - thanks @lkacenja!

## [0.4.0] - 2020-02-10
### Changed
- add explicit support for python 3.7 (#11)
- ensure ordered dict printing is tested (#14)
- support boolean, string, and Int64 new dtypes added in pandas v1.0 (GH-18)
- support pandas up to v1.0.1 -(GH-16)

### Deprecations
- the `str` column type is considered deprecated and will be removed in a future version. Use `object` or `string` (pandas v1.0+) instead.
- support for python 3.5 will be removed in a future version.
- support for `OrderedDict` will be removed in a future version. On python3.6+, use `dict` instead.

## [0.3.0] - 2019-01-16
- added support for `OrderedDict` objects (#10)
- format files using black (#12)

## [0.2.0] - 2018-06-03
### Changed
- added list and dict types  (#6)
- always use object as dtype when creating a string series  (#7)
- use native markdown support form pypi.org  (#5)
- typo in trove classifier

## [0.1.0] - 2018-02-10
### Added
- First release 🎉

[Unreleased]: https://github.com/clembou/behave-pandas/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/clembou/behave-pandas/commit/v0.4.0...v0.5.0
[0.4.0]: https://github.com/clembou/behave-pandas/commit/v0.3.0...v0.4.0
[0.3.0]: https://github.com/clembou/behave-pandas/commit/v0.2.0...v0.3.0
[0.2.0]: https://github.com/clembou/behave-pandas/commit/v0.1.0...v0.2.0
[0.1.0]: https://github.com/clembou/behave-pandas/commit/v0.1.0
