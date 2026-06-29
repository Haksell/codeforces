use codeforces::read;
use std::array;

#[expect(clippy::collapsible_else_if)]
const fn median_of_3(a: i32, b: i32, c: i32) -> i32 {
    if a < b {
        if b < c {
            b
        } else if a < c {
            c
        } else {
            a
        }
    } else {
        if a < c {
            a
        } else if b < c {
            c
        } else {
            b
        }
    }
}

fn main() {
    let [x, y, z] = array::from_fn(|_| {
        let (a, b, c) = read!(i32, i32, i32);
        median_of_3(a, b, c)
    });
    println!("{}", median_of_3(x, y, z));
}
