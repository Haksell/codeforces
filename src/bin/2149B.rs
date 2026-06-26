use codeforces::{read, read_vec};

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(usize);
        let mut a = read_vec::<i64>();
        a.sort_unstable();
        let res = (0..n).step_by(2).map(|i| a[i + 1] - a[i]).max().unwrap();
        println!("{res}");
    }
}
