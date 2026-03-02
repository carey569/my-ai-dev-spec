#!/usr/bin/env python3
"""
Codebase Analyzer for AI Workflow Generator.

Analyzes a project directory and outputs structured JSON with:
- File statistics (counts, lines, extensions)
- Tech stack detection (languages, frameworks, package managers)
- Quality infrastructure (testing, CI/CD, linting, formatting)
- Architecture pattern recognition
- Dependency analysis
- Git metrics
- Documentation assessment
- Project type inference (new / maintenance / refactor)

Usage:
    python3 analyze_codebase.py [TARGET_PATH] [--help]

Output:
    Structured JSON to stdout. Errors/warnings to stderr.
"""

import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

EXCLUDED_DIRS = {
    "node_modules", ".git", "__pycache__", "venv", ".venv", "env",
    "dist", "build", "target", ".next", ".nuxt", ".output",
    "coverage", ".pytest_cache", ".mypy_cache", ".tox",
    "vendor", "Pods", ".gradle", ".idea", ".vscode",
    ".DS_Store", ".cache", ".parcel-cache", ".turbo",
    "out", "bin", "obj", ".svn", ".hg",
}

BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".exe", ".dll", ".so", ".dylib", ".o", ".a",
    ".mp3", ".mp4", ".avi", ".mov", ".wav", ".flac",
    ".pyc", ".pyo", ".class", ".jar", ".war",
    ".wasm", ".min.js", ".min.css",
    ".lock", ".log",
}

LANGUAGE_MAP = {
    ".py": "Python", ".pyw": "Python",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".mts": "TypeScript",
    ".jsx": "JavaScript",
    ".java": "Java", ".kt": "Kotlin", ".kts": "Kotlin",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby", ".erb": "Ruby",
    ".php": "PHP",
    ".cs": "C#",
    ".cpp": "C++", ".cc": "C++", ".cxx": "C++", ".hpp": "C++", ".h": "C/C++",
    ".c": "C",
    ".swift": "Swift",
    ".scala": "Scala",
    ".ex": "Elixir", ".exs": "Elixir",
    ".erl": "Erlang",
    ".lua": "Lua",
    ".r": "R", ".R": "R",
    ".dart": "Dart",
    ".vue": "Vue",
    ".svelte": "Svelte",
    ".sql": "SQL",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell",
    ".md": "Markdown",
    ".json": "JSON", ".yaml": "YAML", ".yml": "YAML", ".toml": "TOML",
    ".xml": "XML",
    ".html": "HTML", ".htm": "HTML",
    ".css": "CSS", ".scss": "SCSS", ".sass": "SASS", ".less": "LESS",
}

GIT_TIMEOUT = 10  # seconds
MAX_LINES_PER_FILE = 50000
MAX_WALK_DEPTH = 10


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def run_git(args, cwd, default=None):
    """Run a git command with timeout, return stdout or default on failure."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd, capture_output=True, text=True, timeout=GIT_TIMEOUT
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return default
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return default


def is_binary_file(filepath):
    """Check if a file is binary by extension or content probe."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext in BINARY_EXTENSIONS:
        return True
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(1024)
            if b"\x00" in chunk:
                return True
    except (OSError, IOError):
        return True
    return False


def count_lines(filepath):
    """Count lines in a text file, capped at MAX_LINES_PER_FILE."""
    try:
        count = 0
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for _ in f:
                count += 1
                if count >= MAX_LINES_PER_FILE:
                    break
        return count
    except (OSError, IOError):
        return 0


def safe_json_load(filepath):
    """Load a JSON file, return None on failure."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError, IOError):
        return None


def safe_read(filepath):
    """Read a text file, return empty string on failure."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except (OSError, IOError):
        return ""


# ---------------------------------------------------------------------------
# Analysis Modules
# ---------------------------------------------------------------------------

