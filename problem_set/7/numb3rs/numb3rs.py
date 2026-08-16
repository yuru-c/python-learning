import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # if re.search(r"^(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))$", ip, re.IGNORECASE):
    #     return "True"
    # else:
    #     return "False"

    parts = ip.split(".")

    if len(parts) != 4:
        return "False"

    for part in parts:
        if not part.isdigit():
            return "False"

        if not 0 <= int(part) <= 255:
            return "False"

        if len(part) > 1 and part[0] == "0":

    return "True"



if __name__ == "__main__":
    main()