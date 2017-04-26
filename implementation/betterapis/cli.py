import click
import logging
from betterapis.app import api, db


@click.group()
@click.option('-l', '--log-level', default='DEBUG', type=click.Choice(
    ['DEBUG', 'INFO', 'WARN', 'ERROR']))
def betterapis_cli(log_level):
    level = getattr(logging, log_level)
    logging.basicConfig(level=level)

@betterapis_cli.command()
@click.option('-p', '--port', default=8080, type=click.IntRange(1,65535))
@click.option('--debug/--no-debug', default=True)
def run(port, debug):
    api.run(port=port, debug=debug)
    click.echo('Goodbye!')

@betterapis_cli.command(name='reset-db')
def reset_db():
    click.confirm('This will ERASE the application databsase. Are you sure?',
            abort=True)
    click.echo('Dropping all tables...')
    db.drop_all()
    click.echo('Creating all tables...')
    db.create_all()
    click.echo('Database reset!')

@betterapis_cli.command(name='create-tables')
def create_tables():
    click.echo('Creating all tables...')
    db.create_all()
    click.echo('Tables created.')


