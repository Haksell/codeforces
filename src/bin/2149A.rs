use codeforces::{read, read_vec, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let a = read_vec::<i8>();
        let zeros = a.iter().filter(|n| **n == 0).count();
        let negatives = a.iter().filter(|n| **n < 0).count();
        println!("{}", zeros + if negatives % 2 == 0 { 0 } else { 2 });
    }
}
