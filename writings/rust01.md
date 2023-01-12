# Why I Learned Rust and Why I Work on it

- 8/6/2021 | Updated 1/11/2023

I've been coding in Rust for a few of years now, and it has been an up and down experience.
I want to explain my choice of language so if/when someone else is picking a language they have
more information than I did to help decide if it is the language for them and also to help
indicate what is actually feasible in Rust.
Because of the delay in writing this since when I first started, I may be artificially justifying
some choices I made before, but hindsight is 20/20.

Back then, Rust was definitely on a bit of a hype train, but I believe it has become a language
in many ways that does not require hype.

# Why I learned Rust

Back 5-ish years ago, when I was still naive to what programming was, I was trying to
pick a language to learn and use in future projects. I had previously used Javascript,
and wanted to have the ability to directly access APIs such as system calls, had found the lack of types annoying, and
wanted something which faster. My initial choice was [Golang](https://golang.org/)
partially because it seemed to be an easy bridge from JavaScript, and it filled the itch of a
new language. From Golang I learned about asynchronous code, benchmarking, and what it means to
write ugly Production-Ready™️  code. Golang was a great step for learning, but I found that I
wanted to go _even deeper_ and also be able to write more generic code.

Thus, the criteria I had for my next language were: a systems language, with a good type
system, that can be used for general purpose stuff (but also preferably graphics since that was
what I was working on at the time). This ruled out languages like Python (too slow because it's
dynamic), Erlang/Elixir (runs on a VM which has slower numerical computation than most
languages), and things like OCaml or Haskell (which are not systems languages). The main choices
were C, C++, and Rust.

- Out of those, I avoided C because I knew it had a ton of difficult to understand edges that were
  easy to cut yourself on, it often requires re-writing many different components instead of
  using libraries, and can be hard to compile on different systems.

- C++ was a pretty strong contender, a ton of libraries are in C and C++, so using C++ would
  give me the power to use all of those. But after trying to read through different
  C++ codebases which often use a plethora of different techniques, a high amount of macros, and
  often appear to be a wild combination of each author's own DSL, I decided it would be best to avoid C++ as well.

- Rust, the last candidate, was definitely not perfect either. What interested me was the
  combination of the generic type system, the semi-elegant syntax, the package manager, and
  simplicity as compared to C++. There were a lot of downsides though, notably it did not seem
  to be the most mature, as many parts of the compiler were under development. In addition, many
  libraries for Rust were not mature (pre-alpha). In the end, this isn't too bad, as most of the
  applications I wanted it for were fun to build by myself, but it makes it harder to use the
  language for larger projects where it doesn't make sense to build everything by hand.

Note: Nim I don't have a strong reasoning for or against. I wasn't super compelled to
investigate it thoroughly, it just kind of exists and is probably in a similar state to Rust.

## Why I work on Rust

While I was very excited to pick up Rust, it took me quite a while to get into it. Despite the
many books and introductions to it, the Borrow Checker is a major pain in the ass to figure out.
In addition, coming from a much less systems-y background, it was not so clear what the costs of
a lot of things were, such as `Box`, `Vec`, and when it was better to pass by reference to a
`Vec` or pass a reference to a slice (i.e. `&[T]`), pass by value, when to return an `impl
Iterator`, when to use an `enum` versus a `trait` for finite sets of objects, and many other
small details which are hard to pick up.

Of course, learning these things is possible with time, and as I continued to learn, I
continued to imagine what I expected Rust to be. Sometimes, I would hope some feature was
implemented, such as const-generics. Since Rust is a relatively young language, it is missing a
lot of these features, so I would often hit walls where I would expect something to be
implemented and it simply wasn't yet.

Fortunately, at that time Rust had a very friendly community which was open to many different
contributions, so I started doing work on Rust in
order to fill in the gaps. I've ended up working more on Rust than anything else in Rust, which
is an odd place to be, because I don't have the context of applications about what is missing
from Rust that needs to be added. I am very grateful that the community is mostly friendly,
and I think the most I've gained out of Rust has been from working on the compiler.

What do I think is missing from Rust? I believe that many core Rust contributors view Rust to be
some parts a research language, some parts a systems language. For me though, first and foremost
is that it must be a language that is used. What I mean by that is that even if it is a research
language and has many interesting compilation tools, the front-end should still fundamentally
follow Ruby's principle of "Least Surprise". What that means is that Rust's syntax for a user
should immediately be obvious, and things that a user can imagine to work should work out of the
box. I think in this regard, Rust still has a lot of progress to make. This may also bear
entirely from my personal experience, but I find that often the trait system is quite difficult
to understand when using it in even slightly off-the-beaten-path ways.

I do think that Rust is continually moving in a good direction, in that the compile-times are
being reduced, there are good diagnostics that are being added into the language, and there are
many new applications which no longer advertise as being "rewritten-in-rust".

To me, Rust is a joy to work on, although it is painful at times because of difficulty
communicating with contributors in Europe and slow compile times, and I am glad that I am able
to work on it.

#### Aside

I found the environment was not the most welcoming in person. While I was interning at google, I
found that people looked down on my lack of knowledge. I remember an exchange with someone where
I had said that Rust was not mature for graphics APIs. They suggested I used
[Vulkano](https://github.com/vulkano-rs/vulkano), which, as of 3 years later, is still in
pre-Alpha, and essentially dismissed my thoughts. I've also found some contributors to the Rust
language to be more dismissive which has not always been the most pleasant experience. For the
most part, the Rust community has been good, but these incidents have made it worse for me.
