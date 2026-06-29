use codeforces::read;

fn main() {
    let (p, m, c) = read!(u16, u16, u16);
    let (k, r, v) = read!(u16, u16, u16);
    let res = *[p / k, m / r, c / v].iter().min().unwrap();
    println!("{res}");
}
