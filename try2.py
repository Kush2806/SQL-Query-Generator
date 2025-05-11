# import subprocess

# # Command to execute
# command = "ollama run gemma:2b"

# # Open a subprocess and create a pipe to the stdin
# p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

# # Input you want to provide
# input_text = "hi hello!!"

# # Send input_text to the subprocess
# p.stdin.write(input_text)
# p.stdin.flush()

# # Close the stdin
# p.stdin.close()

# # Read and print the output
# for line in p.stdout:
#     print(line)

# # Close the process
# p.kill()

# import subprocess

# # To run a single command with no arguments
# subprocess.run(["ollama run gemma:2b"])

# # To run a command with multiple arguments
# # subprocess.run(["dir", "-l"])

# # If you want to capture the output
# # result = subprocess.run(["Hi"], capture_output=True, text=True)
# # print(result.stdout)

import subprocess

# To run a single command with no arguments
subprocess.run(["powershell", "-Command", "ollama run gemma:2b"])

# To run a command with multiple arguments
subprocess.run(["powershell", "-Command", "Hello gemaa"])

# If you want to capture the output
result = subprocess.run(["powershell", "-Command", "Get-Process"], capture_output=True, text=True)
print(result.stdout)

import subprocess

def run_gemma(user_input):
    # Command to execute
    command = f"ollama run gemma:2b {user_input}"

    # Open a subprocess
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    print(p)
    # Send user input to the subprocess
    p.stdin.write(user_input + "\n")
    # p.stdin.flush()

    # Read the output
    ans = p.stdout.readline().strip()
    print(ans)
    # Close the process
    p.kill()

    return ans

# Get user input
user_input = input("Enter your question: ")

# Call run_gemma function
ans = run_gemma(user_input)

# Print the answer
print("Answer:", ans)

# prompt='apple'


# def run_gemma(user_input):
#     # Command to execute
#     # r=subprocess.run(["ollama" ,"run" ,f"gemma:2b {user_input}"],capture_output=True, text=True)
#     # Open a subprocess
#     command = f"ollama run gemma:2b {user_input}"
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    
    
#     # process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

#     # Capture the output
#     output, _ = process.communicate()
#     # p.stdin.flush()
#     output_str = output.decode('utf-8')
#     # Read the output
#     # ans = p.stdout.readline().strip()
#     # print(ans)
#     # Close the process
#     # p.kill()

#     return output_str

# print(run_gemma(prompt))


# import subprocess

# def run_command(command):
#     try:
#         result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return e.output

# # Example usage:
# command_input = input("Enter a command: ")
# output = run_command(command_input)
# print("Output:")
# print(output)