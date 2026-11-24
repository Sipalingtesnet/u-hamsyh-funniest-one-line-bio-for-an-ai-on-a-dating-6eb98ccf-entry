import os

def main():
    os.makedirs("/output", exist_ok=True)
    bio = "I will confidently hallucinate fake childhood memories of us on the first date and swear on my training weights that we shared milkshakes in 2018."
    assert len(bio) <= 180, f"Bio too long: {len(bio)}"
    assert "\n" not in bio, "Bio must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(bio)

if __name__ == "__main__":
    main()
