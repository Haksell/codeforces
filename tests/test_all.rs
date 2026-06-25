#![expect(clippy::tests_outside_test_module)]

use assert_cmd::Command;
use std::sync::LazyLock;

#[test]
fn codeforces_samples() -> Result<(), Box<dyn std::error::Error>> {
    for &(problem, input, expected) in TESTS.iter() {
        Command::cargo_bin(problem)?.write_stdin(input).assert().success().stdout(expected);
    }

    Ok(())
}

static TESTS: LazyLock<Vec<(&'static str, &'static str, &'static str)>> = LazyLock::new(|| {
    vec![
        (
            "2167A",
            "\
7
1 2 3 4
1 1 1 1
2 2 2 2
1 2 1 2
1 1 5 5
5 5 5 5
4 10 5 9
",
            "\
NO
YES
YES
NO
NO
YES
NO
",
        ),
        (
            "2167B",
            "\
5
7
humitsa mitsuha
4
orhi hori
6
aakima makima
6
nezuqo nezuko
6
misaka mikasa
",
            "\
YES
YES
NO
NO
YES
",
        ),
    ]
});
