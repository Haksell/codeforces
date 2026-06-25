FILE ?= error

ifeq (bundle, $(findstring bundle, $(MAKECMDGOALS)))
ifeq ($(FILE), error)
$(error FILE must be set)
endif
endif

clean:
	@rm -rf src/bin/tmp*.rs

install:
	@cargo install rust_bundler_cp
	@cargo install cargo-minify
	@cargo install rustminify-cli

bundle: clean install
	@echo 'extern crate codeforces;' > src/bin/tmp_extern.rs
	@cat $(FILE) >> src/bin/tmp_extern.rs
	@rust_bundler_cp --input . --binary tmp_extern --remove_unused_mod >src/bin/tmp.rs
	@rm src/bin/tmp_extern.rs
	@sed -i -E 's/^pub //g' src/bin/tmp.rs
	@sed -i -E 's/fn/\nfn/g' src/bin/tmp.rs
	@sed -i -E 's/^macro_rules ! read.*//g' src/bin/tmp.rs
	@mv src/bin/tmp.rs /tmp/tmp.rs
	@cp src/read_macro.rs src/bin/tmp.rs
	@cat /tmp/tmp.rs >> src/bin/tmp.rs
	@sed -i -E 's/^#\[macro_export\]$$//g' src/bin/tmp.rs
	@cargo fix --bin tmp --allow-dirty
	@cargo clippy --bin tmp --fix --allow-dirty
	@cargo minify --apply --allow-dirty
	@cargo fmt
	@python3 -c '__import__("pyperclip").copy(open("src/bin/tmp.rs").read())'
	@echo 'Bundled file `src/bin/tmp.rs` copied to clipboard'
