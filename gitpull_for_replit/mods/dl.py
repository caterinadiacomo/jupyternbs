import os
import subprocess

repo = "https://github.com/the-intern/cc22-3-replit-jupyterbooks.git"


def clone_repo(repo):
    '''takes in repo and clones it into current working directory; returns repo's directory name'''
    subprocess.run(["git", "clone", repo], shell=False)
    return repo.split('/')[4][0:-4]


def notebooks_exist():
    if 'notebooks' in os.listdir():
        return True
    return False


def create_notebooks_dir():
    os.system('mkdir notebooks')


def copy_nb_content(repo):
    '''
    [1] copy the notebooks and resources of repo
    [2] store in a directory named 'notebooks'
    '''
    if not notebooks_exist():
        create_notebooks_dir()
        os.system(f"mv {repo}/src/* notebooks/")
    else:
        current_content = os.listdir('notebooks')
        for file in os.listdir(repo + "/src"):
            if file not in current_content:
                os.system(f"mv {repo}/src/{file} notebooks")


def remove_repo(folder):
    os.system(f'rm -rf {folder}')


def launch():
    os.system(
        "jupyter lab --LabApp.default_url=/lab/tree/notebooks/ --ip='*' -NotebookApp.token='' --NotebookApp.password=''"
    )


def main():
    '''clone and launch jlab'''
    folder = clone_repo(repo)
    copy_nb_content(folder)
    remove_repo(folder)
    launch()


if __name__ == '__main__': main()
