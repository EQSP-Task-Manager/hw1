import sys


def main():
    lcov_path = 'coverage/lcov.info'
    total_lines = 0
    covered_lines = 0

    with open(lcov_path) as f:
        for line in f:
            if (line[0:2] == 'LF'):
                total_lines += int(line[3:])
            if (line[0:2] == 'HF'):
                covered_lines += int(line[3:])

    percentage = round((covered_lines / total_lines), 2)

    print(f"::set-output name=percentage::{percentage}")

    sys.exit(0)


if __name__ == "__main__":
    main()
