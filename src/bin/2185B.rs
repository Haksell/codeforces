use codeforces::{read, read_vec};

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(usize);
        let a = read_vec();
        println!("{}", n * a.iter().max().unwrap());
    }
}
