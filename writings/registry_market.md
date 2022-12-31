# An approach to resolving too many packages in Registries

- January 5th, 2023

Prior Work:

- [Proposal for default crate recommendation ranking](https://github.com/rust-lang/rfcs/pull/1824)
- [Reddit: why so much garbage allowed in crates.io ?](https://www.reddit.com/r/rust/comments/nhcq9q/why_so_much_garbage_allowed_in_cratesio/)
- [Cargo Review](https://web.crev.dev/rust-reviews/)
- [add some discussion on crates.io to leave feedback \[...\]](https://github.com/rust-lang/crates.io/issues/452)
- [Comments on Crates?](https://github.com/rust-lang/crates.io/issues/1820)
- [Voting in Crates?](https://github.com/rust-lang/crates.io/issues/786)

For Javascript and Rust programmers, NPM and Cargo (`crates.io`) are great tools to managing and downloading
dependencies. Both NPM and Cargo are package registries which contain a plethora of packages
that can be used for any number of tasks. These stand in stark comparison to ad-hoc libraries
for C, which are maintained across a number of different locations, and do not have a simple
tool that can be used to manage a large number of them. Thus, they are a great improvement as
compared to that ecosystem.

Yet, one issue with these package registries is that they remain
inundated with a large number of redundant, useless, and poorly-documented packages, which are
indistinguishable without prying into documentation, READMEs, and occasionally even source code. Thus, while the ease of
downloading and publishing packages is much easier, it in some ways becomes easier for the
registry to get inundated with every Joe Schmoe's version of the same thing. Before NPM,
JavaScript was already being used to write massive applications, and thus many existing well-known
libraries were simply ported over so that people could more easily download them. With Rust and `crates.io`,
since they both came into the mainstream at approximately the same time, there were no well-known
libraries and thus discoverability outside of a few well-known libraries is difficult.

The issue with these registries now becomes a question of how to sort the wheat from the chaff,
finding diamonds in the rough. Is it that important? Yes, I don't want to download a dependency,
spend 8 hours figuring out how to use it, then decide it is awful and realize I wasted an
afternoon. Instead, I'd rather read something for 10 minutes that evaluates the efficacy of a
crate, and provide some assurance that I'm not wasting my time.

## User Reviews?

The easiest proposal would simply be to have user reviews. The problem with this issue is that
if you assume users are malicious, then it's not at all reliable. That's not to be said that
user reviews are completely bad. It's good to hear how other people are using libraries, because
there is no way to completely measure all qualities of a library. But that solution has been
beaten to death, and hasn't been implemented, so I'm going to kick that can into someone else's
yard.

Another mark against user reviews is that they may contain inappropriate information, and thus
require significant moderation effort. For repositories which are maintained by many fewer
people than those submitting or downloading crates, this is a prohibitive cost. Thus, any
measure of quality for a crate should likely be automated, or restricted to a trusted set of
people.

## Public Benchmarks

While reviews can be useful to determine if a library actually has any good traits, it doesn't
provide a useful way to compare it to another library. Instead, what may be a possible solution
is to also have the registry maintain a set of open source _benchmarks_.

#### Definition of "Benchmark"

It is important to carefully define what a "benchmark" is in this
case, since it may be different than its common use case in computing. What I mean by
"benchmark" is verification that a crate can perform a specific functionality. For example, for
a linear algebra crate, it may be useful to create a benchmark to demonstrate that it can invert
matrices of arbitrary sizes. For a data-structure crate, it would be useful to demonstrate that
the library correctly functions as a heap, tree, etc. These benchmarks do not necessarily need
to measure other metrics such as run-time or heap usage, but can be opted into doing so.

When a library gets published, it can implement a number of these common benchmarks, and if it
"passes" it is displayed as implementing the benchmark. For optional metrics, they can be listed
on a leaderboard. By having a common benchmark which is run by a 3rd party, every schmuck can show
how bad (or not) their library is, and someone looking for a library can then use a single benchmark
as a way to evaluate whether a library is usable or not. The benchmarks are published on the registry
with some number of tags describing each benchmark/tests use-case. For the end user, they can
now examine benchmarks to look for implementing crates instead of searching for a crate that can
satisfy their needs.

While it is possible that a 3rd party generate these benchmarks, having them be tightly
integrated with the registry provides a few nice benefits. First, it provides centralization, a
library implementor doesn't need to maintain multiple accounts to manage benchmarks versus
publishing. Second, the result of a benchmark is tightly integrated with the version of a crate
and thus, the benchmarks can be listed directly with the libraries alongside the
implementing version, and a user can then use it to track progress of development of a crate.


The purpose of the benchmarks are primarily to:
- Demonstrate what features the crate has, and show a canonical way of implementing something with
  the crate.
- Create a standardized way to measure performance on different tasks across a variety of
  crates.

This would allow crates which are well written but lost in the sea of crates to have an
objective way to demonstrate their quality.

## Issues with Public Benchmarks

- Manipulation of Benchmarks:
  A malicious library owner may create an implementation that performs well on a benchmark, but
  poorly in general or does not work.

  By forcing implementations to be open-source, these implementations can be manually verified
  by users, and poor implementations can be flagged.

- Cost of running a benchmark:
  It is non-trivial to run benchmarks for many projects, thus initially it would likely make
  sense to rate-limit each user over all their crates to a fixed amount. This would also prevent
  malicious users from spamming the benchmark.

  One note is that users should be able to run benchmarks as much as they want locally, to
  verify correctness.

- Creation of benchmarks:
  There is an additional burden of creating benchmarks, so it is unclear who would create them.

  But library owners are incentivized to create them if they do not exist, or implement them if
  they do. By creating a benchmark, they are able to demonstrate that their library works well.

  It should be noted that it is important that not every crate creates its own benchmark, and
  instead most crates implement them. Creation of crates could be managed by a team, such as the
  `crates.io` team, but implementation can be done independently by each library owner.

- The task must be isolated, and performable without special hardware.
  This issue is not so easily resolved for all crates. For example, embedded crates would not be
  easily tested. For isolated tasks, such as algorithm/data-structure implementations, linalg,
  autograd, or other tasks which do not require shelling out to a complex system, I believe this
  would work well.

## Implementation Details

In practice, what would this look like for a library owner? One possible way, specific to Rust,
is to provide a trait interface that a library must implement in a specific example file. TODO
in progress at this point.
