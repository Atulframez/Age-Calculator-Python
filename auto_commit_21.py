import os
import subprocess

file_name = "commit_tracker.txt"

for i in range(21):
    with open(file_name, "a") as f:
        f.write(f"Commit {i} for today\n")
    
    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "-m", "21"])

subprocess.run(["git", "push"])
