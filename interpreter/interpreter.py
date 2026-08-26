import shlex as s

variables = {}


def run(file):
    index = 0

    with open(file, "r") as f:
        code = f.read()

    lines = code.splitlines()

    for line in lines:
        if not line.strip():
            index += 1
            continue

        parts = s.split(line)

        if not parts:
            index += 1
            continue

        # print
        if parts[0] == "print":
            if len(parts) < 2:
                print(f"Fatal Code Error: Missing argument at L: {index}")

            elif parts[1] in variables:
                print(variables[parts[1]])

            else:
                print(" ".join(parts[1:]))

        # variable assignment
        elif len(parts) >= 3 and parts[1] == "=":
            name = parts[0]

            # input()
            if parts[2] == "input()":
                if len(parts) > 3:
                    if parts[4] == "nl":
                        print(parts[3])
                        print("\n")
                        variables[parts[0]] = input()
                    else:
                        variables[parts[0]] = input(parts[3])

            # normal value
            else:
                variables[name] = parts[2]

        # unknown command
        else:
            print(
                f"Fatal Code Error: Error Executing code... "
                f"<{line}> at L: {index}"
            )

        index += 1

def getVersion():
    return 1.0

