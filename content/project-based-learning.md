+++
title = "Project based learning"
date = 2025-02-07
draft = true

[taxonomies]
tags = ["rust", "learning"]
+++

- [Why?](#why)
- [Previous Learning Attempts](#previous-learning-attempts)
- [Project based learning](#project-based-learning)
  - [Pngme](#pngme)
  - [CodeCrafters](#pngme)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Footnotes](#footnotes)

Learning a new programming language is like building muscle - sporadic gym visits won't get you far. After years of starting and abandoning Rust, I finally found a learning approach that sticks: hands-on projects that force you to write real code. This post traces my journey from tutorial hell to actually building things, and shares what worked (and what didn't) in hopes of helping others avoid the same pitfalls.

## Why?

Always wanted to learn Rust, with several false starts along the way. The appeal is clear - Rust consistently ranks as the most loved programming language in Stack Overflow's annual developer survey for the past 8 years. It promises memory safety without garbage collection, fearless concurrency, and zero-cost abstractions.

Modern systems programming demands better tools, and Rust delivers with its strict compiler, excellent tooling, and growing ecosystem. For a Python developer like myself, it offers a path to writing performant, safe code without sacrificing productivity.

## Previous Learning Attempts

My Rust journey has been a series of starts and stops:

Pre-1.0 (2014): A brief experiment that ended quickly after writing a few basic functions. The borrow checker won that round.

2020: My wife gifted me "The Rust Programming Language" book after overhearing my interest in Rust podcasts (particularly Rustacean Station). Finished the book and completed various small contained code examples but it was never put in to practice and started to fade.

2023: Two more serious attempts:

- Explored Rust + Kafka integration for a work proposal
- Started "Zero to Production in Rust" in October

Late 2023: Returned to coding with Advent of Code. While this got me writing Rust daily, I soon began to spend more time learning AoC problem-solving patterns than Rust idioms.

2024: Started preprating for another AoC attempt starting with some prep in November, more focused this time but still searching for a better learning approach.

## Project based learning

It was around this time when trying to form the habit of writing Rust with the aim of working through AoC2024 that I can across the suggestion of [PNGme][1] in a response to a similar request for guidance from someone learning Rust in [r/rust][4]

### PNGme

PNGme bills itself as "An Intermediate Rust Project". It comprsises of a series of Chapters each with a clear goal to build some functionality that will eventually evolve into a CLI tool for reading PNG files and then embedding or secrets messages stored within. Almost as important as the guidance are the suite of tests to verify each chapter as you go.

[My work][5] on this has expanded as the simple library has become a test bed to experiement with other parts of the Rust ecosystem such as

- Python to Rust binding with pyO3[6] by building a [PNGme python library][7] from the Rust library.
- Experimenting with GUI toolkit [`eframe`][8] using [`egui`][9] by building a [GUI interface for PNGme][10].
- A [html frontend for PNGme][11] using Maud and Axum.
- Splitting a codebase into various crates in a single workspace.

### Programming Projects for Advanced Beginners

Upon finishing up PNGme the author gives some suggestions of other projects based learning resources, one of which was [Programming Projects for Advanced Beginners][3] a blog series by Robert Heaton which consist of prompts for small self-contained projects and some guidance on how you might approach and structure solving them.

These led nicely into experimenting with [`ratatui`][12] a library designed to help you to build Text User Interfaces (TUIs) resulting in:

- [`gridlife`][13]: A library and TUI CLI for simulating Conways Game of Life automatons. Which in some "the interest is smaller than you think", one of the maintainers of `ratatui` (Orhun Parmaksız) filed an issue on my repo, asking for some changes so they could use it in a website they were building. The reason I used `ratatui` in the first place was because of watching [a talk Orhun gave at EuroRust][14]. This also gave me the nudge I needed to publish the library to `crates.io`.
- A functionality unfinished [snake][15] game.

### CodeCrafters

After PNGme's success, I discovered [CodeCrafters][2] through Jon Gjengset's videos. The platform offers hands-on projects where you build clones of real-world tools: Git, Redis, Docker, and more. Each project breaks down into small, testable steps with clear feedback.

What sets CodeCrafters apart is its focus on real-world implementations rather than toy problems. Building a BitTorrent client or Redis server forces you to understand both Rust and the underlying protocols. The automated tests provide immediate feedback, while the step-by-step progression keeps you motivated.

The projects I worked on via CodeCrafters are:

- [`loxide`][16] - An implementation of an interpreter for the Lox language by Robert Nystrom for his excellent (and free) book [Crafting Interpreter][17]. Which has given me a new appreciation for my 4 years studying Computer Science and wishing as a new engineer all those years ago I had some work projects that would have slowed down the atrophy of all that theory that I never put into practice to make it stick.
- [`rsh][18] - A bare bones POXIS shell.

## Conclusion and Next Steps

Looking back on the last 3-4 months I am frankly shocked by how productive I have been, in that span of time I have done more development work for my own pleasure than I had in the nearly 10 years preceding it.

## Footnotes

<!-- Reference links --->
[1]: https://jrdngr.github.io/pngme_book/
[2]: https://codecrafters.io/
[3]: https://robertheaton.com/2018/12/08/programming-projects-for-advanced-beginners/
[4]: https://old.reddit.com/r/rust
[5]:https://github.com/sinon/pngme/
[6]: https://pyo3.rs
[7]: https://github.com/sinon/pngme/tree/main/crates/pngme-python
[8]: https://docs.rs/eframe/
[9]: https://docs.rs/egui/
[10]: https://github.com/sinon/pngme/tree/main/crates/pngme-gui
[11]: https://github.com/sinon/pngme/compare/main...pngme-www
[12]: https://docs.rs/ratatui
[13]: https://docs.rs/gridlife
[14]: https://www.youtube.com/watch?v=hWG51Mc1DlM
[15]: https://github.com/sinon/snake
[16]: https://github.com/sinon/loxide
[17]: https://craftinginterpreters.com/
[18]: https://github.com/sinon/rsh
