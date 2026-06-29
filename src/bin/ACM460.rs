use codeforces::{input, read};

fn main() {
    for _ in 0..read!(u64) {
        let s = input();
        if ["ch", "x", "s", "o"].iter().any(|end| s.ends_with(end)) {
            println!("{s}es");
        } else if ["f", "fe"].iter().any(|end| s.ends_with(end)) {
            let stop = s.rfind('f').unwrap();
            println!("{}ves", &s[..stop]);
        } else if s.ends_with('y') {
            let stop = s.len() - 1;
            println!("{}ies", &s[..stop]);
        } else {
            println!("{s}s");
        }
    }
}
