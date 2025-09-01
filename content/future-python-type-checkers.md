+++
title = "How Well Do New Python Type Checkers Conform? A Deep Dive into Ty, Pyrefly, and Zuban"
date = 2025-08-29
description = "A comparison of three new Rust-based Python type checkers through the lens of typing spec conformance: Astral's ty, Meta's pyrefly, and David Halter's zuban"

[taxonomies]
tags = ["rust", "python", "type-checkers", "typing"]
+++

- [Introduction](#introduction)
  - [The Incumbents](#the-incumbents)
  - [The Newcomers](#the-newcomers)
    - [`ty` from Astral](#ty-from-astral)
    - [`pyrefly` from Meta](#pyrefly-from-meta)
    - [`zuban` from David Halter](#zuban-from-david-halter)
- [Typing Conformance Suite Analysis](#typing-conformance-suite-analysis)
  - [Summary](#summary)
  - [Review of progress](#review-of-progress)
  - [Relevance?](#relevance)
    - [The Gap Between Conformance and Real-World Usage](#the-gap-between-conformance-and-real-world-usage)
    - [Practical Experience vs. Test Scores](#practical-experience-vs-test-scores)
    - [What This Means for Adoption Decisions](#what-this-means-for-adoption-decisions)
- [Other resources to learn more](#other-resources-to-learn-more)
- [Footnotes](#footnotes)

# Introduction

The Python type checking landscape is experiencing a particularly active phase of innovation in 2025. This year has witnessed the emergence of not one, not two, but **three** new Python type checking tools, each backed by significant pedigree and resources. While these tools have slightly different goals and philosophies, they share a common foundation: all are built in Rust with performance as a core design principle.

This continued shift toward Rust-based implementations represents a significant evolution in the Python tooling ecosystem, promising faster type checking, better IDE integration, and improved developer experience for large codebases.

## The Incumbents

Before examining these new Rust-based tools, it's worth understanding the current landscape of Python type checkers that have established the foundation for static typing in Python:

**mypy** - The original and most widely adopted Python type checker, developed by Jukka Lehtosalo and now maintained by the mypy team. As the reference implementation for Python's type system, mypy has shaped many of the conventions and behaviors that newer tools aim to be compatible with. It's written in Python and offers comprehensive type checking capabilities, though performance can become a bottleneck on large codebases.

**pyright/Pylance** - Microsoft's type checker written in TypeScript/Node.js. Pyright powers the Pylance extension in VS Code and is known for its fast performance and strong IDE integration. It often implements new typing features before other checkers and provides rich editor feedback, making it popular among developers who prioritize IDE experience.

**pyre** - A type checker from Meta, written in a mix of OCaml and Python. Designed to handle Meta's massive Python codebase, pyre introduced several performance optimizations and incremental checking capabilities. However, Meta is now developing pyrefly as pyre's successor.

**pytype** - Google's type checker that takes a unique approach by performing type inference on unannotated Python code. Unlike other checkers that primarily validate existing type annotations, pytype can infer types from runtime behaviour and generate stub files for gradual typing adoption. Written in Python, it's particularly useful for analysing legacy codebases without type hints. However, Google announced in 2024 that pytype is being deprecated and Python 3.12 will be the last supported version of Python.

## The Newcomers

### `ty` from Astral

**Repository:** <https://github.com/astral-sh/ty/>  
**Development Repository:** <https://github.com/astral-sh/ruff/> 

**Key Highlights:**

- Strong focus on gradual guarantee principles
- Planned tight integration with Astral's existing linting tool `ruff`, with the aim to support type based linting rules.[^1]
- Backing from a team combining Python core developers and very experienced Rust tooling developers
- Incremental computation at the function level leveraging the [salsa](https://github.com/salsa-rs/salsa) library used by [rust-analyzer](https://github.com/rust-lang/rust-analyzer/). This could be particularly important on the LSP that `ty` provides to give very quick/responsive feedback loops in code editors.

**Philosophy:** Astral's approach emphasizes reliability and gradual adoption, making it easier for teams to incrementally add type checking to existing codebases without overwhelming developers with potential false positives.

### `pyrefly` from Meta

**Repository:** <https://github.com/facebook/pyrefly>  

**Key Highlights:**

- Successor to Meta's existing [pyre](https://github.com/facebook/pyre-check) type checker, designed to eventually replace it
- Enhanced type inference capabilities by default
- Potentially higher upfront adoption cost due to aggressive inference which might flag issues with correct code
- Backed by Meta's substantial engineering resources and real-world usage at scale

**Philosophy:** Meta prioritizes powerful inference and catching more potential issues out of the box, even if this means a steeper learning curve for teams new to type checking.

### `zuban` from David Halter

**Homepage:** <https://zubanls.com/>  
**Documentation:** <https://docs.zubanls.com/en/latest/>

**Key Highlights:**

- Created by the author of the popular Python LSP tool `jedi`
- Aims for high-degree of compatibility with `mypy` to make adoption in large existing codebases seamless.
- Not FOSS[^2], will require a license for codebases above 1.5 MB (~50,000 lines of code)[^3].
- Currently maintained by a single author seems a potential risk to long-term sustainability as Python typing does not stand still.

**Philosophy:** Zuban aims to provide the smoothest possible migration path from existing type checkers, particularly `mypy`, making it attractive for organizations with substantial existing typed codebases.

# Typing Conformance Suite Analysis

The Python Typing Council maintains a [Conformance test suite](https://github.com/python/typing/tree/main/conformance) which validates the behaviour of static type checkers against the expectations defined in the [Python typing specification](https://typing.python.org/en/latest/spec/index.html).

`ty` and `pyrefly` have not yet been added to the conformance suite, so it's harder to establish a baseline for their progress on this front.

To help resolve this gap I have [expanded the current test harness to support both of them](https://github.com/sinon/typing/pull/1)[^4], this also adds some additional debugging information to the html report to show the split between false negatives and false positives that the suite has detected in each test case.

I've also included a local build of `ty` for two main reasons:

- I've wanted to investigate contributing to `ty` and/or `ruff` for a while, so this was good impetus to get things set up.
- `ty` releases are cut relatively infrequently and I am impatient.

## Summary

__Generated 29/08/2025__

> NOTE
>
> The following section is slightly unfair, all of these tools are in alpha and only one of these tools (Zuban) has opted into the Conformance suite. This was mainly driven by own curiosity and seemed like an interesting project to understand the conformance test suite better.
>
> That being said even though `ty` is lagging on this metric at the moment it is still the type checker that I am most excited to use long-term because of the quality of the tooling Astral has built so far.

|                  Type Checker                   | Total Test Case Passes | Total Test Case Partial | Total False Positives | Total False Negatives |
| :---------------------------------------------: | :--------------------: | :---------------------: | :-------------------: | :-------------------: | 
|                  zuban 0.0.20                   |           97           |           42            |          152          |          89           |
|    ty 0.0.1-alpha.19 (e9cb838b3 2025-08-19)     |           20           |           119           |          371          |          603          |
| Local:ty ruff/0.12.11+27 (0bf5d2a20 2025-08-29) |           20           |           119           |          370          |          590          |
|                 pyrefly 0.30.0                  |           81           |           58            |          100          |          187          |

## Review of progress

`zuban` has a lead, having full `Pass` on ~69% of test cases, compared with ~15% for `ty` and ~58% for `pyrefly`. Which makes sense as though it's released in a similar time period to `ty` and `pyrefly` it has been in active development in private for several years.

The thing that surprised me more was how much progress `pyrefly` has made when compared to `ty`. Both broke cover and released their first advertised alpha builds around the same time, in the run up to PyCon 2025. This can maybe be partially explained from a point raised in [Edward Li's excellent blog post on the Typing Summit at PyCon 2025][1] which mentions that the `pyrefly` team devoted a lot of up-front time to solving some of the hard problems, such as generics.

## Relevance?

I initially came across the conformance test suite because `ty` runs every PR against the test suite and diffs the PR results against the results from `main` to ensure changes are desired. From this it's become a surprisingly useful learning tool for some of the more advanced typing topics, but the advanced nature of these topics raises an important question: **how relevant is the conformance suite pass rate for the average Python developer?**

### The Gap Between Conformance and Real-World Usage

The conformance test suite focuses heavily on advanced typing features that, while important for the specification, may not reflect the day-to-day typing needs of most Python codebases. Many of the test cases cover complex scenarios involving:

- Advanced generic variance and bounds
- Complex protocol inheritance hierarchies  
- Edge cases in structural subtyping
- Intricate interactions between multiple typing features

In contrast, the majority of Python codebases primarily use:

- Basic type annotations (`str`, `int`, `List[str]`, etc.)
- Simple class hierarchies
- Optional types and Union types
- Basic generic containers

### Practical Experience vs. Test Scores

My experience using the `ty` VSCode extension in place of `Pylance` across various projects and libraries tells a different story than the conformance test scores suggest. Despite `ty`'s relatively low 15% full pass rate, it has been surprisingly effective at catching real bugs and providing useful feedback for common typing patterns.

This suggests that while conformance test coverage is important for specification compliance and handling edge cases, it may not be the best predictor of a type checker's utility for everyday Python development. The features that matter most for typical codebases appear to be working well across all three tools, even when they struggle with more esoteric typing scenarios.

### What This Means for Adoption Decisions

For teams evaluating these type checkers, the conformance scores provide valuable insight into specification compliance, but shouldn't be the sole deciding factor. Consider:

- **For greenfield projects**: Any of these tools will likely handle your immediate needs well
- **For large, complex codebases or libraries leaning on more esoteric generic patterns**: Higher conformance scores may indicate better handling of advanced patterns you might encounter
- **For teams new to typing**: The difference in conformance scores may be less relevant than IDE integration, error message quality, and performance

# Other resources to learn more

- [Edward Li's excellent blog post comparing `ty` and `pyrefly`][1] which also contains the videos recorded at the PyCon typing summit which both `ty` and `pyrefly` gave presentations at.
- [Happy Path Programming - 114 ty: Fast Python Type Checking with Carl Meyer](https://www.youtube.com/watch?v=V1OmqEYoSz4)
- [Happy Path Programming - 115 More Python Type Checking! Pyrefly with Aaron Pollack & Steven Troxler](https://www.youtube.com/watch?v=huHF0Rv8L14)
- [Talk Python - ty: Astral's New Type Checker (Formerly Red-Knot)](https://talkpython.fm/episodes/show/506/ty-astrals-new-type-checker-formerly-red-knot)

# Footnotes

[^1]: Which can be demonstrated in the [open issues](https://github.com/astral-sh/ruff/issues?q=is%3Aissue%20state%3Aopen%20label%3Atype-inference ) on ruff tagged with `type-inference` which are bugs or new features that can only be resolved with `ruff` having access to deeper type inference data that `ty` can supply. 
[^2]: David has indicated a plan to make [source available in the future](https://github.com/python/typing/pull/2067#issuecomment-3177937964) when adding Zuban to the Python typing conformance suite.
[^3]: Full pricing information at: <https://zubanls.com/pricing/>
[^4]: This is just for this blog post, no plans to seek merging this.

<!-- Reference links --->
[1]: https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/
