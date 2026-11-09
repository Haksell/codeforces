use codeforces::read;

fn main() {
    let (k, n, w) = read!(u64, u64, u64);
    let cost = w * (w + 1) / 2 * k;
    println!("{}", cost.saturating_sub(n));
}
