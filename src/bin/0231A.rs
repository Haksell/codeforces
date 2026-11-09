use codeforces::read;

fn main() {
    let res = (0..read!(u64))
        .filter(|_| {
            let (a, b, c) = read!(u8, u8, u8);
            a + b + c >= 2
        })
        .count();
    println!("{res}");
}
