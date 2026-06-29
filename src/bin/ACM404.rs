use codeforces::{input, read, skip_line};

fn main() {
    let (n, m) = read!(u8, u8);
    let skip = (n - 1) % m;
    for _ in 0..skip {
        skip_line();
    }
    println!("{}", input());
}
