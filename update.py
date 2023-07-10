import subprocess
repo = 'https://github.com/kusholino/checkmk-trial-reset'
repo_dir = '/root/checkmk-trial-reset'

def update():
    subprocess.run(["git", "clone", repo, repo_dir], check=True)
    subprocess.run(["git", "-C", repo_dir, "fetch"], check=True)
    subprocess.run(["git", "-C", repo_dir, "merge", "origin/master"], check=True)
    