def main():
    import argparse

    parser = argparse.ArgumentParser(description="greeting from timur")
    parser.add_argument("name", help="Your name")

    args = parser.parse_args()

    print(f"{args.name} - hello from Timur")

if __name__ == "__main__":
    main()