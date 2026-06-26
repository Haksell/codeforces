use codeforces::{gcd, read, read_vec, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let a = read_vec::<u64>();
        let g = a.iter().fold(0, |x, &y| gcd(x, y));
        let res = (2..=g + 1).find(|i| gcd(*i, g) == 1).unwrap();
        println!("{res}");
    }
}
