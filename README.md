# pythonic-quickstart

이 레레포지토리는 Python 개발 환경에서 정적 분석 및 테스트 자동화를 실습할 수 있도록 구성된 템플릿입니다.

## 목표

- 코드 스타일 점검 및 자동 포맷
- 타입 안전성 확보
- 자동화된 테스트 작성 및 실행

## uv 설치 방법

```bash
# With pip.
pip install uv

# With Homebrew.
brew install uv
```

## uv Python 설치

```
uv python install 3.10 3.11 3.12
```

## uv 가상환경 관리

```
uv venv --python 3.12
```

## 가상환경 접근

```
# On macOS and Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\Activate.ps1
```

## 의존성 관리

```
# 의존성 추가
uv add ruff mypy pytest

# 버전을 명시하려면
uv add ruff==0.11.4

# 의존성 삭제
uv remove ruff

# 개발용으로 추가
uv add ruff --dev
```

## uv.lock 동기화

```
uv sync
```

## 실습 방법

- ruff 오류 테스트:

```bash
uv run ruff check broken_code/ruff_example.py
```

- mypy 타입 검사:

```bash
uv run mypy broken_code/mypy_example.py
```

- pytest 테스트 실행:

```bash
uv run pytest
```

## ⚙️ `mypy.ini` 설정 설명

```ini
[mypy]
strict = True
ignore_missing_imports = True
```

| 옵션                            | 설명                                                                                                                                                                                         |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `strict = True`                 | 엄격한 타입 검사 모드를 활성화합니다. 아래 항목들이 한 번에 켜집니다:<br> `warn_unused_configs`, `disallow_untyped_defs`, `check_untyped_defs`, `warn_return_any`, `no_implicit_optional` 등 |
| `ignore_missing_imports = True` | 외부 라이브러리의 타입 힌트가 없을 경우, 에러를 무시합니다. 예: `requests` 같은 패키지에 타입 힌트가 없을 때 mypy 경고를 피할 수 있습니다.                                                   |

---

## ⚙️ `ruff.toml` 설정 설명

```toml
# ruff.toml
line-length = 120
target-version = "py312"

[lint]
select = ["E", "F", "B", "I", "UP"]
ignore = []

[format]
quote-style = "double"
```

| 항목                       | 설명                                                        |
| -------------------------- | ----------------------------------------------------------- |
| `line-length = 120`        | 한 줄 최대 길이를 120자로 설정합니다 (기본은 88자).         |
| `target-version = "py312"` | Python 3.12 버전에 맞춰 lint 및 format 동작을 최적화합니다. |

### `[lint]` 블록

| 항목     | 설명                                                                                                                                                                                                                                                                          |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `select` | 활성화할 린트 규칙을 지정합니다:<br> - `E`: PEP8 스타일 오류<br> - `F`: Pyflakes 오류 (예: 정의되지 않은 변수)<br> - `B`: flake8-bugbear (잠재적 버그 패턴)<br> - `I`: import 순서 정리 (isort)<br> - `UP`: 업그레이드 관련 (예: `isinstance(x, dict)` → `dict` 타입 명시 등) |
| `ignore` | 무시할 린트 코드 목록. 현재는 빈 리스트로 모든 선택한 코드가 적용됩니다.                                                                                                                                                                                                      |

### `[format]` 블록

| 항목                     | 설명                                                                       |
| ------------------------ | -------------------------------------------------------------------------- |
| `quote-style = "double"` | 문자열에 사용할 따옴표를 `"double"`로 강제 지정합니다. (`'single'`도 가능) |
