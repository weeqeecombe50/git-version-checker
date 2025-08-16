import subprocess
import sys


def check_git_version():
    """
    Überprüft die installierte Git-Version.
    Gibt die Version zurück oder beendet das Programm bei einem Fehler.
    """
    try:
        version = subprocess.check_output(['git', '--version']).decode('utf-8').strip()
        return version
    except Exception as e:
        print(f'Fehler beim Überprüfen der Git-Version: {e}')
        sys.exit(1)


def get_commit_history():
    """
    Ruft die letzten 5 Commits aus der Git-Historie ab.
    Gibt eine Liste von Commit-Nachrichten zurück oder beendet das Programm bei einem Fehler.
    """
    try:
        commits = subprocess.check_output(['git', 'log', '--oneline', '-5']).decode('utf-8').strip().split('\n')
        return commits
    except Exception as e:
        print(f'Fehler beim Abrufen der Kommittierungshistorie: {e}')
        sys.exit(1)


def main():
    """
    Hauptfunktion zur Anzeige der Git-Version und der letzten Commits.
    """
    print('Aktuelle Git-Version:')
    version = check_git_version()
    print(version)

    print('\nLetzte 5 Kommittierungen:')
    commit_history = get_commit_history()
    for commit in commit_history:
        print(commit)


if __name__ == '__main__':
    main()