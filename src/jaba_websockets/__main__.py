"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Jaba Websockets."""


if __name__ == "__main__":
    main(prog_name="jaba-websockets")  # pragma: no cover
