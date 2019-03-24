import functools
import traceback
import click
import crayons


def _error(message):
    print(crayons.red(message))


def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            _error(traceback.format_exc(limit=1))
            raise click.Abort()
    return wrapper
