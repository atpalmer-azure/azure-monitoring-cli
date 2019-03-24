import functools
import traceback
import click
import crayons
from . import jsontools


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


def handle_result(func):
    @handle_errors
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(jsontools.dumps(result))
    return wrapper


def subcommands(commands):
    def decorator(func):
        commands(func)
        return func
    return decorator


def metric_command(group):
    def decorator(func):
        @group.command()
        @click.option('-c', '--count', default=1)
        @click.pass_obj
        @handle_result
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
