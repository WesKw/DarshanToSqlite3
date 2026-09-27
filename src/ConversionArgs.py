from dataclasses import dataclass


@dataclass
class ConversionArgs:
    """Generic conversion options"""
    log_file_directory: str = None # The directory containing all log files for conversion.
    module_types: str = "all" # The module types to convert to a database. all -> Convert every module | std -> Convert non-dxt modules | dxt -> Convert DXT modules
    existing_db: str = None # An optional path to an existing sqlite db file.
    