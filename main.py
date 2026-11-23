"""Write one single-line office joke to /output/entry.txt."""

JOKE = "I blocked an hour for focus time, so my boss booked that exact hour for a meeting called 'Quick Sync About Your Focus Time'."


def main():
    import os

    assert "\n" not in JOKE and 1 <= len(JOKE) <= 199 and JOKE.strip(), "joke fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"Joke ({len(JOKE)} characters): {JOKE}")


if __name__ == "__main__":
    main()
