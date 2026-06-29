use codeforces::{gcd, read};

fn main() {
    let n = read!(u64);
    let res = (1..=n).filter(|i| gcd(*i, n) == 1).count();
    println!("{res}");
}
