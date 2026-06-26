use codeforces::{print_iter, read, read_vec};

fn main() {
    for _ in 0..read!(u64) {
        let n = read!(usize);
        let mut p = read_vec::<usize>();
        for l in 0..n {
            if p[l] != n - l {
                let r = p.iter().position(|x| *x == n - l).unwrap();
                p[l..=r].reverse();
                break;
            }
        }
        print_iter(p);
    }
}
