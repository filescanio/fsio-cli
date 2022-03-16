from typing import Dict, List
from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.formatter.features.overview import OverviewFormatter
from filescan_cli.formatter.features.details import DetailsFormatter
from filescan_cli.formatter.features.emulation import EmulationFormatter
from filescan_cli.formatter.features.iocs import IOCFormatter
from filescan_cli.formatter.features.disassembly import DisassemblyFormatter
from filescan_cli.formatter.features.yara import YaraFormatter
from filescan_cli.formatter.features.strings import StringsFormatter
from filescan_cli.formatter.features.files import FilesFormatter
from filescan_cli.formatter.features.osint import OsintFormatter
from filescan_cli.formatter.features.geolocation import GeoFormatter


class ReportFormatter:

    def __init__(self):
        self.formatters: List[BaseFormatter] = [
            OverviewFormatter(),
            DetailsFormatter(),
            EmulationFormatter(),
            IOCFormatter(),
            DisassemblyFormatter(),
            YaraFormatter(),
            StringsFormatter(),
            FilesFormatter(),
            OsintFormatter(),
            GeoFormatter()
        ]


    def format(self, report: Dict) -> str:

        result = ''
        for formatter in self.formatters:
            result += formatter.format(report)

        return result



