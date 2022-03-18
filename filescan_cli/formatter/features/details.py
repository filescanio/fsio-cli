from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.formatter.features.pe_details import PeFormatter
from filescan_cli.formatter.features.elf_details import ElfFormatter
from filescan_cli.formatter.features.lnk_details import LnkFormatter
from filescan_cli.formatter.features.mbox_details import MboxFormatter
from filescan_cli.formatter.features.office_details import OfficeFormatter
from filescan_cli.formatter.features.pdf_details import PdfFormatter
from filescan_cli.formatter.features.default_details import DefaultDetailsFormatter


class DetailsFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()
        self.formatters = [
            PeFormatter(),
            ElfFormatter(),
            LnkFormatter(),
            MboxFormatter(),
            OfficeFormatter(),
            PdfFormatter(),
            DefaultDetailsFormatter()
        ]


    def format(self, report):
        
        for formatter in self.formatters:
            formatted = formatter.format(report)
            if not formatted:
                continue

            return formatted

        return ''
