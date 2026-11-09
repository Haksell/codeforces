use codeforces::{read, yes_no};

fn main() {
    let n = read!(u8);
    yes_no(n & 1 == 0 && n >= 4);
}