def analyze_file_statistics(root):
    """Walk the directory tree and collect file statistics."""
    total_files = 0
    total_lines = 0
    ext_stats = defaultdict(lambda: {"count": 0, "lines": 0})
    key_dirs = set()

    for dirpath, dirnames, filenames in os.walk(root):
        # Calculate depth relative to root
        rel = os.path.relpath(dirpath, root)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if depth >= MAX_WALK_DEPTH:
            dirnames.clear()
            continue

        # Filter excluded directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".")]

        # Track key directories (depth 1-2)
        if 0 < depth <= 2 and filenames:
            key_dirs.add(os.path.relpath(dirpath, root) + "/")

        for fname in filenames:
            if fname.startswith("."):
                continue
            fpath = os.path.join(dirpath, fname)
            ext = os.path.splitext(fname)[1].lower()

            if is_binary_file(fpath):
                ext_stats[ext]["count"] += 1
                total_files += 1
                continue

            lines = count_lines(fpath)
            ext_stats[ext]["count"] += 1
            ext_stats[ext]["lines"] += lines
            total_files += 1
            total_lines += lines

    # Sort by line count descending, take top entries
    sorted_exts = dict(sorted(ext_stats.items(), key=lambda x: x[1]["lines"], reverse=True))

    return {
        "total_files": total_files,
        "total_lines": total_lines,
        "by_extension": sorted_exts,
        "key_directories": sorted(key_dirs)[:20],
    }


