use codeforces::{print_iter, read};

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(u64);
        let mut res = Vec::new();
        for z in (1..=18).rev() {
            let mul = 10u64.pow(z) + 1;
            if n % mul == 0 {
                res.push(n / mul);
            }
        }
        if res.is_empty() {
            println!("0");
        } else {
            println!("{}", res.len());
            print_iter(res);
        }
    }
}
