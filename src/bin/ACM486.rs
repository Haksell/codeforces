use codeforces::input;
use std::{cmp::min, iter::zip};

fn main() {
    let s1 = input();
    let s2 = input();
    let bulls = zip(s1.chars(), s2.chars()).filter(|&(c1, c2)| c1 == c2).count();
    let cows = ('0'..='9')
        .map(|d| {
            min(s1.chars().filter(|c| *c == d).count(), s2.chars().filter(|c| *c == d).count())
        })
        .sum::<usize>()
        - bulls;
    println!("{bulls} {cows}");
}
