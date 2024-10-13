+++
title = "Starting a blog"
date = 2024-10-13

[taxonomies]
tags = ["blogging", "zola"]
+++

- [Why start a blog?](#why-start-a-blog)
- [The nuts and bolts](#the-nuts-and-bolts)
  - [Why Zola?](#why-zola)
  - [Why Github Pages?](#why-github-pages)
- [Footnotes](#footnotes)

As a backend engineer with over a decade of experience,
I've spent countless hours diving deep into code, architecting systems, and solving complex problems.
But recently, I've felt a growing urge to step out of my comfort zone and embark on a new challenge: starting a blog.
In this post, I'll share my motivations for this journey and explain in brief some of the reasons for choosing Zola and Github Pages.

## Why start a blog?

- In my current and past roles I have tried to follow parts of the recommendations in
[Always be quitting][1] when it comes to documenting various aspects of my role.
The problem with this is that even when it's a generic explainer or How To this information is lost to me once I move roles.
- Personal wiki / Zettelkasten system: Memory is imperfect and trying to find the same piece of information
to something you have already encountered can be a frustrating experience.
- [Rubber duck debugging][2][^1] or How To generators. This technique for solving a problem when
combined with posting the updates in Slack or Teams naturally leads to a set of useful
textual information, transforming this into a blog item that might help someone else or maybe more importantly my future self
facing the same problem again is an attactive proposition.
- [Complex Systems Podcast][3]: I have recently been enjoying the podcast Complex Systems hosted by Patrick McKenzie (Patio11)
which in many of it's episodes re-enforces the role of regular written communication and the benefits of it in
critical thinking and self-examination.
- "Show your workings": During secondary school it was drilled into me to always show my workings,
the right answer wasn't always enough, demonstrating how you came to that answer was almost as important[^2].
This is something I didn't value at the time but found time and again in my professional life that
following this mantra solved or prevented many a problem from developing.

## The nuts and bolts

### Why Zola?

- It's written in Rust :zap:. There is my on-going side project to get more proficient at Rust and find avenues for to leverage and embed this learning.
So [Zola][4] being written in Rust was a big plus, in the hope that if I started blogging regularly I might find
reason to delve into some OSS contributions in Zola itself.
- It's a SSG (Static Site Generator) which works nicely with Github Pages
- Builds off strong pre-existing tooling such as Hugo, Pelican and Jeykyll
- Uses a template engine Tera, which will be familiar from my time using Jinja2 / Django
- Content written in CommonMark (expanded with some Github flavour via [`pulldown-cmark`][5]).

### Why Github Pages?

No real thought went into this choice, it was the default. Maybe in the future I will actually
examine other options. This is mainly that it's free, easy and fits easily into my usual
development flows.

## Footnotes

[^1]: Here is my current partner in debugging:
<!-- TODO: Update this with real picture-->
![Image of Dark Souls Rubberduck](https://m.media-amazon.com/images/I/81Yfyhw-QkL.__AC_SX300_SY300_QL70_ML2_.jpg)
[^2]: especially for the cases where you were actually wrong

<!-- Reference links --->
[1]: https://jmmv.dev/2021/04/always-be-quitting.html
[2]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[3]: https://www.complexsystemspodcast.com/
[4]: https://getzola.org
[5]: https://pulldown-cmark.github.io/pulldown-cmark/cheat-sheet.html