def detect_tech_stack(root):
    """Detect languages, frameworks, package managers, and build tools."""
    result = {
        "primary_language": None,
        "languages": [],
        "frameworks": [],
        "package_manager": None,
        "build_tools": [],
        "runtime": None,
    }

    # Detect by dependency/config files
    frameworks = []
    build_tools = []

    # --- Node.js ecosystem ---
    pkg_json_path = os.path.join(root, "package.json")
    pkg_data = safe_json_load(pkg_json_path)
    if pkg_data:
        result["runtime"] = "node"
        deps = {}
        deps.update(pkg_data.get("dependencies", {}))
        deps.update(pkg_data.get("devDependencies", {}))

        # Frameworks
        framework_map = {
            "next": "Next.js", "nuxt": "Nuxt.js", "react": "React",
            "vue": "Vue.js", "@angular/core": "Angular", "svelte": "Svelte",
            "express": "Express", "fastify": "Fastify", "koa": "Koa",
            "nest": "NestJS", "@nestjs/core": "NestJS",
            "electron": "Electron", "gatsby": "Gatsby", "remix": "Remix",
            "astro": "Astro", "vite": "Vite",
        }
        for dep, name in framework_map.items():
            if dep in deps:
                frameworks.append(name)

        # Package manager
        if os.path.exists(os.path.join(root, "pnpm-lock.yaml")):
            result["package_manager"] = "pnpm"
        elif os.path.exists(os.path.join(root, "yarn.lock")):
            result["package_manager"] = "yarn"
        elif os.path.exists(os.path.join(root, "bun.lockb")) or os.path.exists(os.path.join(root, "bun.lock")):
            result["package_manager"] = "bun"
        elif os.path.exists(os.path.join(root, "package-lock.json")):
            result["package_manager"] = "npm"

        # Build tools from scripts
        scripts = pkg_data.get("scripts", {})
        script_vals = " ".join(scripts.values())
        for tool in ["webpack", "vite", "rollup", "esbuild", "parcel", "turbo", "tsc", "swc"]:
            if tool in script_vals or tool in deps:
                build_tools.append(tool)

    # --- Python ecosystem ---
    py_configs = ["pyproject.toml", "requirements.txt", "setup.py", "setup.cfg", "Pipfile"]
    for cfg in py_configs:
        if os.path.exists(os.path.join(root, cfg)):
            result["runtime"] = result["runtime"] or "python"
            break

    pyproject_path = os.path.join(root, "pyproject.toml")
    if os.path.exists(pyproject_path):
        content = safe_read(pyproject_path)
        py_framework_patterns = {
            "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
            "starlette": "Starlette", "tornado": "Tornado",
            "celery": "Celery", "sqlalchemy": "SQLAlchemy",
        }
        for pattern, name in py_framework_patterns.items():
            if pattern in content.lower():
                frameworks.append(name)

        if "poetry" in content:
            result["package_manager"] = result["package_manager"] or "poetry"
        elif os.path.exists(os.path.join(root, "Pipfile")):
            result["package_manager"] = result["package_manager"] or "pipenv"
        elif os.path.exists(os.path.join(root, "uv.lock")):
            result["package_manager"] = result["package_manager"] or "uv"
        else:
            result["package_manager"] = result["package_manager"] or "pip"

    req_path = os.path.join(root, "requirements.txt")
    if os.path.exists(req_path):
        content = safe_read(req_path).lower()
        py_framework_patterns = {
            "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
        }
        for pattern, name in py_framework_patterns.items():
            if pattern in content and name not in frameworks:
                frameworks.append(name)
        result["package_manager"] = result["package_manager"] or "pip"

    # --- Go ---
    if os.path.exists(os.path.join(root, "go.mod")):
        result["runtime"] = result["runtime"] or "go"
        result["package_manager"] = result["package_manager"] or "go modules"
        content = safe_read(os.path.join(root, "go.mod"))
        go_frameworks = {"gin-gonic/gin": "Gin", "labstack/echo": "Echo", "gofiber/fiber": "Fiber"}
        for pattern, name in go_frameworks.items():
            if pattern in content:
                frameworks.append(name)

    # --- Rust ---
    if os.path.exists(os.path.join(root, "Cargo.toml")):
        result["runtime"] = result["runtime"] or "rust"
        result["package_manager"] = result["package_manager"] or "cargo"
        content = safe_read(os.path.join(root, "Cargo.toml"))
        rust_frameworks = {"actix-web": "Actix", "rocket": "Rocket", "axum": "Axum", "tokio": "Tokio"}
        for pattern, name in rust_frameworks.items():
            if pattern in content:
                frameworks.append(name)

    # --- Java/Kotlin ---
    if os.path.exists(os.path.join(root, "pom.xml")):
        result["runtime"] = result["runtime"] or "jvm"
        result["package_manager"] = result["package_manager"] or "maven"
        # Check root and submodule pom.xml files for Spring
        pom_files = [os.path.join(root, "pom.xml")]
        for item in os.listdir(root):
            sub_pom = os.path.join(root, item, "pom.xml")
            if os.path.isfile(sub_pom):
                pom_files.append(sub_pom)
        for pom_path in pom_files:
            content = safe_read(pom_path).lower()
            if "spring-boot" in content:
                if "Spring Boot" not in frameworks:
                    frameworks.append("Spring Boot")
                break
            elif "spring" in content:
                if "Spring" not in frameworks:
                    frameworks.append("Spring")
                break
        build_tools.append("maven")
    elif os.path.exists(os.path.join(root, "build.gradle")) or os.path.exists(os.path.join(root, "build.gradle.kts")):
        result["runtime"] = result["runtime"] or "jvm"
        result["package_manager"] = result["package_manager"] or "gradle"
        # Check for Spring in gradle files
        for gf in ["build.gradle", "build.gradle.kts"]:
            gf_path = os.path.join(root, gf)
            if os.path.exists(gf_path):
                content = safe_read(gf_path).lower()
                if "spring-boot" in content and "Spring Boot" not in frameworks:
                    frameworks.append("Spring Boot")
                elif "spring" in content and "Spring" not in frameworks:
                    frameworks.append("Spring")
        build_tools.append("gradle")

    # --- Ruby ---
    if os.path.exists(os.path.join(root, "Gemfile")):
        result["runtime"] = result["runtime"] or "ruby"
        result["package_manager"] = result["package_manager"] or "bundler"
        content = safe_read(os.path.join(root, "Gemfile"))
        if "rails" in content.lower():
            frameworks.append("Rails")
        if "sinatra" in content.lower():
            frameworks.append("Sinatra")

    # --- Swift ---
    if os.path.exists(os.path.join(root, "Package.swift")):
        result["runtime"] = result["runtime"] or "swift"
        result["package_manager"] = result["package_manager"] or "swift-pm"

    # --- Elixir ---
    if os.path.exists(os.path.join(root, "mix.exs")):
        result["runtime"] = result["runtime"] or "elixir"
        result["package_manager"] = result["package_manager"] or "mix"
        content = safe_read(os.path.join(root, "mix.exs"))
        if "phoenix" in content.lower():
            frameworks.append("Phoenix")

    result["frameworks"] = list(dict.fromkeys(frameworks))  # dedupe preserving order
    result["build_tools"] = list(dict.fromkeys(build_tools))

    return result


