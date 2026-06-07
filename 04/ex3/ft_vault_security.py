def secure_archieve(file_name: str, readf: bool) -> tuple[bool, str]:
    open_file_state: bool = False
    phrase: str = "I wish to write this here."
    try:
        if readf:
            with open(file_name, "r") as file:
                phrase = file.read()
        else:
            with open(file_name, "w") as file:
                file.write(phrase)
    except (FileNotFoundError, PermissionError) as error:
        function_tuple: tuple = (open_file_state, error)
        return function_tuple
    open_file_state = True
    function_tuple = (open_file_state, phrase)
    return function_tuple


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archieve' to read from a nonexistent file:")
    tuple1: tuple = (secure_archieve("not/existing/file", True))
    print(tuple1, "\n")
    print("Using 'secure_archieve' to read from an inaccessible file:")
    tuple2: tuple = (secure_archieve("master.passwd", True))
    print(tuple2, "\n")
    print("Using 'secure_archieve' to read from a regular file:")
    tuple3: tuple = (secure_archieve("test_read.txt", True))
    print(tuple3, "\n")
    print("Using 'secure_archieve' to write from a nonexistent file:")
    tuple4: tuple = (secure_archieve("test_write.txt", False))
    print(tuple4, "\n")


if __name__ == "__main__":
    main()
