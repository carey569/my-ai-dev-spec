# Codebase Analysis Methodology

Step-by-step instructions for analyzing a project using built-in tools
(Glob, Grep, Read, Bash). Produces the same data as the former
`scripts/analyze_codebase.py` — plus qualitative fields the script could
not generate.

Execute each step in order. Collect named data fields for use in template
placeholder substitution (Phase 5-6 of the main skill).

> **SOURCE_PATH** refers to the project directory being analyzed. For
> refactor projects this is `LEGACY_DIR`; configs will be generated in
> `TARGET_DIR`.

---

## Excluded Directories

Skip these directories during all file operations:

```
node_modules, .git, __pycache__, venv, .venv, env, dist, build, target,
.next, .nuxt, .output, coverage, .pytest_cache, .mypy_cache, .tox,
vendor, Pods, .gradle, .idea, .vscode, .DS_Store, .cache,
.parcel-cache, .turbo, out, bin, obj, .svn, .hg
```

---

## Step 1: File Statistics

Gather quantitative measures of the codebase.

### Data fields

| Field | Description |
|-------|-------------|
| `total_files` | Count of all non-binary files (excluding dirs above) |
| `total_lines` | Aggregate line count of code files |
| `extension_distribution` | Top 20 extensions by occurrence |
| `key_directories` | Directories at depth 1-2 that contain files |
| `directory_tree` | Indented tree to depth 3 |

### How to collect

```bash
# File count (adjust excluded dirs with -not -path)
find SOURCE_PATH -type f \
  -not -path '*/node_modules/*' -not -path '*/.git/*' \
  -not -path '*/dist/*' -not -path '*/build/*' \
  -not -path '*/target/*' -not -path '*/.next/*' \
  -not -path '*/coverage/*' -not -path '*/vendor/*' \
  -not -path '*/__pycache__/*' -not -path '*/venv/*' \
  -not -path '*/.venv/*' \
  | wc -l

# Extension distribution
find SOURCE_PATH -type f [same exclusions] \
  | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20

# Line count of code files
find SOURCE_PATH -type f \( \
  -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.tsx' \
  -o -name '*.jsx' -o -name '*.go' -o -name '*.rs' -o -name '*.java' \
  -o -name '*.rb' -o -name '*.kt' -o -name '*.swift' -o -name '*.c' \
  -o -name '*.cpp' -o -name '*.cs' -o -name '*.php' -o -name '*.ex' \
  -o -name '*.vue' -o -name '*.svelte' \
\) [same exclusions] | xargs wc -l 2>/dev/null | tail -1

# Directory tree (depth 3)
find SOURCE_PATH -maxdepth 3 -type d [same exclusions] | sort
```

**Large repository (1000+ files)**: Use only the extension distribution
and top-level directory listing. Skip per-file line counting.

---

## Step 2: Tech Stack Detection

Detect languages, frameworks, package managers, build tools, and runtime.

### Check order (stop at first match per ecosystem)

Use **Glob** to find config files, then **Read** to parse their contents.

#### Node.js

1. Glob `SOURCE_PATH/package.json`
2. Read it → extract `dependencies`, `devDependencies`, `scripts`
3. **Frameworks** — check dependency keys against:

   | Dependency key | Framework name |
   |---------------|---------------|
   | `next` | Next.js |
   | `nuxt` | Nuxt.js |
   | `react` | React |
   | `vue` | Vue.js |
   | `@angular/core` | Angular |
   | `svelte` | Svelte |
   | `express` | Express |
   | `fastify` | Fastify |
   | `koa` | Koa |
   | `@nestjs/core` or `nest` | NestJS |
   | `electron` | Electron |
   | `gatsby` | Gatsby |
   | `remix` | Remix |
   | `astro` | Astro |
   | `vite` | Vite |

4. **Package manager** — check lockfile existence (priority order):
   - `pnpm-lock.yaml` → pnpm
   - `yarn.lock` → yarn
   - `bun.lockb` or `bun.lock` → bun
   - `package-lock.json` → npm

5. **Build tools** — check `scripts` values and dependency keys for:
   `webpack`, `vite`, `rollup`, `esbuild`, `parcel`, `turbo`, `tsc`, `swc`