def compute_language_stats(file_stats):
    """Compute language distribution from file statistics."""
    lang_lines = Counter()
    for ext, stats in file_stats.get("by_extension", {}).items():
        lang = LANGUAGE_MAP.get(ext)
        if lang and lang not in ("JSON", "YAML", "TOML", "XML", "Markdown", "HTML", "CSS", "SCSS", "SASS", "LESS"):
            lang_lines[lang] += stats.get("lines", 0)

    total = sum(lang_lines.values()) or 1
    languages = [
        {"name": lang, "percentage": round(lines / total * 100, 1)}
        for lang, lines in lang_lines.most_common()
    ]
    primary = languages[0]["name"] if languages else None
    return primary, languages


def assess_quality(root):
    """Assess testing, CI/CD, linting, formatting, and type checking."""
    quality = {
        "testing": {"framework": None, "test_file_count": 0, "coverage_config": False},
        "ci_cd": {"platform": None, "pipeline_count": 0},
        "linting": {"tools": []},
        "formatting": {"tools": []},
        "type_checking": False,
    }

    # --- Testing ---
    test_dirs = ["tests", "test", "__tests__", "spec", "cypress", "e2e", "integration"]
    test_file_count = 0
    for td in test_dirs:
        td_path = os.path.join(root, td)
        if os.path.isdir(td_path):
            for dp, _, fns in os.walk(td_path):
                test_file_count += len(fns)

    # Count test files in src/ (co-located tests)
    src_path = os.path.join(root, "src")
    if os.path.isdir(src_path):
        for dp, _, fns in os.walk(src_path):
            for fn in fns:
                if re.search(r"(test|spec)\.(js|ts|jsx|tsx|py|go|rs|java|rb)$", fn, re.I):
                    test_file_count += 1
                elif fn.startswith("test_") or fn.endswith("_test.py") or fn.endswith("_test.go"):
                    test_file_count += 1

    quality["testing"]["test_file_count"] = test_file_count

    # Test frameworks
    test_framework_files = {
        "jest.config": "jest", "jest.config.js": "jest", "jest.config.ts": "jest",
        "vitest.config": "vitest", "vitest.config.ts": "vitest",
        "pytest.ini": "pytest", "conftest.py": "pytest",
        ".rspec": "rspec", "karma.conf.js": "karma",
        "cypress.config": "cypress",
        "playwright.config": "playwright",
    }
    for fname, framework in test_framework_files.items():
        matches = [f for f in os.listdir(root) if f.startswith(fname)] if os.path.isdir(root) else []
        if matches:
            quality["testing"]["framework"] = framework
            break

    # Check pyproject.toml for pytest
    pyproject = os.path.join(root, "pyproject.toml")
    if os.path.exists(pyproject) and "pytest" in safe_read(pyproject):
        quality["testing"]["framework"] = quality["testing"]["framework"] or "pytest"

    # Coverage config
    coverage_markers = [".nycrc", ".coveragerc", "coverage", ".c8rc"]
    for marker in coverage_markers:
        if os.path.exists(os.path.join(root, marker)):
            quality["testing"]["coverage_config"] = True
            break
    # Check package.json for coverage scripts
    pkg = safe_json_load(os.path.join(root, "package.json"))
    if pkg:
        scripts = pkg.get("scripts", {})
        if any("coverage" in v for v in scripts.values()):
            quality["testing"]["coverage_config"] = True

    # --- CI/CD ---
    ci_checks = [
        (".github/workflows", "github-actions"),
        (".gitlab-ci.yml", "gitlab-ci"),
        ("Jenkinsfile", "jenkins"),
        (".circleci", "circleci"),
        (".travis.yml", "travis"),
        ("azure-pipelines.yml", "azure-devops"),
        ("bitbucket-pipelines.yml", "bitbucket"),
    ]
    for path, platform in ci_checks:
        full = os.path.join(root, path)
        if os.path.exists(full):
            quality["ci_cd"]["platform"] = platform
            if os.path.isdir(full):
                quality["ci_cd"]["pipeline_count"] = len([
                    f for f in os.listdir(full) if f.endswith((".yml", ".yaml"))
                ])
            else:
                quality["ci_cd"]["pipeline_count"] = 1
            break

    # --- Linting ---
    lint_checks = {
        "eslint": [".eslintrc", ".eslintrc.js", ".eslintrc.json", ".eslintrc.yml", "eslint.config.js", "eslint.config.mjs"],
        "pylint": [".pylintrc", "pylintrc"],
        "flake8": [".flake8"],
        "ruff": ["ruff.toml", ".ruff.toml"],
        "rubocop": [".rubocop.yml"],
        "golangci-lint": [".golangci.yml", ".golangci.yaml"],
        "stylelint": [".stylelintrc", ".stylelintrc.json"],
    }
    for tool, files in lint_checks.items():
        for f in files:
            if os.path.exists(os.path.join(root, f)):
                quality["linting"]["tools"].append(tool)
                break

    # Check pyproject.toml for ruff/pylint
    if os.path.exists(pyproject):
        content = safe_read(pyproject)
        if "[tool.ruff" in content and "ruff" not in quality["linting"]["tools"]:
            quality["linting"]["tools"].append("ruff")

    # --- Formatting ---
    format_checks = {
        "prettier": [".prettierrc", ".prettierrc.js", ".prettierrc.json", "prettier.config.js"],
        "black": [],  # checked via pyproject.toml
        "editorconfig": [".editorconfig"],
        "clang-format": [".clang-format"],
    }
    for tool, files in format_checks.items():
        for f in files:
            if os.path.exists(os.path.join(root, f)):
                quality["formatting"]["tools"].append(tool)
                break

    if os.path.exists(pyproject):
        content = safe_read(pyproject)
        if "[tool.black" in content:
            quality["formatting"]["tools"].append("black")
        if "[tool.ruff.format" in content:
            if "ruff-format" not in quality["formatting"]["tools"]:
                quality["formatting"]["tools"].append("ruff-format")

    # --- Type Checking ---
    type_checks = ["tsconfig.json", "mypy.ini", "pyrightconfig.json"]
    for f in type_checks:
        if os.path.exists(os.path.join(root, f)):
            quality["type_checking"] = True
            break
    if os.path.exists(pyproject) and "[tool.mypy" in safe_read(pyproject):
        quality["type_checking"] = True

    return quality


