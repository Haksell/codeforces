mod read_macro;

use std::{
    cmp::min,
    collections::HashMap,
    io::{Write as _, stdin},
    mem::swap,
};

pub fn input() -> String {
    let mut s = String::new();
    stdin().read_line(&mut s).expect("Failed to read line");
    s.truncate(s.trim_end().len());
    s
}

pub fn skip_line() {
    stdin().read_line(&mut String::new()).expect("Failed to skip a line");
}

pub fn read_vec<T>() -> Vec<T>
where
    T: std::fmt::Debug + std::str::FromStr,
    T::Err: std::fmt::Debug,
{
    input().split_whitespace().map(|x| x.parse::<T>().unwrap()).collect()
}

pub fn yes_no(b: bool) {
    println!("{}", if b { "YES" } else { "NO" });
}

pub fn print_iter<S: std::fmt::Display, I: IntoIterator<Item = S>>(iter: I) {
    let mut stdout = std::io::stdout().lock();
    let mut first = true;

    for item in iter {
        if !first {
            write!(stdout, " ").unwrap();
        }
        first = false;
        write!(stdout, "{item}").unwrap();
    }

    writeln!(stdout).unwrap();
}

pub fn counter(s: &str) -> HashMap<char, u32> {
    let mut counter = HashMap::new();
    for c in s.chars() {
        *counter.entry(c).or_insert(0) += 1;
    }
    counter
}

// https://en.wikipedia.org/wiki/Binary_GCD_algorithm
pub fn gcd(mut a: u64, mut b: u64) -> u64 {
    if a == 0 {
        return b;
    } else if b == 0 {
        return a;
    }

    let tz_a = a.trailing_zeros();
    let tz_b = b.trailing_zeros();
    let tz_max = min(tz_a, tz_b);
    a >>= tz_a;
    b >>= tz_b;

    loop {
        if a == b {
            return a << tz_max;
        }
        if a > b {
            swap(&mut a, &mut b);
        }
        b -= a;
        b >>= b.trailing_zeros();
    }
}

pub fn lcm(a: u64, b: u64) -> u64 {
    a * b / gcd(a, b)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_counter() {
        assert_eq!(
            counter("babaorum"),
            HashMap::from([('a', 2), ('b', 2), ('m', 1), ('o', 1), ('r', 1), ('u', 1)])
        );
    }

    #[test]
    #[expect(clippy::cognitive_complexity)]
    fn test_gcd() {
        assert_eq!(gcd(0, 0), 0);
        assert_eq!(gcd(0, 1), 1);
        assert_eq!(gcd(0, 2), 2);
        assert_eq!(gcd(0, 3), 3);
        assert_eq!(gcd(0, 4), 4);
        assert_eq!(gcd(0, 5), 5);
        assert_eq!(gcd(0, 6), 6);

        assert_eq!(gcd(1, 0), 1);
        assert_eq!(gcd(1, 1), 1);
        assert_eq!(gcd(1, 2), 1);
        assert_eq!(gcd(1, 3), 1);
        assert_eq!(gcd(1, 4), 1);
        assert_eq!(gcd(1, 5), 1);
        assert_eq!(gcd(1, 6), 1);

        assert_eq!(gcd(2, 0), 2);
        assert_eq!(gcd(2, 1), 1);
        assert_eq!(gcd(2, 2), 2);
        assert_eq!(gcd(2, 3), 1);
        assert_eq!(gcd(2, 4), 2);
        assert_eq!(gcd(2, 5), 1);
        assert_eq!(gcd(2, 6), 2);

        assert_eq!(gcd(3, 0), 3);
        assert_eq!(gcd(3, 1), 1);
        assert_eq!(gcd(3, 2), 1);
        assert_eq!(gcd(3, 3), 3);
        assert_eq!(gcd(3, 4), 1);
        assert_eq!(gcd(3, 5), 1);
        assert_eq!(gcd(3, 6), 3);

        assert_eq!(gcd(4, 0), 4);
        assert_eq!(gcd(4, 1), 1);
        assert_eq!(gcd(4, 2), 2);
        assert_eq!(gcd(4, 3), 1);
        assert_eq!(gcd(4, 4), 4);
        assert_eq!(gcd(4, 5), 1);
        assert_eq!(gcd(4, 6), 2);

        assert_eq!(gcd(6, 0), 6);
        assert_eq!(gcd(6, 1), 1);
        assert_eq!(gcd(6, 2), 2);
        assert_eq!(gcd(6, 3), 3);
        assert_eq!(gcd(6, 4), 2);
        assert_eq!(gcd(6, 5), 1);
        assert_eq!(gcd(6, 6), 6);

        assert_eq!(gcd(945, 1008), 63);
        assert_eq!(gcd(945, 1071), 63);
    }

    #[test]
    fn test_lcm() {
        assert_eq!(lcm(42, 0), 0);
        assert_eq!(lcm(42, 1), 42);
        assert_eq!(lcm(42, 2), 42);
        assert_eq!(lcm(42, 3), 42);
        assert_eq!(lcm(42, 4), 84);
        assert_eq!(lcm(42, 5), 210);
        assert_eq!(lcm(42, 63), 126);
    }
}