6. **Commands** — derive from `scripts` field:
   - `INSTALL_CMD`: `[pkg-mgr] install`
   - `DEV_CMD`: `[pkg-mgr] run dev` (or actual script name)
   - `BUILD_CMD`: `[pkg-mgr] run build`
   - `TEST_CMD`: `[pkg-mgr] test` or `[pkg-mgr] run test`
   - `LINT_CMD`: `[pkg-mgr] run lint`

#### Python

1. Glob `SOURCE_PATH/pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile`
2. Read content → check for framework patterns:

   | Pattern (case-insensitive) | Framework name |
   |---------------------------|---------------|
   | `django` | Django |
   | `flask` | Flask |
   | `fastapi` | FastAPI |
   | `starlette` | Starlette |
   | `tornado` | Tornado |
   | `celery` | Celery |
   | `sqlalchemy` | SQLAlchemy |

3. **Package manager** (priority order):
   - `pyproject.toml` contains `poetry` → poetry
   - `Pipfile` exists → pipenv
   - `uv.lock` exists → uv
   - Default → pip

4. **Commands**:
   - poetry: `poetry install` / `poetry run pytest` / `poetry run python manage.py runserver`
   - pip: `pip install -r requirements.txt` / `pytest` / `python manage.py runserver`
   - uv: `uv sync` / `uv run pytest`

#### Go

1. Glob `SOURCE_PATH/go.mod`
2. Read content → check for framework patterns:

   | Pattern | Framework name |
   |---------|---------------|
   | `gin-gonic/gin` | Gin |
   | `labstack/echo` | Echo |
   | `gofiber/fiber` | Fiber |

3. Package manager: `go modules`
4. Commands: `go build ./...` / `go test ./...` / `golangci-lint run`

#### Rust

1. Glob `SOURCE_PATH/Cargo.toml`
2. Read `[dependencies]` section → check for:

   | Pattern | Framework name |
   |---------|---------------|
   | `actix-web` | Actix |
   | `rocket` | Rocket |
   | `axum` | Axum |
   | `tokio` | Tokio |

3. Package manager: `cargo`
4. Commands: `cargo build` / `cargo test` / `cargo clippy`

#### Java / Kotlin (JVM)

1. Glob `SOURCE_PATH/pom.xml` or `build.gradle` / `build.gradle.kts`
2. Read content → check for `spring-boot` or `spring`:
   - Found `spring-boot` → Spring Boot
   - Found `spring` → Spring
3. Package manager: `maven` or `gradle`
4. Build tool: `maven` or `gradle`
5. Commands:
   - Maven: `mvn clean install` / `mvn test`
   - Gradle: `./gradlew build` / `./gradlew test`

#### Ruby

1. Glob `SOURCE_PATH/Gemfile`
2. Read content → `rails` → Rails; `sinatra` → Sinatra
3. Package manager: `bundler`
4. Commands: `bundle install` / `bundle exec rails server` / `bundle exec rspec`

#### Swift

1. Glob `SOURCE_PATH/Package.swift`
2. Package manager: `swift-pm`
3. Commands: `swift build` / `swift test`

#### Elixir

1. Glob `SOURCE_PATH/mix.exs`
2. Read content → `phoenix` → Phoenix
3. Package manager: `mix`
4. Commands: `mix deps.get` / `mix phx.server` / `mix test`

### Language distribution

Determine `PRIMARY_LANGUAGE` from the extension distribution (Step 1),
using only code extensions:

| Extension | Language |
|-----------|----------|
| `.py` | Python |
| `.js`, `.mjs`, `.cjs`, `.jsx` | JavaScript |
| `.ts`, `.tsx`, `.mts` | TypeScript |
| `.java` | Java |
| `.kt`, `.kts` | Kotlin |
| `.go` | Go |
| `.rs` | Rust |
| `.rb`, `.erb` | Ruby |
| `.php` | PHP |
| `.cs` | C# |
| `.cpp`, `.cc`, `.cxx`, `.hpp` | C++ |
| `.c`, `.h` | C |
| `.swift` | Swift |
| `.scala` | Scala |
| `.ex`, `.exs` | Elixir |
| `.dart` | Dart |
| `.vue` | Vue |
| `.svelte` | Svelte |
| `.sh`, `.bash`, `.zsh` | Shell |

