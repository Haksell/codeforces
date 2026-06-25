#[macro_export]
macro_rules! read {
    ($t:ty) => { $crate::input().parse::<$t>().unwrap() };
    ($($t:ty),+) => {
        {
            let line = $crate::input();
            let mut iter = line.split_whitespace();
            (
                $(
                    iter.next()
                        .expect("Not enough input values")
                        .parse::<$t>()
                        .expect("Failed to parse input"),
                )+
            )
        }
    };
}
