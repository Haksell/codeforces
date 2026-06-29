use codeforces::read;

fn main() {
    let n = read!(usize) + 1;

    let mut sieve = vec![true; n];
    sieve[0] = false;
    sieve[1] = false;

    let mut res = Vec::new();
    for i in 2..n {
        if sieve[i] {
            if sieve[i - 2] {
                res.push(i - 2);
            }
            for j in (i * i..n).step_by(i) {
                sieve[j] = false;
            }
        }
    }

    println!("{}", res.len());
    for r in res {
        println!("2 {r}");
    }
}
