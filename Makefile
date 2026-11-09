validate:
	@$(MAKE) -s format
	@$(MAKE) -s test
	@RUSTFLAGS="--deny warnings" $(MAKE) -s check
	@RUSTFLAGS="--deny warnings" $(MAKE) -s lint
	@$(MAKE) -s solved

format:
	@cargo fmt --all

test:
	@cargo test --lib
	@cargo test --test '*'

check:
	@cargo check --workspace --all-targets

lint:
	@cargo clippy --workspace --all-targets

clean:
	@rm -rf src/bin/tmp*.rs

install:
	@cargo install cargo-udeps --locked
	@cargo install cargo-equip --locked

PYTHON_PROBLEMS := $(shell ls python | grep -E '[0-9]{4}[A-Z][0-9]?\.py' | wc -l)
RUST_PROBLEMS := $(shell ls src/bin | grep -E '[0-9]{4}[A-Z][0-9]?\.rs' | wc -l)
RUST_ACM := $(shell ls src/bin | grep -E 'ACM[0-9]{3}\.rs' | wc -l)

solved:
	@echo "Problems in Python: $(PYTHON_PROBLEMS)"
	@echo "Problems in Rust: $(RUST_PROBLEMS)"
	@echo "ACM problems in Rust: $(RUST_ACM)"
	@sed -i "s/.*problems in Python/- $(PYTHON_PROBLEMS)\/1600 problems in Python/" README.md
	@sed -i "s/.*[0-9] problems in Rust/- $(RUST_PROBLEMS)\/100 problems in Rust/" README.md
	@sed -i "s/.*ACM problems in Rust/- $(RUST_ACM)\/100 ACM problems in Rust/" README.md

setup_git_hooks:
	@rm -rf .git/hooks
	@ln -s ../git_hooks .git/hooks