# Why I Learned Rust and Why I Work on it

- 8/6/2021

I've been doing stuff in Rust for a number of years now, and I wanted to explain my choice of
language so if someone else comes along they have more information than I did to explain why I
chose it as a language, and also what is actually feasible in Rust. Because of the
delay, I might be back-justifying some choices I made before, but hopefully that makes them more
clear, not less so. Of course, there's only so many wise choices a 19 y/o can make, so probably
a really strong reason was getting on board that hype-train, but I think I wasn't that clueless
to see other good signs.

# Why I learned Rust

Back 5-ish years ago, when I was still a chick barely hatching from the egg, I was trying to
select a language to learn for future projects. I had previously used Javascript, and wanted to
have the ability to directly access APIs such as syscall, found the lack of types annoying, and
wanted something which was a bit faster. I had picked up [Golang](https://golang.org/) after
that, because it seemed to be an easy enough bridge, and that was true. I certainly learned a
lot about asynchronous code, benchmarking, and what it means to write butt-ugly code. Golang was
a great step for learning, but I found that I wanted to go _even deeper_ (and also generics
pls).

Thus, the criteria I had for my next language were: a systems language, with an elegant type
system, that can be used for general purpose stuff (but also preferably graphics since that was
what I was working on at the time). This ruled out languages like Python (too slow because it's
dynamic), Erlang/Elixir (runs on a VM which has slower numerical computation than most
languages), and things like OCaml or Haskell (which are not systems languages). The main choices
were C, C++, and Rust.

- Out of those, I avoided C because I knew it had a ton of difficult to understand edges that were
  easy to cut yourself on, it was ugly and hard-to-read, and it was hard to compile on different
  systems.

- C++ was a pretty strong contender, a ton of libraries are in C and C++, so using C++ would
  give me the power to use all of those. But after trying to read through some random person's
  interpretation of what C++ should be (scattering random combinations of features akin to a
  Pollack painting), I decided it would be best to avoid C++ as well.

- Rust, the last candidate, was definitely not perfect either. What is this borrow checker that
  everyone's whining about in posts? Since it's new, the flaws are more hidden... but the syntax
  seems pleasant enough.

Note: Nim I don't have a strong reasoning for or against. I wasn't super compelled to
investigate it thoroughly, it just kind of exists and is probably in a similar state to Rust.

---

# Why I work on Rust

While I was very excited to pick up Rust, it took me quite a while to get into it. Despite the
many books and introductions to it, the Borrow Checker is a major pain in the ass to figure out.
In addition, coming from a much less systems-y background, it was not so clear what the costs of
a lot of things were, such as `Box`, `Vec`, and when it was better to pass by reference to a
`Vec` or pass a reference to a slice (i.e. `&[T]`), pass by value, when to return an `impl
Iterator`, when to use an `enum` versus a `trait` for finite sets of objects, and many other
small details which are hard to pick up.

Of course, these are all surmountable with time, and I think as I continued to learn, I
continued to imagine what I expected Rust to be. Sometimes, I would hope some feature was
implemented, such as const-generics. Since Rust is a relatively young language, it is missing a
lot of these features, so I would often hit walls where I would expect something to be
implemented and it simply wasn't yet.

Fortunately, at that time Rust has a very friendly community, so I started doing work on Rust in
order to fill in the gaps. I've ended up working more on Rust than anything else in Rust, which
is an odd place to be, because I don't have the context of applications about what is missing
from Rust that needs to be added. I am very grateful that the community is friendly, and I think
the most I've gained out of Rust has been from working on the compiler.

I think the point I'm trying to make is that I think Rust still has a lot of missing components
that would make it a lot friendlier to use as a language, but it has a lot of potential to grow,
so if you're interested in it, you can put your energy to work on the compiler. The one thing I
am worried about is that because of such high interest in it, rather than encourage growth, it
may lead to a lot of churn, and slow down it's growth rather than speed it up. What will happen
is still unclear, so I think for me the best is to keep contributing to what I can.


