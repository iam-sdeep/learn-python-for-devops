import subprocess

def execute_command(command):
    process = subprocess.run(command,
                             shell=True,
                             check=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             ) 
    return process.output.decode()

print(execute_command("docker ps"))