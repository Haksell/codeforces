use codeforces::read;

fn main() {
    let (mut a, mut b) = (1u64, 1u64);
    let mut s = 0;
    for _ in 0..read!(u64) {
        s += a;
        (a, b) = (b, a + b);
    }
    println!("{s}");
}
