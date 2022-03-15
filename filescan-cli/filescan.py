import asyncclick as aclick
from commands.scan import scan
from commands.report import report
from commands.reports import reports
from commands.system import system
from commands.files import files


@aclick.group(help="CLI tool to access to the filescan service")
def cli():
    pass


cli_groups = aclick.CommandCollection(sources=[scan, report, reports, system, files])
if __name__ == "__main__":
    cli_groups(_anyio_backend="asyncio")  # or asyncio, or curio
