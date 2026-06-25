mod read_macro;

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
    T: core::fmt::Debug + core::str::FromStr,
    T::Err: core::fmt::Debug,
{
    input().split_whitespace().map(|x| x.parse::<T>().unwrap()).collect()
}

pub fn yes_no(b: bool) {
    println!("{}", if b { "YES" } else { "NO" });
}
