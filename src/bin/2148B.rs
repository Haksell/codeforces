use codeforces::{read, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        let (n, m, (), ()) = read!(u64, u64, _, _);
        skip_line();
        skip_line();
        println!("{}", n + m);
    }
}
