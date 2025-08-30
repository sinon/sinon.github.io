+++
title = "TIL: Flowistry tool to understand information flow in Rust"
date = 2025-08-28
[taxonomies]
tags = ["til", "rust", "debugging"]
+++

When watching the excellent talk [Rust for Everyone](https://www.youtube.com/watch?v=R0dP-QR5wQo) by Will Crichton the item that stood out as potentially most useful day to day was [Flowistry](https://github.com/willcrichton/flowistry). It is a VSCode extension, when a user clicks a variable the extension greys out all code that the variable does not interact with, it seems like it could be very useful when debugging.