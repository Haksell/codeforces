pub struct FenwickTree {
    len: usize,
    tree: Vec<i64>,
}

impl FenwickTree {
    pub fn new(len: usize) -> Self {
        Self { len, tree: vec![0; len + 1] }
    }

    pub fn update(&mut self, mut i: usize, delta: i64) {
        i += 1;
        while i <= self.len {
            self.tree[i] += delta;
            i += (i as isize & -(i as isize)) as usize;
        }
    }

    pub fn prefix_sum(&self, mut i: usize) -> i64 {
        let mut res = 0;
        while i > 0 {
            res += self.tree[i];
            i -= (i as isize & -(i as isize)) as usize;
        }
        res
    }
}
