use codeforces::{read, yes_no};

fn main() {
    for _ in 0..read!(u64) {
        let (a, b, c, d) = read!(u32, u32, u32, u32);
        yes_no(a == b && a == c && a == d);
    }
}
