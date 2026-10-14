import os
import sys


def main() -> None:
    port = os.environ.get("PORT")
    if port is None:
        raise SystemExit("PORT is required")
    os.execv(
        sys.executable,
        [sys.executable, "-m", "uvicorn", "project.asgi:application", "--host", "0.0.0.0", "--port", str(int(port))],
    )


if __name__ == "__main__":
    main()
