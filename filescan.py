import asyncclick as aclick
from filescan_cli.commands.scan import scan
from filescan_cli.commands.report import report
from filescan_cli.commands.reports import reports
from filescan_cli.commands.system import system
from filescan_cli.commands.files import files


@aclick.group(help="CLI tool to access to the filescan service")
def cli():
    pass


cli_groups = aclick.CommandCollection(sources=[scan, report, reports, system, files])
if __name__ == "__main__":
    cli_groups(_anyio_backend="asyncio")  # or asyncio, or curio
