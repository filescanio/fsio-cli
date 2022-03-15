from typing import Dict, List
from .base import BaseFormatter
from .pe_details import PeFormatter
from .elf_details import ElfFormatter
from .lnk_details import LnkFormatter
from .mbox_details import MboxFormatter
from .office_details import OfficeFormatter
from .pdf_details import PdfFormatter
from .default_details import DefaultDetailsFormatter


class DetailsFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()
        self.formatters: List[BaseFormatter] = [
            PeFormatter(),
            ElfFormatter(),
            LnkFormatter(),
            MboxFormatter(),
            OfficeFormatter(),
            PdfFormatter(),
            DefaultDetailsFormatter()
        ]


    def format(self, report: Dict) -> str:
        
        for formatter in self.formatters:
            formatted = formatter.format(report)
            if not formatted:
                continue

            return formatted

        return ''
