mod graph;
mod read_macro;

use std::collections::HashMap;
use std::io::Write as _;

pub fn input() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).expect("Failed to read line");
    s.truncate(s.trim_end().len());
    s
}

pub fn skip_line() {
    std::io::stdin().read_line(&mut String::new()).expect("Failed to skip a line");
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
