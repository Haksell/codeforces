#[macro_export]
macro_rules! read {
    ($t:ty) => { $crate::input().parse::<$t>().unwrap() };
    ($($t:tt),+ $(,)?) => {{
        let line = $crate::input();
        let mut iter = line.split_whitespace();
        ($(read!(@parse iter, $t),)+)
    }};
    (@parse $iter:ident, _) => {{ $iter.next().expect("Not enough input values"); }};
    (@parse $iter:ident, $t:ty) => {{
        $iter.next()
            .expect("Not enough input values")
            .parse::<$t>()
            .expect("Failed to parse input")
    }};
}