Exclude markup/config formats (JSON, YAML, TOML, XML, Markdown, HTML, CSS)
from primary language calculation. The language with the most code lines
is `PRIMARY_LANGUAGE`.

---

## Step 3: Quality Infrastructure

### Testing

| What to check | How |
|---------------|-----|
| Test framework | Glob for config files at project root: |

| Config file pattern | Framework |
|---------------------|-----------|
| `jest.config*` | jest |
| `vitest.config*` | vitest |
| `pytest.ini`, `conftest.py` | pytest |
| `.rspec` | rspec |
| `karma.conf.js` | karma |
| `cypress.config*` | cypress |
| `playwright.config*` | playwright |

Also check `pyproject.toml` for `[tool.pytest` section.

| What | How |
|------|-----|
| Test file count | Glob for `**/test_*`, `**/*_test.*`, `**/*.test.*`, `**/*.spec.*` in non-excluded directories |
| Coverage config | Glob for `.nycrc`, `.coveragerc`, `.c8rc`, `coverage/`; check `package.json` scripts for "coverage" |

### CI/CD

Check existence (priority order — first match wins):

| Path | Platform |
|------|----------|
| `.github/workflows/` | github-actions |
| `.gitlab-ci.yml` | gitlab-ci |
| `Jenkinsfile` | jenkins |
| `.circleci/` | circleci |
| `.travis.yml` | travis |
| `azure-pipelines.yml` | azure-devops |
| `bitbucket-pipelines.yml` | bitbucket |

Count `.yml`/`.yaml` files inside the CI directory for `pipeline_count`.

### Linting

| Tool | Config files to check |
|------|----------------------|
| eslint | `.eslintrc`, `.eslintrc.js`, `.eslintrc.json`, `.eslintrc.yml`, `eslint.config.js`, `eslint.config.mjs` |
| pylint | `.pylintrc`, `pylintrc` |
| flake8 | `.flake8` |
| ruff | `ruff.toml`, `.ruff.toml`, or `[tool.ruff` in `pyproject.toml` |
| rubocop | `.rubocop.yml` |
| golangci-lint | `.golangci.yml`, `.golangci.yaml` |
| stylelint | `.stylelintrc`, `.stylelintrc.json` |

### Formatting

| Tool | Config files to check |
|------|----------------------|
| prettier | `.prettierrc`, `.prettierrc.js`, `.prettierrc.json`, `prettier.config.js` |
| black | `[tool.black` in `pyproject.toml` |
| ruff-format | `[tool.ruff.format` in `pyproject.toml` |
| editorconfig | `.editorconfig` |
| clang-format | `.clang-format` |

### Type Checking

Check for: `tsconfig.json`, `mypy.ini`, `pyrightconfig.json`, or
`[tool.mypy` in `pyproject.toml`.

---

## Step 4: Architecture Recognition

### Pattern scoring

Using `key_directories` from Step 1, score each pattern by checking
whether directory names appear in the project:

| Pattern | Directory → Weight |
|---------|-------------------|
| **mvc** | controllers(2), models(2), views(2), routes(1) |
| **layered** | services(2), repositories(1), controllers(1), middleware(1), utils(1) |
| **ddd** | domain(3), application(2), infrastructure(2), ports(1), adapters(1) |
| **spa-frontend** | components(3), pages(2), hooks(2), stores(1), store(1), assets(1) |
| **api-server** | routes(2), handlers(2), middleware(2), models(1), services(1) |
| **serverless** | functions(3), lambda(3), handlers(2) |

- Highest-scoring pattern wins (minimum score = 3 to be reported)
- `confidence = min(best_score / max_possible_score, 1.0)`
- If no pattern scores >= 3, report `unknown`

### Monorepo detection

1. Check directories: `packages/`, `apps/`, `modules/`, `libs/`, `services/` —
   if any contains 2+ subdirectories → monorepo
2. Check config files: `lerna.json`, `nx.json`, `turbo.json`,
   `pnpm-workspace.yaml` — if any exists → monorepo

### Entry points

Check existence of standard entry files:

```
main.py, app.py, server.py, manage.py,
main.go, main.rs, main.java,
index.js, index.ts, index.tsx,
src/main.py, src/app.py, src/main.ts, src/index.ts,
src/main.go, src/main.rs, src/main.java,
src/index.js, src/index.tsx,
src/pages/index.tsx, src/pages/index.js,
cmd/main.go
```

