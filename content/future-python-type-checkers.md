+++
title = "Ty versus Pyrefly versus Zuban: Reviewing the future of Python type checkers"
date = 2025-08-29
description = "A comparison of three new Rust-based Python type checkers: Astral's ty, Meta's pyrefly, and David Halter's zuban"
draft = true

[taxonomies]
tags = ["rust", "python", "type-checkers", "typing"]
+++

# Table of Contents

- [Introduction](#introduction)
    - [`ty` from Astral](#ty-from-astral)
    - [`pyrefly` from Meta](#pyrefly-from-meta)
    - [`zuban` from David Halter](#zuban-from-david-halter)
- [Typing Conformance Suite Analysis](#typing-conformance-suite-analysis)
    - [Summary](#summary)
    - [Review of progress](#review-of-progress)
- [Other resources to learn more](#other-resources-to-learn-more)
- [Footnotes](#footnotes)

# Introduction

The Python type checking landscape is experiencing a particularly active phase of innovation in 2025. This year has witnessed the emergence of not one, not two, but **three** new Python type checking tools, each backed by significant pedigree and resources. While these tools have slightly different goals and philosophies, they share a common foundation: all are built in Rust with performance as a core design principle.

This continued shift toward Rust-based implementations represents a significant evolution in the Python tooling ecosystem, promising faster type checking, better IDE integration, and improved developer experience for large codebases.


## `ty` from Astral

**Repository:** <https://github.com/astral-sh/ty/>  
**Development Repository:** <https://github.com/astral-sh/ruff/> 

**Key Highlights:**
- Strong focus on gradual guarantee principles
- Planned tight integration with Astral's existing linting tool `ruff`, with the aim to support type based linting rules.[^1]
- Backing from a team combining Python core developers and very experienced Rust tooling developers
- Incremental computation at the function level leveraging the [salsa](https://github.com/salsa-rs/salsa) library used by [rust-analyzer](https://github.com/rust-lang/rust-analyzer/). This could be particularly important on the LSP that `ty` provides to give very quick/responsive feedback loops in code editors.

**Philosophy:** Astral's approach emphasizes reliability and gradual adoption, making it easier for teams to incrementally add type checking to existing codebases without overwhelming developers with false positives.

## `pyrefly` from Meta

**Repository:** <https://github.com/facebook/pyrefly>  

**Key Highlights:**
- Successor to Meta's existing [pyre](https://github.com/facebook/pyre-check) type checker, designed to eventually replace it
- Enhanced type inference capabilities by default
- Potentially higher upfront adoption cost due to aggressive inference which might flag issues with correct code
- Backed by Meta's substantial engineering resources and real-world usage at scale

**Philosophy:** Meta prioritizes powerful inference and catching more potential issues out of the box, even if this means a steeper learning curve for teams new to type checking.

## `zuban` from David Halter

**Homepage:** <https://zubanls.com/>  
**Documentation:** <https://docs.zubanls.com/en/latest/>

**Key Highlights:**
- Created by the author of the popular Python LSP tool `jedi`
- Aims for high-degree of compatibility with `mypy` to make adoption in large existing codebases seamless.
- Not FOSS[^2], will require a license for codebases above 1.5 MB (~50,000 lines of code)[^3].
- Currently maintained by a single author seems a potential risk to long-term sustainability as Python typing does not stand still.

**Philosophy:** Zuban aims to provide the smoothest possible migration path from existing type checkers, particularly `mypy`, making it attractive for organizations with substantial existing typed codebases.


# Typing Conformance Suite Analysis

The Python Typing Council maintains a [Conformance test suite](https://github.com/python/typing/tree/main/conformance) which validates the behavior of static type checkers against the expectations defined in the [Python typing specification](https://typing.python.org/en/latest/spec/index.html).

`ty` and `pyrefly` have not yet been added to the conformance suite, so it's harder to establish a baseline for their progress on this front.

To help resolve this gap I have [expanded the current test harness to support both of them](https://github.com/sinon/typing/pull/1)[^4], this also adds some additional debugging information to the html report to show the split between false negatives and false positives that the suite has detected in each test case.

I've also included a local build of `ty` for two main reasons:

* I've wanted to investigate contributing to `ty` and/or `ruff` for a while, so this was good impetus to get things set up.
* `ty` releases are cut relatively infrequently and I am impatient.

## Summary

| Type Checker                                    | Test Case Passes | Test Case Fails | Test Case Unknown status | False Positives | False Negatives |
|-------------------------------------------------|------------------|-----------------|--------------------------|-----------------|-----------------|
| zuban 0.0.20                                    | 96               | 38              | 5                        | 149             | 92              |
| ty 0.0.1-alpha.19 (e9cb838b3 2025-08-19)        | 20               | 0               | 119                      | 371             | 603             |
| Local:ty ruff/0.12.11+27 (0bf5d2a20 2025-08-29) | 20               | 0               | 119                      | 370             | 590             |
| pyrefly 0.30.0                                  | 81               | 0               | 58                       | 100             | 187             |

## Review of progress

`zuban` has a lead, having full `Pass` on ~69% of test cases, compared with ~15% for `ty` and ~58% for `pyrefly`. Which makes sense as though it's released in a similar time period to `ty` and `pyrefly` it has been in active development in private for several years.

The thing that surprised me more was how much progress `pyrefly` has made when compared to `ty`. This can maybe be partially explained from a point raised in [Edward Li's blog excellent post on the Typing Summit at PyCon 2025][1] which mentions that the `pyrefly` team devoted a lot of up front time into solving some of the hard problems, such as generics.


# Other resources to learn more

* [Edward Li's excellent blog post comparing `ty` and `pyrefly`][1] which also contains the videos recorded at the PyCon typing summit which both `ty` and `pyrefly` gave presentations at.
* [Happy Path Programming - 114 ty: Fast Python Type Checking with Carl Meyer](https://www.youtube.com/watch?v=V1OmqEYoSz4)
* [Happy Path Programming - 115 More Python Type Checking! Pyrefly with Aaron Pollack & Steven Troxler](https://www.youtube.com/watch?v=huHF0Rv8L14)
* [Talk Python - ty: Astral's New Type Checker (Formerly Red-Knot)](https://talkpython.fm/episodes/show/506/ty-astrals-new-type-checker-formerly-red-knot)


# Footnotes

[^1]: Which can be demonstrated in the [open issues](https://github.com/astral-sh/ruff/issues?q=is%3Aissue%20state%3Aopen%20label%3Atype-inference ) on ruff tagged with `type-inference` which are bugs or new features that can only be resolved with `ruff` having access to deeper type inference data that `ty` can supply. 
[^2]: David has indicated a plan to make [source available in the future](https://github.com/python/typing/pull/2067#issuecomment-3177937964) when adding Zuban to the Python typing conformance suite.
[^3]: Full pricing information at: <https://zubanls.com/pricing/>
[^4]: This is just for this blog post, no plans to seek merging this.


<!-- Reference links --->
[1]: https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/
