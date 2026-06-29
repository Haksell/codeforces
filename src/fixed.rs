use std::{
    array,
    fmt::write,
    ops::{AddAssign, MulAssign, Neg, Not, Sub},
};

// TODO: remove Copy
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
#[expect(non_camel_case_types)]
pub struct i1024 {
    repr: [u64; 16],
}

impl i1024 {
    const fn zero() -> Self {
        Self { repr: [0; 16] }
    }

    const fn one() -> Self {
        Self { repr: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] }
    }

    const fn is_negative(&self) -> bool {
        self.repr[15] >> 63 == 1
    }

    pub fn pow(b: i64, mut e: u32) -> Self {
        if e == 0 {
            return Self::one();
        }
        if b <= 1 {
            return Self::from(b);
        }

        let mut res = Self::one();
        let mut cur = Self::from(b);
        while e != 0 {
            if e & 1 == 1 {
                res *= cur;
            }
            cur *= cur;
            e >>= 1;
        }

        res
    }
}

impl Not for i1024 {
    type Output = Self;

    fn not(self) -> Self::Output {
        Self { repr: array::from_fn(|i| !self.repr[i]) }
    }
}

impl Neg for i1024 {
    type Output = Self;

    fn neg(self) -> Self::Output {
        todo!()
    }
}

impl Sub for i1024 {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self::Output {
        todo!()
    }
}

impl AddAssign for i1024 {
    fn add_assign(&mut self, rhs: Self) {
        todo!()
    }
}

impl MulAssign for i1024 {
    fn mul_assign(&mut self, rhs: Self) {
        todo!()
    }
}

impl AddAssign<u64> for i1024 {
    fn add_assign(&mut self, rhs: u64) {
        todo!()
    }
}

impl MulAssign<u64> for i1024 {
    fn mul_assign(&mut self, rhs: u64) {
        todo!()
    }
}

impl From<i64> for i1024 {
    fn from(value: i64) -> Self {
        let mut repr = [0; 16];
        repr[0] = value as u64 & 0x7fff_ffff_ffff_ffff;
        repr[15] = value as u64 & 0x8000_0000_0000_0000;
        Self { repr }
    }
}

// a bit sus but nicer to use
#[expect(clippy::fallible_impl_from)]
impl From<&str> for i1024 {
    fn from(s: &str) -> Self {
        const CHUNK_LEN: usize = 19; // largest number of repr that fit in a u64
        const CHUNK_POW: u64 = 10u64.pow(CHUNK_LEN as u32);

        // TODO: handle minus sign

        assert!(s.chars().all(|c| c.is_ascii_digit()), "Invalid character in string");

        let mut result = Self::from(0);
        for i in (0..s.len()).step_by(CHUNK_LEN) {
            let chunk_len = (s.len() - i).min(CHUNK_LEN);
            let chunk = s[i..(i + chunk_len)].parse::<u64>().unwrap();
            let chunk_pow =
                if chunk_len == CHUNK_LEN { CHUNK_POW } else { 10u64.pow(chunk_len as u32) };
            result *= chunk_pow;
            result += chunk;
        }

        result
    }
}

impl std::fmt::Display for i1024 {
    // TODO: fix EXTREME inefficiency
    #[expect(clippy::unwrap_in_result)]
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let mut digits: Vec<u64> = Vec::new();
        for i in 0..1023 {
            let word_idx = i >> 6;
            let bit_idx = i & 63;
            let bit = (self.repr[word_idx] >> bit_idx) & 1;
            for d in &mut digits {
                *d *= 2;
            }
            if digits.is_empty() {
                digits.push(bit);
            } else {
                let mut carry = 0;
                for d in &mut digits {
                    *d += carry;
                    if *d >= 10 {
                        *d -= 10;
                        carry = 1;
                    } else {
                        carry = 0;
                    }
                }
                if carry == 1 {
                    digits.push(carry);
                }
            }
        }

        let sign = if self.is_negative() { "-" } else { "" };
        let digits_str = digits
            .into_iter()
            .rev()
            .map(|d| char::from_digit(d as u32, 10).unwrap())
            .collect::<String>();
        write!(f, "{sign}{digits_str}")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_not() {
        assert_eq!(!i1024::from(0), i1024::from(-1));
        assert_eq!(!i1024::from(-1), i1024::from(0));

        assert_eq!(!i1024::from(42), i1024::from(-43));
        assert_eq!(!i1024::from(-43), i1024::from(42));

        assert_eq!(
            !i1024::from("100000000000000000000000000000000000000000000000000"),
            !i1024::from("-100000000000000000000000000000000000000000000000001")
        );
        assert_eq!(
            !i1024::from("-100000000000000000000000000000000000000000000000001"),
            !i1024::from("100000000000000000000000000000000000000000000000000"),
        );
    }
}
