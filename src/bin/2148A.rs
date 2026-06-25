use codeforces::read;

fn main() {
    for _ in 0..read!(u64) {
        let (x, n) = read!(u64, u64);
        println!("{}", x * (n & 1));
    }
}
