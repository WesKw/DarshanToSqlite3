from dataclasses import dataclass

@dataclass
class LogMetadata():
    pid: int # the process id of the log
    is_parent: bool # if the process id and parent ids are the same, this is set to true
    start_time: float
    end_time: float
    