def recognize_architecture(root, file_stats):
    """Recognize architectural patterns from directory structure."""
    result = {
        "pattern": "unknown",
        "confidence": 0.0,
        "indicators": [],
        "is_monorepo": False,
        "entry_points": [],
    }

    dirs = set()
    for d in file_stats.get("key_directories", []):
        parts = d.strip("/").split("/")
        dirs.update(parts)

    # Pattern scoring
    patterns = {
        "mvc": {"controllers": 2, "models": 2, "views": 2, "routes": 1},
        "layered": {"services": 2, "repositories": 1, "controllers": 1, "middleware": 1, "utils": 1},
        "ddd": {"domain": 3, "application": 2, "infrastructure": 2, "ports": 1, "adapters": 1},
        "spa-frontend": {"components": 3, "pages": 2, "hooks": 2, "stores": 1, "store": 1, "assets": 1},
        "api-server": {"routes": 2, "handlers": 2, "middleware": 2, "models": 1, "services": 1},
        "serverless": {"functions": 3, "lambda": 3, "handlers": 2},
    }

    best_pattern = "unknown"
    best_score = 0
    best_indicators = []

    for pattern_name, signals in patterns.items():
        score = 0
        indicators = []
        for dir_name, weight in signals.items():
            if dir_name in dirs:
                score += weight
                indicators.append(dir_name + "/")
        if score > best_score:
            best_score = score
            best_pattern = pattern_name
            best_indicators = indicators

    max_possible = max(sum(s.values()) for s in patterns.values())
    confidence = min(best_score / max_possible, 1.0) if max_possible else 0.0

    if best_score >= 3:
        result["pattern"] = best_pattern
        result["confidence"] = round(confidence, 2)
        result["indicators"] = best_indicators

    # Monorepo detection
    monorepo_markers = ["packages", "apps", "modules", "libs", "services"]
    for marker in monorepo_markers:
        marker_path = os.path.join(root, marker)
        if os.path.isdir(marker_path):
            subdirs = [d for d in os.listdir(marker_path) if os.path.isdir(os.path.join(marker_path, d))]
            if len(subdirs) >= 2:
                result["is_monorepo"] = True
                break

    mono_config_files = ["lerna.json", "nx.json", "turbo.json", "pnpm-workspace.yaml"]
    for f in mono_config_files:
        if os.path.exists(os.path.join(root, f)):
            result["is_monorepo"] = True
            break

    # Entry points
    entry_candidates = [
        "main.py", "app.py", "server.py", "manage.py",
        "main.go", "main.rs", "main.java",
        "index.js", "index.ts", "index.tsx",
        "src/main.py", "src/app.py", "src/main.ts", "src/index.ts",
        "src/main.go", "src/main.rs", "src/main.java",
        "src/index.js", "src/index.tsx",
        "src/pages/index.tsx", "src/pages/index.js",
        "cmd/main.go",
    ]
    for candidate in entry_candidates:
        if os.path.exists(os.path.join(root, candidate)):
            result["entry_points"].append(candidate)

    return result


