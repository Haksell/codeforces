#![expect(clippy::tests_outside_test_module)]

use assert_cmd::Command;
use std::sync::LazyLock;

#[test]
fn codeforces_samples() -> Result<(), Box<dyn std::error::Error>> {
    for &(problem, stdin, stdout) in TESTS.iter() {
        Command::cargo_bin(problem)?.write_stdin(stdin).assert().success().stdout(stdout);
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
        (
            "2148A",
            "\
4
1 4
2 5
3 6
4 7
",
            "\
0
2
0
4
",
        ),
    ]
});
