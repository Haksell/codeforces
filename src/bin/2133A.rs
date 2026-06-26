use codeforces::{read, read_vec, skip_line, yes_no};
use std::collections::HashSet;

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let a = read_vec::<u64>();
        let h: HashSet<u64> = a.iter().copied().collect();
        yes_no(a.len() != h.len());
    }
}