def analyze_dependencies(root, tech_stack):
    """Parse dependency files and extract key information."""
    result = {
        "total_count": 0,
        "dev_dependency_count": 0,
        "key_dependencies": [],
    }

    # Node.js
    pkg = safe_json_load(os.path.join(root, "package.json"))
    if pkg:
        deps = pkg.get("dependencies", {})
        dev_deps = pkg.get("devDependencies", {})
        result["total_count"] = len(deps) + len(dev_deps)
        result["dev_dependency_count"] = len(dev_deps)
        result["key_dependencies"] = list(deps.keys())[:15]
        return result

    # Python - requirements.txt
    req_path = os.path.join(root, "requirements.txt")
    if os.path.exists(req_path):
        lines = safe_read(req_path).strip().splitlines()
        deps = [l.split("==")[0].split(">=")[0].split("<=")[0].split("[")[0].strip()
                for l in lines if l.strip() and not l.startswith("#") and not l.startswith("-")]
        result["total_count"] = len(deps)
        result["key_dependencies"] = deps[:15]
        return result

    # Go - go.mod
    gomod_path = os.path.join(root, "go.mod")
    if os.path.exists(gomod_path):
        content = safe_read(gomod_path)
        requires = re.findall(r"^\s+(\S+)\s+v", content, re.MULTILINE)
        result["total_count"] = len(requires)
        result["key_dependencies"] = [r.split("/")[-1] for r in requires[:15]]
        return result

    # Rust - Cargo.toml
    cargo_path = os.path.join(root, "Cargo.toml")
    if os.path.exists(cargo_path):
        content = safe_read(cargo_path)
        deps_section = re.findall(r'\[dependencies\](.*?)(?:\[|\Z)', content, re.DOTALL)
        if deps_section:
            dep_names = re.findall(r'^(\w[\w-]*)\s*=', deps_section[0], re.MULTILINE)
            result["total_count"] = len(dep_names)
            result["key_dependencies"] = dep_names[:15]
        return result

    return result


