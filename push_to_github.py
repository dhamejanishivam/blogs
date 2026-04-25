import subprocess

blog_path = "/Users/shivam/Desktop/blogs"
public_path = f"{blog_path}/public"

subprocess.run(["hugo"], cwd=blog_path, check=True)

subprocess.run(["git", "add", "."], cwd=public_path, check=True)
subprocess.run(["git", "commit", "-m", "pushed_via_python"], cwd=public_path, check=True)
subprocess.run(["git", "push", "-f"], cwd=public_path, check=True)