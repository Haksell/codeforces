use codeforces::{read, read_vec};

fn main() {
    for _ in 0..read!(u64) {
        let a = read_vec::<i32>();
        let res = 2 * a.iter().max().unwrap() - a.iter().sum::<i32>();
        println!("{res}");
    }
}
