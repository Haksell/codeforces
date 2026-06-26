use codeforces::{read, read_vec, yes_no};

fn main() {
    for _ in 0..read!(u64) {
        let ((), s, x) = read!(_, i64, i64);
        let a = read_vec();
        let sum = a.iter().sum::<i64>();
        let diff = s - sum;
        yes_no(diff >= 0 && diff % x == 0);
    }
}