def collect_git_metrics(root):
    """Collect git repository metrics."""
    result = {
        "is_git_repo": False,
        "total_commits": 0,
        "repo_age_days": 0,
        "active_contributors": 0,
        "recent_commit_frequency": {"last_30d": 0, "last_90d": 0},
        "most_changed_files": [],
        "branch_count": 0,
        "recent_commit_messages": [],
    }

    # Check if git repo
    git_check = run_git(["rev-parse", "--is-inside-work-tree"], root)
    if git_check != "true":
        return result

    result["is_git_repo"] = True

    # Total commits
    commit_count = run_git(["rev-list", "--count", "HEAD"], root, "0")
    result["total_commits"] = int(commit_count) if commit_count else 0

    # Repo age
    first_commit = run_git(["log", "--reverse", "--format=%aI", "--max-count=1"], root)
    if first_commit:
        try:
            first_date = datetime.fromisoformat(first_commit.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            result["repo_age_days"] = (now - first_date).days
        except (ValueError, TypeError):
            pass

    # Contributors
    shortlog = run_git(["shortlog", "-sn", "--no-merges"], root, "")
    if shortlog:
        result["active_contributors"] = len(shortlog.strip().splitlines())

    # Recent activity
    last_30d = run_git(["rev-list", "--count", "--since=30 days ago", "HEAD"], root, "0")
    last_90d = run_git(["rev-list", "--count", "--since=90 days ago", "HEAD"], root, "0")
    result["recent_commit_frequency"]["last_30d"] = int(last_30d) if last_30d else 0
    result["recent_commit_frequency"]["last_90d"] = int(last_90d) if last_90d else 0

    # Most changed files (top 10)
    churn = run_git(["log", "--format=format:", "--name-only", "--max-count=200"], root, "")
    if churn:
        files = [f for f in churn.strip().splitlines() if f.strip()]
        counter = Counter(files)
        result["most_changed_files"] = [f for f, _ in counter.most_common(10)]

    # Branch count
    branches = run_git(["branch", "-a"], root, "")
    if branches:
        result["branch_count"] = len(branches.strip().splitlines())

    # Recent commit messages (for refactor signal detection)
    recent_msgs = run_git(["log", "--oneline", "--max-count=30"], root, "")
    if recent_msgs:
        result["recent_commit_messages"] = recent_msgs.strip().splitlines()[:30]

    return result


def assess_documentation(root):
    """Assess documentation coverage."""
    result = {
        "readme_exists": False,
        "readme_lines": 0,
        "claude_md_exists": False,
        "api_docs_exist": False,
        "changelog_exists": False,
        "contributing_exists": False,
        "docs_directory_exists": False,
    }

    readme_path = os.path.join(root, "README.md")
    if os.path.exists(readme_path):
        result["readme_exists"] = True
        result["readme_lines"] = count_lines(readme_path)

    result["claude_md_exists"] = os.path.exists(os.path.join(root, "CLAUDE.md"))
    result["docs_directory_exists"] = os.path.isdir(os.path.join(root, "docs"))
    result["changelog_exists"] = any(
        os.path.exists(os.path.join(root, f))
        for f in ["CHANGELOG.md", "CHANGELOG", "CHANGES.md", "HISTORY.md"]
    )
    result["contributing_exists"] = os.path.exists(os.path.join(root, "CONTRIBUTING.md"))

    api_doc_patterns = ["openapi.yaml", "openapi.yml", "openapi.json", "swagger.yaml", "swagger.json"]
    result["api_docs_exist"] = any(
        os.path.exists(os.path.join(root, f)) for f in api_doc_patterns
    )

    return result


def infer_project_type(file_stats, git_metrics, quality, documentation):
    """Infer project type using weighted scoring."""
    scores = {"new": 0, "maintenance": 0, "refactor": 0}
    signals = {"new": [], "maintenance": [], "refactor": []}

    total_files = file_stats.get("total_files", 0)
    total_commits = git_metrics.get("total_commits", 0)
    repo_age = git_metrics.get("repo_age_days", 0)
    contributors = git_metrics.get("active_contributors", 0)
    is_git = git_metrics.get("is_git_repo", False)
    test_count = quality.get("testing", {}).get("test_file_count", 0)
    has_ci = quality.get("ci_cd", {}).get("platform") is not None
    has_coverage = quality.get("testing", {}).get("coverage_config", False)

    # --- New project signals ---
    if total_files == 0:
        scores["new"] += 5
        signals["new"].append("Empty directory - no files found")
    elif total_files < 15:
        scores["new"] += 3
        signals["new"].append(f"Very few files ({total_files})")

    if not is_git:
        scores["new"] += 2
        signals["new"].append("Not a git repository")
    elif total_commits < 10:
        scores["new"] += 3
        signals["new"].append(f"Very few commits ({total_commits})")

    if is_git and repo_age < 14:
        scores["new"] += 2
        signals["new"].append(f"Repository is only {repo_age} days old")

    if test_count == 0 and total_files > 0:
        scores["new"] += 1
        signals["new"].append("No test files found")

    if not has_ci and total_files > 0:
        scores["new"] += 1
        signals["new"].append("No CI/CD configuration")

    # --- Maintenance signals ---
    if total_commits > 100:
        scores["maintenance"] += 2
        signals["maintenance"].append(f"Substantial commit history ({total_commits} commits)")

    if contributors > 1:
        scores["maintenance"] += 2
        signals["maintenance"].append(f"Multiple contributors ({contributors})")

    if has_ci:
        scores["maintenance"] += 2
        signals["maintenance"].append("CI/CD pipeline configured")

    if has_coverage:
        scores["maintenance"] += 1
        signals["maintenance"].append("Test coverage tracking configured")

    if test_count > 10:
        scores["maintenance"] += 2
        signals["maintenance"].append(f"Established test suite ({test_count} test files)")

    if repo_age > 90:
        scores["maintenance"] += 1
        signals["maintenance"].append(f"Mature repository ({repo_age} days old)")

    if documentation.get("changelog_exists"):
        scores["maintenance"] += 1
        signals["maintenance"].append("CHANGELOG exists")

    # --- Refactor signals ---
    recent_msgs = git_metrics.get("recent_commit_messages", [])
    refactor_keywords = ["refactor", "rewrite", "migrate", "migration", "redesign",
                         "restructure", "overhaul", "v2", "新架构", "重构", "迁移", "重写"]
    refactor_msg_count = sum(
        1 for msg in recent_msgs
        if any(kw in msg.lower() for kw in refactor_keywords)
    )
    if refactor_msg_count >= 3:
        scores["refactor"] += 3
        signals["refactor"].append(f"Refactor-related keywords found in {refactor_msg_count} recent commits")
    elif refactor_msg_count >= 1:
        scores["refactor"] += 1
        signals["refactor"].append(f"Refactor-related keywords in {refactor_msg_count} recent commit(s)")

    # Check for deprecated markers
    deprecated_files = []
    for d in file_stats.get("key_directories", []):
        d_lower = d.lower()
        if any(kw in d_lower for kw in ["old", "legacy", "deprecated", "v1", "backup"]):
            deprecated_files.append(d)
    if deprecated_files:
        scores["refactor"] += 3
        signals["refactor"].append(f"Legacy/deprecated directories found: {', '.join(deprecated_files)}")

    # Check for new+old parallel structures
    key_dirs = [d.strip("/").lower() for d in file_stats.get("key_directories", [])]
    parallel_pairs = [("src", "src-new"), ("app", "app-new"), ("old", "new"), ("v1", "v2")]
    for old, new in parallel_pairs:
        if old in key_dirs and new in key_dirs:
            scores["refactor"] += 3
            signals["refactor"].append(f"Parallel structures found: {old}/ and {new}/")

    # Migration files
    migration_dirs = [d for d in key_dirs if "migration" in d or "migrate" in d]
    if migration_dirs:
        scores["refactor"] += 2
        signals["refactor"].append(f"Migration directories found: {', '.join(migration_dirs)}")

    # Determine winner
    max_score = max(scores.values())
    if max_score == 0:
        suggested_type = "new"
        confidence = 0.5
    else:
        suggested_type = max(scores, key=scores.get)
        # Simple confidence: how much does the winner lead?
        sorted_scores = sorted(scores.values(), reverse=True)
        lead = sorted_scores[0] - sorted_scores[1] if len(sorted_scores) > 1 else sorted_scores[0]
        confidence = min(0.5 + lead * 0.1, 0.95)

    return {
        "suggested_type": suggested_type,
        "confidence": round(confidence, 2),
        "scores": scores,
        "signals": signals,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def analyze(target_path):
    """Run full analysis and return structured result."""
    root = os.path.abspath(target_path)

    if not os.path.isdir(root):
        return {"error": f"Not a valid directory: {root}"}

    # Run all analysis modules
    file_stats = analyze_file_statistics(root)
    tech_stack = detect_tech_stack(root)
    primary_lang, languages = compute_language_stats(file_stats)
    tech_stack["primary_language"] = primary_lang
    tech_stack["languages"] = languages
    quality = assess_quality(root)
    architecture = recognize_architecture(root, file_stats)
    dependencies = analyze_dependencies(root, tech_stack)
    git_metrics = collect_git_metrics(root)
    documentation = assess_documentation(root)
    maturity = infer_project_type(file_stats, git_metrics, quality, documentation)

    return {
        "project_root": root,
        "analysis_timestamp": datetime.now(timezone.utc).isoformat(),
        "file_statistics": file_stats,
        "tech_stack": tech_stack,
        "quality": quality,
        "architecture": architecture,
        "dependencies": dependencies,
        "git_metrics": git_metrics,
        "documentation": documentation,
        "maturity_inference": maturity,
    }


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    result = analyze(target)

    if "error" in result:
        print(json.dumps(result, indent=2, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
