import subprocess

subprocess.call("random_input.py", shell=True)

print(end='',file = open("right_output.txt", "w"))
#放入正確程式碼
subprocess.call("work_8_test.py", shell=True)


print(end='',file = open("test_output.txt", "w"))
#放入待測程式碼
subprocess.call("8.py", shell=True)

# import subprocess
subprocess.call("verify_test.py", shell=True)