# Ideas

This is a collection of a random ideas which I have not had time to work on, but someone else
may be able to pick up! While it might be good for me to just keep them to myself, I think it
would be more beneficial to put them out there.

These ideas are not well explained, partially because they are just ideas, but if they don't
make sense, oops.

---

- Dynamic Lock Ordering

In many applications, we may need to acquire multiple locks at a given time. In order to prevent
deadlock, one strategy is to keep a certain ordering over locks and only acquire them in that
order. But it's often not known ahead of time what order to acquire locks. Thus, we may want to
keep an ordered vector of locks, sorted by frequency or how long they've been held for. Then, if
we want to acquire a lock, we are only allowed to acquire a lock if none of the locks which are
less frequent/popular are acquired. The benefit of this would be that we can then reorder the
locks at runtime depending on these statistics.

- Perceptual Merkle Hash Tree

A Merkle Tree is useful for hashing 1D information such as text, but they do not extend to 2D
information such as images (where hashing is more rare anyway). Is there a way to define a hash
function that can generate another output image, and create a tree of such hashes? This may be
useful in something like perceptual hashing.

- Auto Entropy Computation

Understanding the information flow through a system might be useful for finding bugs, or while
training an ML model to see if it has saturated. We might be able to create a system that
automatically generates distributions of inputs, and computes entropy/mutual information within
a system. Whether this is useful/practical is something I have no idea about, and I also have no
clue whether this is feasible or not, or what it would exactly look like.
