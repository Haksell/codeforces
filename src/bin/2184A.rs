use codeforces::read;

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(u64);
        println!("{}", if n <= 3 { n } else { n % 2 });
    }
}
