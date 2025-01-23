from dataclasses import dataclass
from typing import List

@dataclass
class Dice:
    values: List[int] 
    def __str__(self):
        
        return ','.join(map(str, self.values))
    
    def __getitem__(self, index: int) -> int:
       
        return self.values[index]

