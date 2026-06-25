use codeforces::{counter, read, skip_line, yes_no};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let (s, t) = read!(String, String);
        yes_no(counter(&s) == counter(&t));
    }
}
