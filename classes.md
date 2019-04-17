# Classes

This is just a brief summary of some of my undergraduate courses, and what I've learned. I write
this here more so I don't forget, but hopefully it may be of some use to some people.

### Freshman Fall

This was my first semester, so I was taking a lot of prerequisite courses. I omitted two for
concise-ness.

- Introduction to Systems

In this class, I learned the basics of C, including pointer manipulation. Unfortunately, it was
taught under the assumption that we were using C90 or some older standard, under the pretense
that some systems still ran that. In addition the assignments were as follows:

1. Build a program that removes winged comments from files
The general idea of this assignment was to use a DFA(Deterministic Finite Automata AKA a state
diagram) and help teach C's general syntax. I found it to be excessive in the strictness of the
completeness of the DFA, because it made it much harder to implement certain cases assuming that
lookaheads weren't allowed.
2. Reimplement parts of `string.h`
This was fairly normal. The main thing I remember was talking to my TA about having `strlen(s)`
as the terminating conditional in a for loop. I made the assumption that the compiler would optimize
this into a constant outside of the loop, and it improved readability. I was told that this
could not be assumed, even though I'm still fairly sure I'm correct.
3. Implement a table which maps pointers to pointers.
4. Implement a fast fibonacci algorithm on an implementation of arbitrary precision numbers in
x86. In later versions of this course, it was updated to ARM with different objectives.

I think the choice to move to ARM was a smart one, as the main part of this assignment was
understanding the flags updated and changed by each instruction, and familiarizing myself with
the x86 ISA(instruction set architecture). I think the original assignment was super fun to
optimize, albeit awful to debug.
5. Build a set of files which when passed into a specific program cause it overflow and execute
arbitrary code.
6. Build a simple heap manager
I found this assignment to be too pipelined, in that the instructors gave way too much direction
in what to do, without letting students actually think about how to do it themselves. I often
considered emailing a TA with a reference to
[this](https://www.cs.cmu.edu/~bryant/pubdir/sigcse18.pdf), but I hesitate because I didn't
think they would receive it well.

7. Implement a multi-threaded Othello
This was the first time they tried this assignment, in lieu of making a shell. To me, the shell
would have been way more interesting, and actually further CS knowledge in that area. It was fun
to work on this for me though, because I made a Golang-esque abstraction for creating threads,
and thinking about how to build that made it fun. I think this was returned back to working on a shell,
and I hope that the next generation can do that instead.

- Multivariable Calculus

I took this course as a prerequisite to engineering. I found it to be not immediately applicable
to anything I've done thus far, but it definitely has its uses. I don't think I was as good at
math when I took this course, and I definitely would've spent more time trying to conceptualize
it now looking back. I don't think it's anywhere near as important as linear algebra. I really
enjoyed my Professor in this class though, because he would force everyone to talk, by going
around and asking us all a bit about how something worked. It might've been a little too much at
times, especially since not everyone was as strong at math as this was a pre-req class, but I
found it to keep the class engaging.

- History of Pirates

Yooooo, this class was dope. It was a seminar class offered only to first years, and I took it
on the recommendation of someone that I get out of my comfort zone. I definitely was not the
most historically versed person in that class, but I had a great time reading about the pirates
in both the Mediterranean and the Caribbeans. Not only were their adventures crazy in that a
couple hundred pirates would capture whole cities, but it was crazy to see how they actually
acted in a very democratic manner, where as most people have been trained to see pirates as
tyrannical and lawless. Pirates had honor amongst themselves, and the kinship they had during
their trials at sea is unimaginable to me.

### Freshman Spring

TODO
