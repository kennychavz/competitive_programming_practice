import random
import numpy as np

def manual_shuffle(lst):

    # we can loop this as many times as we want but the higher
    # the better
    for _ in range(10000):

        # we make a numpy array containing the index of the list
        new_lst = np.arange(0, len(lst), 1)

        # we random 2 choices of index between the list
        choice_1 = np.random.choice(new_lst)
        choice_2 = np.random.choice(new_lst)

        # we save the temp variable 2 pertaining to the index choose by choice
        temp_value_1 = lst[choice_1]
        temp_value_2 = lst[choice_2]

        # we replace the original list indexes with these temp values
        lst[choice_1] =  temp_value_2
        lst[choice_2] = temp_value_1

    return lst




# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing your Shuffle's length:")
if len(manual_shuffle(list(range(20)))) == 20:
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's randomness:")
if manual_shuffle(list(range(100))) != manual_shuffle(list(range(100))):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Shuffle's content vs. the original:")
if set(manual_shuffle(list(range(100)))) == set(range(100)):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's destructiveness:")
test_list = list(range(10))
manual_shuffle(test_list)
if len(test_list) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's helper methods")
import dis
def list_method_calls(fn):
    methods = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for ix, instr in enumerate(instrs):
        if instr.opname=="CALL_METHOD":
            load_method_instr = instrs[ix + instr.arg + 1]
            methods.append(load_method_instr.argval)
    return methods

if "shuffle" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

if "sort" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    




    