import simple_parsing
import pandas as pd

from dataclasses import dataclass
from abc import abstractmethod,ABC


@ABC
class ExtraConversionaArgs:
    @abstractmethod
    def apply_extra_args(self, pd.DataFrame) -> pd.DataFrame:
        ...


@dataclass
class AthenaConversionArgs(ExtraConversionaArgs):
    """Athena-specific conversion options"""
    runargs_directory: str = "" # the directory containing a runargs.*.py file.