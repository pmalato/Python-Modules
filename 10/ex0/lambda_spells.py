artifact = lambda x, y, z: {"dict": x, "power": y, "type": z}
artifact_sorter = lambda a: sorted(artifact["power"])


def main() -> None:
    print("\nTesting artifact sorter...")
    # artifact_sorter = lambda a
    print(artifact("gloss", 95, "fire"))


if __name__ == "__main__":
    main()
