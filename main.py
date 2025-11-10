# Typer package tutorial

import typer


def main(username: str):
    """
    Say hello to user, using command-line parameter 'name'
    :param username: str
    :return: None
    """
    print(f"Hello, {username}!")


if __name__ == '__main__':
    typer.run(main)
