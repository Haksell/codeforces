use codeforces::{read, read_vec, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let a = read_vec::<u8>();
        println!("{}", a.iter().max().unwrap());
    }
}
