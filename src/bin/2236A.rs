use codeforces::{read, read_vec, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let a = read_vec::<u64>();
        println!("{}", 1 + a.iter().max().unwrap() - a.iter().min().unwrap());
    }
}
