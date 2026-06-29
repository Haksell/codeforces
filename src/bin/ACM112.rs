use codeforces::{i1024, read};

// 100**100 requires 665 bits

fn main() {
    let (a, b) = read!(i64, i64);
    println!("{}", i1024::pow(a, b as u32) - i1024::pow(b, a as u32));
}
