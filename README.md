# sqlfluff 1970

Reproduces sqlfluff issue [#1970](https://github.com/sqlfluff/sqlfluff/issues/1970)

## Usage

1. Create and activate a virtualenv
1. Install: `pip install -e ".[dev]"`
1. Start postgres in the background: `docker compose up -d`
1. Run sqlfluff:

   ```
    $ sqlfluff lint
    === [dbt templater] Sorting Nodes...
    === [dbt templater] Compiling dbt project...
    === [dbt templater] Project Compiled.
    file create_table.sql:   0%|                                                                                                   | 0/3 [00:00<?, ?it/s]Traceback (most recent call last):
    File "/Users/tekumara/code/sqlfluff1970/.venv/bin/sqlfluff", line 8, in <module>
        sys.exit(cli())
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/click/core.py", line 1128, in __call__
        return self.main(*args, **kwargs)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/click/core.py", line 1053, in main
        rv = self.invoke(ctx)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/click/core.py", line 1659, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/click/core.py", line 1395, in invoke
        return ctx.invoke(self.callback, **ctx.params)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/click/core.py", line 754, in invoke
        return __callback(*args, **kwargs)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/cli/commands.py", line 497, in lint
        result = lnt.lint_paths(
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/linter.py", line 974, in lint_paths
        self.lint_path(
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/linter.py", line 926, in lint_path
        for i, linted_file in enumerate(runner.run(fnames, fix), start=1):
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/runner.py", line 101, in run
        for fname, partial in self.iter_partials(fnames, fix=fix):
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/runner.py", line 54, in iter_partials
        for fname, rendered in self.iter_rendered(fnames):
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/runner.py", line 43, in iter_rendered
        yield fname, self.linter.render_file(fname, self.config)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/linter.py", line 652, in render_file
        return self.render_string(raw_file, fname, config, encoding)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff/core/linter/linter.py", line 629, in render_string
        templated_file, templater_violations = self.templater.process(
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff_templater_dbt/templater.py", line 331, in process
        processed_result = self._unsafe_process(fname_absolute_path, in_str, config)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff_templater_dbt/templater.py", line 448, in _unsafe_process
        node = self._find_node(fname, config)
    File "/Users/tekumara/code/sqlfluff1970/.venv/lib/python3.9/site-packages/sqlfluff_templater_dbt/templater.py", line 403, in _find_node
        raise RuntimeError(
    RuntimeError: File /Users/tekumara/code/sqlfluff1970/macros/create_table.sql was not found in dbt project
   ```
