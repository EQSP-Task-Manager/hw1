import sys


def main():
    # lcov_path = 'test_project/coverage/lcov.info'
    lcov_path = 'coverage/lcov.info'
    total_lines = 0
    covered_lines = 0

    with open(lcov_path) as f:
        for line in f:
            if (line[0:2] == 'LF'):
                total_lines += int(line[3:])
            if (line[0:2] == 'LH'):
                covered_lines += int(line[3:])

    percentage = round((covered_lines / total_lines) * 100, 2)

    print(f'percentage {percentage}')

    if (percentage < 80):
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
