use codeforces::read;

fn main() {
    for _ in 0..read!(u64) {
        let (k, x) = read!(u64, u64);
        println!("{}", k * x + 1);
    }
}