### Qualitative analysis (advantage over script)

Read 2-3 key source files (entry points or high-traffic modules) to
understand:
- `MODULE_DESCRIPTIONS` — module responsibilities
- `DATA_FLOW_DESCRIPTION` — request/data flow
- `OBSERVED_PATTERNS` — error handling, logging, auth patterns
- `NAMING_CONVENTIONS` — file and variable naming style
- `ONE_LINE_DESCRIPTION` — from README first paragraph or package.json `description`

---

## Step 5: Dependencies

Read the primary dependency file (already read in Step 2) and extract:

| Field | How |
|-------|-----|
| `total_count` | Count all dependencies |
| `dev_dependency_count` | Count dev-only dependencies (Node.js: `devDependencies`) |
| `key_dependencies` | Top 15 most important dependencies (judge by relevance, not alphabetical order) |

### Per-ecosystem parsing

- **Node.js**: Read `package.json` → `dependencies` + `devDependencies`
- **Python**: Read `requirements.txt` → split on `==`, `>=`, `<=`, `[`; or parse `pyproject.toml`
- **Go**: Read `go.mod` → extract `require` block entries
- **Rust**: Read `Cargo.toml` → extract `[dependencies]` section keys

---

## Step 6: Git Metrics

Use **Bash** for all git commands. Skip this step entirely if not a git
repository (`git rev-parse --is-inside-work-tree` fails).

| Data field | Command |
|------------|---------|
| `is_git_repo` | `git -C SOURCE_PATH rev-parse --is-inside-work-tree` |
| `total_commits` | `git -C SOURCE_PATH rev-list --count HEAD` |
| `repo_age_days` | `git -C SOURCE_PATH log --reverse --format=%aI --max-count=1` → calculate days since |
| `active_contributors` | `git -C SOURCE_PATH shortlog -sn --no-merges \| wc -l` |
| `last_30d_commits` | `git -C SOURCE_PATH rev-list --count --since="30 days ago" HEAD` |
| `last_90d_commits` | `git -C SOURCE_PATH rev-list --count --since="90 days ago" HEAD` |
| `most_changed_files` | `git -C SOURCE_PATH log --format=format: --name-only --max-count=200 \| sort \| uniq -c \| sort -rn \| head -10` |
| `branch_count` | `git -C SOURCE_PATH branch -a \| wc -l` |
| `recent_commit_messages` | `git -C SOURCE_PATH log --oneline --max-count=30` |

---

## Step 7: Documentation Assessment

Use **Glob** to check existence:

| Document | Files to check |
|----------|---------------|
| README | `README.md` |
| CLAUDE.md | `CLAUDE.md` |
| API docs | `openapi.yaml`, `openapi.yml`, `openapi.json`, `swagger.yaml`, `swagger.json` |
| Changelog | `CHANGELOG.md`, `CHANGELOG`, `CHANGES.md`, `HISTORY.md` |
| Contributing | `CONTRIBUTING.md` |
| Docs directory | `docs/` |

---

## Step 8: Project Type Inference

