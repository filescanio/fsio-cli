from typing import Dict, List
from .features.base import BaseFormatter
from .features.overview import OverviewFormatter
from .features.details import DetailsFormatter
from .features.emulation import EmulationFormatter
from .features.iocs import IOCFormatter
from .features.disassembly import DisassemblyFormatter
from .features.yara import YaraFormatter
from .features.strings import StringsFormatter
from .features.files import FilesFormatter
from .features.osint import OsintFormatter
from .features.geolocation import GeoFormatter


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



