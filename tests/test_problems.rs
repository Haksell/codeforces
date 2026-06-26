#![expect(clippy::tests_outside_test_module)]

use assert_cmd::Command;
use std::sync::LazyLock;

#[test]
fn test_problems() -> Result<(), Box<dyn std::error::Error>> {
    for &(problem, stdin, stdout) in TESTS.iter() {
        Command::cargo_bin(problem)?.write_stdin(stdin).assert().success().stdout(stdout);
    }
    Ok(())
}

// TODO: parse from directory
static TESTS: LazyLock<Vec<(&str, &str, &str)>> = LazyLock::new(|| {
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
        (
            "2193A",
            "\
6
3 3 5
1 1 1
3 8 2
1 2 3
4 7 2
1 1 1 1
3 15 1
2 4 10
2 100 5
4 6
5 12 1
1 2 2 3 2
",
            "\
YES
YES
NO
NO
YES
YES
",
        ),
    ]
});
