FILE ?= error

ifeq (bundle, $(findstring bundle, $(MAKECMDGOALS)))
ifeq ($(FILE), error)
$(error FILE must be set)
endif
endif

RUSTFMT_CONFIG := use_small_heuristics=Max,group_imports=One,imports_granularity=One
RUSTFMT_FLAGS := --edition 2024 --style-edition 2024 --config $(RUSTFMT_CONFIG)

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
	@cargo install rust_bundler_cp
	@cargo install cargo-minify
	@cargo install rustminify-cli

bundle: clean
	@echo 'extern crate codeforces;' > src/bin/tmp_extern.rs
	@cat $(FILE) >> src/bin/tmp_extern.rs
	@rust_bundler_cp --input . --binary tmp_extern --remove_unused_mod >src/bin/tmp.rs
	@rm src/bin/tmp_extern.rs
	@sed -i -E 's/^pub //g' src/bin/tmp.rs
	@sed -i -E 's/^#/\n#/g' src/bin/tmp.rs
	@sed -i -E 's/^fn/\nfn/g' src/bin/tmp.rs
	@sed -i -E 's/^macro_rules ! read.*//g' src/bin/tmp.rs
	@mv src/bin/tmp.rs /tmp/tmp.rs
	@cp src/read_macro.rs src/bin/tmp.rs
	@echo >> src/bin/tmp.rs
	@cat /tmp/tmp.rs >> src/bin/tmp.rs
	@sed -i -E 's/^#\[macro_export\]$$//g' src/bin/tmp.rs
	@python3 scripts/use_on_top.py src/bin/tmp.rs
	@rustfmt src/bin/tmp.rs $(RUSTFMT_FLAGS)
	@cargo fix --bin tmp --allow-dirty
	@cargo clippy --bin tmp --fix --allow-dirty
	@cargo minify --apply --allow-dirty --allow-staged
	@cargo fix --bin tmp --allow-dirty
	@cargo clippy --bin tmp --fix --allow-dirty
	@rustfmt src/bin/tmp.rs $(RUSTFMT_FLAGS)

bundle_copy: bundle
	@python3 -c '__import__("pyperclip").copy(open("src/bin/tmp.rs").read())'
	@echo 'Bundled file `src/bin/tmp.rs` copied to clipboard'

PYTHON_PROBLEMS := $(shell ls python | grep -E '[0-9]{4}[A-Z][0-9]?\.py' | wc -l)
RUST_PROBLEMS := $(shell ls src/bin | grep -E '[0-9]{4}[A-Z][0-9]?\.rs' | wc -l)
RUST_ACM := $(shell ls src/bin | grep -E 'ACM[0-9]{3}?\.rs' | wc -l)

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