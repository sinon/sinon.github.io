+++
title = "Stepping Out of My Comfort Zone: A Backend Engineer's Journey into Blogging"
date = 2024-10-13

[taxonomies]
tags = ["blogging", "zola"]
+++

- [Why start a blog?](#why-start-a-blog)
- [The nuts and bolts](#the-nuts-and-bolts)
  - [Why Zola?](#why-zola)
  - [Why Github Pages?](#why-github-pages)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Footnotes](#footnotes)

As a backend engineer with over a decade of experience,
I've spent countless hours diving deep into code, architecting systems, and solving complex problems.
But recently, I've felt a growing urge to step out of my comfort zone and embark on a new challenge: starting a blog.
In this post, I'll discuss my motivations for starting a blog and briefly explain my choice of tools: Zola and GitHub Pages.

## Why start a blog?

- **Preserving Knowledge across Roles**: In my current and past roles I have tried to follow parts of the recommendations in
[Always be quitting][1] when it comes to documenting various aspects of my role.
The problem with this is that even when it's a generic explainer or How To this information is lost to me once I move roles.
- **Personal knowledge management**: Memory is imperfect, and trying to find the same piece of information
you've already encountered can be frustrating. A blog can serve as a personal wiki or Zettelkasten system,
helping me organize and retrieve information more efficiently.
- **[Rubber duck debugging][2]**[^1]: This technique for solving problems when
combined with posting the updates in Slack or Teams naturally leads to a set of useful
textual information, transforming this into a blog item that might help someone else or maybe more importantly my future self
facing the same problem again is an attactive proposition.
- **[Complex Systems Podcast][3]**: I have recently been enjoying the podcast Complex Systems hosted by Patrick McKenzie (Patio11)
which in many of its episodes re-enforces the role of regular written communication and the benefits of it in
critical thinking and self-examination.
- **"Show your workings"**: During secondary school, it was drilled into me to always show my workings in mathematics and science.
The right answer wasn't always enough; demonstrating how you came to that answer was almost as important[^2]. While I didn't fully appreciate this at the time, I've found throughout my professional life that following this mantra has solved or prevented many problems from developing.

  Blogging serves as an excellent platform for "showing my workings" in my professional context.
  By writing about my problem-solving processes, architectural decisions, or even my learning journey,
  I'm not just sharing the final solution but the entire thought process behind it. This approach offers several benefits:

  - It helps me clarify my own thinking and often leads to new insights.
  - It provides a valuable resource for others who might be facing similar challenges.
  - It creates a record of my decision-making process, which can be incredibly useful when revisiting projects or defending choices later on.
  - It encourages a culture of transparency and knowledge-sharing within the tech community.

  By treating my blog as a place to "show my workings," I'm not just creating content – I'm cultivating a habit of thorough analysis and clear communication that will serve me well throughout my career.

## The nuts and bolts

### Why Zola?

- It's written in Rust :zap:. There is my on-going side project to get more proficient at Rust and find avenues for to leverage and embed this learning.
So [Zola][4] being written in Rust was a big plus, in the hope that if I started blogging regularly I might find
reason to delve into some OSS contributions in Zola itself.
- It's a SSG (Static Site Generator) which works nicely with Github Pages.
- Builds off strong pre-existing tooling such as Hugo, Pelican and Jeykyll.
- Uses a template engine Tera, which will be familiar in syntax from my time using Jinja2 and Django.
- Content written in CommonMark (expanded with some Github flavour via [`pulldown-cmark`][5]).

### Why Github Pages?

No real thought went into this choice, it was the default. Maybe in the future I will actually
examine other options. This is mainly that it's free, easy and fits easily into my usual
development flows.

## Conclusion and Next Steps

Starting this blog represents a practical step in documenting my work and sharing knowledge. By using Zola and GitHub Pages, I'm balancing the desire to learn new tools with the need for a straightforward, low-maintenance platform.

Moving forward, I plan to focus on:

1. Documenting solutions to specific backend engineering problems I encounter
2. Sharing brief explanations of useful techniques or patterns from my daily work
3. Posting occasional updates on my progress with learning Rust and any Zola-related insights
4. Writing about system design decisions and trade-offs from recent projects

I don't have a fixed posting schedule, but I aim to write when I have something concrete and useful to share. The primary goal is to create a resource that's valuable for my future self, with the added benefit of potentially helping others facing similar challenges.

This blog is a work in progress, and its direction may evolve based on what I find most useful and manageable alongside my primary work. If you happen to find something helpful here, all the better.

## Footnotes

[^1]: Here is my current partner in debugging:
<center>
<img src="/RubberDuckDarkSouls.jpg" width="50%" height="50%" alt="Dark Souls Rubber duck"/>
</center>

[^2]: especially for the cases where you were actually wrong

<!-- Reference links --->
[1]: https://jmmv.dev/2021/04/always-be-quitting.html
[2]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[3]: https://www.complexsystemspodcast.com/
[4]: https://getzola.org
[5]: https://pulldown-cmark.github.io/pulldown-cmark/cheat-sheet.html
