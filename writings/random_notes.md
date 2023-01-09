# Random notes!

- How to link a crate without using Cargo

```sh
# https://doc.rust-lang.org/rustc/command-line-arguments.html
rustc --crate-type [your crate kind] <input file(s)> -L dependency=<folder with crate>
  --extern <path to crate rlib>
```
Rather than figuring out how to run this myself, I had to figure this out using the verbose
output from Cargo. This is useful when performing some weird compilation magic.


---

I found that named functions in Rust do not implement traits. In order to ensure that they
implement a trait on `fn(*) -> *`, you have to cast `fn_name as fn(*) -> *`, which is confusing
at best and seems buggy at worst.

---
