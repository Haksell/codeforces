use codeforces::{print_iter, read};

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(u64);
        print_iter(1..=n);
    }
}
