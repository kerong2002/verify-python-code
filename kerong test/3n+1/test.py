import subprocess

subprocess.call("random_input.py", shell=True)

print(end='',file = open("right_output.txt", "w"))
#放入正確程式碼
subprocess.call("answer_code.py", shell=True)


print(end='',file = open("test_output.txt", "w"))
#放入待測程式碼
subprocess.call("active.py", shell=True)

# import subprocess
subprocess.call("verify.py", shell=True)