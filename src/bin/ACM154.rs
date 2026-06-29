use codeforces::read;

const fn zeros(mut n: u64) -> u64 {
    let mut res = 0;
    while n > 0 {
        res += n;
        n /= 5;
    }
    res
}

const fn solve(n: u64) -> Option<u64> {
    if n == 0 {
        return Some(1);
    }

    let mut lo = 0;
    let mut hi = n;
    while lo <= hi {
        let mi = u64::midpoint(lo, hi);
        let z = zeros(mi);
        if z < n {
            lo = mi + 1;
        } else if z > n {
            hi = mi - 1;
        } else {
            return Some(mi * 5);
        }
    }

    None
}

fn main() {
    let n = read!(u64);
    match solve(n) {
        Some(res) => println!("{res}"),
        None => println!("No solution"),
    }
}
