from itertools import product
from subprocess import check_output

PASSWORD_DEFS = {"n": -13, "s": 13, "w": -1, "e": 1}  # north, south, west, east. a line is 13 chars and this is a map
MAP = "##############     #     ## ### # ### ##   # # #$# #### # # # # ##   #   # # ## ####### # ##  #      # ### # ###### ##  #  #  @# ## ### # ### ##     #     ##############"

MAX_LENGTH = 0x169

AT_SIGN_POS = 126
DOLLAR_SIGN_POS = 48

HASHTAG = '#'
WHITESPACE = ' '
DOLLAR_SIGN = '$'

HASHTAG_CODE = 888
DOLLAR_SIGN_CODE = 999
NO_RESULT_CODE = 1111
OUT_OF_BOUND_CODE = 2222


def check_password(possible_password):
    # Add that to identical e.g: sn, we, ew etc are false
    key_ind = AT_SIGN_POS
    for _letter in possible_password:
        if key_ind < 0 or key_ind > len(MAP):
            return OUT_OF_BOUND_CODE

        key_ind += PASSWORD_DEFS[_letter]
        if MAP[key_ind] == DOLLAR_SIGN:
            return DOLLAR_SIGN_CODE
        if MAP[key_ind] == HASHTAG:
            return HASHTAG_CODE

    return NO_RESULT_CODE


def main():
    rotten_combos = []

    for i in range(1, MAX_LENGTH):
        print(f"Moved to {i}")
        for permutation in product(PASSWORD_DEFS.keys(), repeat=i):
            password = ''.join(permutation)

            if any(password.startswith(rotten_combo) for rotten_combo in rotten_combos):
                continue

            print(f"Length: {i}, Trying: {password}")
            _password_res = check_password(password)

            if _password_res == DOLLAR_SIGN_CODE:
                print(f"Password is: {password}")
                with open("correct_password.txt", "w") as result:
                    result.write(password)
                return

            if _password_res == NO_RESULT_CODE:
                continue

            rotten_combos.append(password)

    print("No password")


if __name__ == "__main__":
    main()


'''
# 48 - 48+13=61, 74, 87, 100, 95 (by Ws), 108, 121

# 126 - 124 - 137 - 150

# we need to go to 61 excatly
#in conclusion: wwsseeeennnnnnnnnn!!!!! this goes to 24

#failed attempt for generic solution
KEY = "##############     #     ## ### # ### ##   # # #$# #### # # # # ##   #   # # ## ####### # ##  #      # ### # ###### ##  #  #  @# ## ### # ### ##     #     ##############"
PASSWORD_DEFS = {"n": -13, "s": 13, "w": -1, "e": 1}
DEF_SHIFT = 0

AT_SIGN_POS = 126
DOLLAR_SIGN_POS = 48

HASHTAG = '#'
WHITESPACE = ' '
DOLLAR_SIGN = '$'

STARTING_PASSWORD = ""

possible_passwords = []


def rec_solve(possible_password, key_ind):
    if key_ind >= len(KEY):
        return False

    for _letter, _factor in PASSWORD_DEFS.items():
        if 0 <= key_ind + _factor < len(KEY) and KEY[key_ind + _factor] != HASHTAG and \
         (len(possible_password) <= 0 or abs(PASSWORD_DEFS[_letter]) != abs(PASSWORD_DEFS[possible_password[-1]])):
            key_ind += _factor
            possible_password += _letter

            if KEY[key_ind] == DOLLAR_SIGN:
                possible_passwords.append(possible_password)
                return True

            if KEY[key_ind] == HASHTAG:
                return False

            rec_solve(possible_password, key_ind)


start_pos = AT_SIGN_POS
rec_solve(STARTING_PASSWORD, start_pos)
print(possible_passwords)
'''