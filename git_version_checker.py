import subprocess
import sys


def check_git_version():
    try:
        version = subprocess.check_output(['git', '--version']).decode('utf-8').strip()
        return version
    except Exception as e:
        print(f'Fehler beim Überprüfen der Git-Version: {e}')
        sys.exit(1)


def get_commit_history():
    try:
        commits = subprocess.check_output(['git', 'log', '--oneline', '-5']).decode('utf-8').strip().split('\n')
        return commits
    except Exception as e:
        print(f'Fehler beim Abrufen der Kommittierungshistorie: {e}')
        sys.exit(1)


def main():
    print('Aktuelle Git-Version:')
    version = check_git_version()
    print(version)

    print('\nLetzte 5 Kommittierungen:')
    commit_history = get_commit_history()
    for commit in commit_history:
        print(commit)


if __name__ == '__main__':
    main()