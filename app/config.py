import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    db_path:str=os.getenv('MEMORY_DB_PATH','memory.db')
    max_results:int=int(os.getenv('MEMORY_MAX_RESULTS','10'))
