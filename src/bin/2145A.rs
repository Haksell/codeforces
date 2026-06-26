use codeforces::read;

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(i64);
        println!("{}", (-n).rem_euclid(3));
    }
}