Apply the scoring matrix from `analysis-guide.md` (section "Type Inference
Scoring Matrix") using data collected in Steps 1-7.

Additionally, check `recent_commit_messages` (Step 6) for refactor keywords:

```
refactor, rewrite, migrate, migration, redesign, restructure,
overhaul, v2, 新架构, 重构, 迁移, 重写
```

- 3+ matches → +3 refactor
- 1-2 matches → +1 refactor

Check `key_directories` for:
- Legacy/deprecated directories (`old`, `legacy`, `deprecated`, `v1`, `backup`) → +3 refactor
- Parallel old/new structures (`src` + `src-new`, `v1` + `v2`, etc.) → +3 refactor
- Migration directories (name contains `migration` or `migrate`) → +2 refactor

**Confidence**: `0.5 + (lead over second place * 0.1)`, capped at 0.95.

---

## Summary Presentation

Present the analysis to the user in this format:

```
Project Analysis Summary
========================
Tech Stack:    [language] / [frameworks] / [package manager]
Architecture:  [pattern] ([confidence]%)
Scale:         [total files] files, [total lines] lines
Quality:       Testing: [framework] ([count] files) | CI: [platform] | Lint: [tools]
Git:           [commits] commits, [age] days, [contributors] contributors
Documentation: README [✓/✗] | CLAUDE.md [✓/✗] | API docs [✓/✗]

[For refactor projects only]
Refactor Setup:
  Legacy:      [LEGACY_DIR]
  Target:      [TARGET_DIR]
  Approach:    [In-place / Clean slate]
```

---

## Data Field → Template Placeholder Mapping

| Data field | Placeholder(s) | Source step |
|------------|----------------|------------|
| Project name | `{{PROJECT_NAME}}` | Last segment of SOURCE_PATH |
| One-line description | `{{ONE_LINE_DESCRIPTION}}` | README first paragraph or package.json `description` |
| Primary language | `{{PRIMARY_LANGUAGE}}` | Step 2: language with most code lines |
| Language version | `{{LANGUAGE_VERSION}}` | Step 2: from config files (e.g., `engines.node` in package.json) |
| Primary framework | `{{FRAMEWORK}}` | Step 2: first detected framework |
| Framework version | `{{FRAMEWORK_VERSION}}` | Step 2: from dependency version |
| Package manager | `{{PACKAGE_MANAGER}}` | Step 2: detected package manager |
| Build tool | `{{BUILD_TOOL}}` | Step 2: detected build tool |
| Install command | `{{INSTALL_CMD}}` | Step 2: derived from package manager |
| Dev command | `{{DEV_CMD}}` | Step 2: from scripts or convention |
| Build command | `{{BUILD_CMD}}` | Step 2: from scripts or convention |
| Test command | `{{TEST_CMD}}` | Step 2: from test framework + PM |
| Lint command | `{{LINT_CMD}}` | Step 2: from lint tools + PM |
| Coverage command | `{{COVERAGE_CMD}}` | Step 3: from coverage config + PM |
| Test framework | `{{TEST_FRAMEWORK}}` | Step 3: detected framework |
| CI platform | `{{CI_PLATFORM}}` | Step 3: detected platform |
| Lint tools | `{{LINT_TOOLS}}` | Step 3: detected tools (comma-separated) |
| Format tools | `{{FORMAT_TOOLS}}` | Step 3: detected formatters |
| Type checking | `{{TYPE_CHECK}}` | Step 3: tools found (tsconfig/mypy/pyright) |
| Lint convention | `{{LINT_CONVENTION}}` | Step 3: tool + config style |
| Format convention | `{{FORMAT_CONVENTION}}` | Step 3: tool + config style |
| Type check convention | `{{TYPE_CHECK_CONVENTION}}` | Step 3: tool + strictness |
| Architecture pattern | `{{ARCHITECTURE}}` | Step 4: highest-scoring pattern |
| Directory tree | `{{DIRECTORY_TREE}}` | Step 1: formatted tree |
| Entry points / key files | `{{KEY_FILES}}` | Step 4: entry points + churn files |
| Monorepo flag | (inline in templates) | Step 4: is_monorepo |
| Total commits | `{{TOTAL_COMMITS}}` | Step 6: commit count |
| Contributors | `{{CONTRIBUTORS}}` | Step 6: contributor count |
| Repo age | `{{REPO_AGE}}` | Step 6: days since first commit |
| High-churn files | `{{HIGH_CHURN_FILES}}` | Step 6: top 10 changed files |
| Module descriptions | `{{MODULE_DESCRIPTIONS}}` | Step 4: qualitative analysis |
| Data flow | `{{DATA_FLOW_DESCRIPTION}}` | Step 4: qualitative analysis |
| Observed patterns | `{{OBSERVED_PATTERNS}}` | Step 4: qualitative analysis |
| Naming conventions | `{{NAMING_CONVENTIONS}}` | Step 4: qualitative analysis |

**Note**: Placeholders prefixed with `{{INTENT_*}}` come from Phase 4
(intent collection), not from this analysis. Remaining placeholders such
as `{{BUSINESS_RULES}}`, `{{EXTERNAL_INTEGRATIONS}}`, `{{DATABASE_DETAILS}}`
are populated by Claude's interpretation of the codebase during template
generation (Phase 6) or marked `[NEEDS CLARIFICATION]`.
