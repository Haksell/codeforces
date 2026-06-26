use codeforces::{print_iter, read, read_vec, skip_line};

fn main() {
    for _ in 0..read!(u64) {
        skip_line();
        let mut a = read_vec::<u64>();
        let all_same = a.iter().all(|x| x & 1 == a[0] & 1);
        if !all_same {
            a.sort_unstable();
        }
        print_iter(a);
    }
}
