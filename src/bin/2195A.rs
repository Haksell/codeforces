use codeforces::{read, read_vec, skip_line, yes_no};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        yes_no(read_vec().contains(&67));
    }
}
