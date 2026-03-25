# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0).

## [Unreleased]

## [0.3.0] - 2026-03-26

### Added

- Release-hook command template for chaining full release workflow (docs, changelog, version bump, tag, push) (#1)
- Project-aware template tailoring — templates are rendered with context from pyproject.toml and git at install time

## [0.2.0] - 2026-03-26

### Added

- Hook template for chaining release actions (documentation, changelog, release, tag, push) (#1)
- Documentation for included templates and release workflow in README
- Bootstrapped bellbird's own skills and commands into the repo
