use codeforces::read;

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(u64);
        let res = if n % 2 == 1 { 0 } else { n / 4 + 1 };
        println!("{res}");
    }
}
