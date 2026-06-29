use codeforces::{read_vec, skip_line, FenwickTree};

fn main() {
    skip_line();
    let a = {
        let mut a = read_vec::<usize>();
        let mut indices: Vec<usize> = (0..a.len()).collect();
        indices.sort_unstable_by_key(|&i| a[i]);
        for (compressed, &i) in indices.iter().enumerate() {
            a[i] = compressed;
        }
        a
    };
    let mut fenwick_tree = FenwickTree::new(a.len());
    let mut inv = 0;
    for (i, &ai) in a.iter().enumerate() {
        inv += i as i64 - fenwick_tree.prefix_sum(ai + 1);
        fenwick_tree.update(ai, 1);
    }
    println!("{inv}");
}
