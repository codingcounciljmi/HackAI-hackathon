"""
Bug & Code Storage - Persistence layer for Code Made Easy
"""
import json
import os
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

@dataclass
class BugRecord:
    """Represents a single bug/mistake record."""
    date: str
    language: str
    error_type: str
    mistake: str
    wrong_code: str
    correct_code: str
    explanation: str
    
    def to_dict(self) -> Dict:
        return {
            'date': self.date,
            'language': self.language,
            'error_type': self.error_type,
            'mistake': self.mistake,
            'wrong_code': self.wrong_code,
            'correct_code': self.correct_code,
            'explanation': self.explanation
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BugRecord':
        return cls(
            date=data.get('date', ''),
            language=data.get('language', ''),
            error_type=data.get('error_type', ''),
            mistake=data.get('mistake', ''),
            wrong_code=data.get('wrong_code', ''),
            correct_code=data.get('correct_code', ''),
            explanation=data.get('explanation', '')
        )
    
    def display(self) -> str:
        return f"""
┌─────────────────────────────────────────────────────────────────┐
│ 📅 Date: {self.date:<54}│
│ 💻 Language: {self.language:<51}│
│ ⚠️ Error Type: {self.error_type:<49}│
├─────────────────────────────────────────────────────────────────┤
│ ❌ Mistake: {self.mistake[:52]:<52}│
├─────────────────────────────────────────────────────────────────┤
│ Wrong Code:                                                     │
│ {self.wrong_code[:60]:<62}│
├─────────────────────────────────────────────────────────────────┤
│ Correct Code:                                                   │
│ {self.correct_code[:60]:<62}│
├─────────────────────────────────────────────────────────────────┤
│ 💡 Explanation:                                                 │
│ {self.explanation[:60]:<62}│
└─────────────────────────────────────────────────────────────────┘
"""

@dataclass
class SavedCode:
    """Represents a saved code snippet."""
    date: str
    language: str
    code: str
    description: str
    
    def to_dict(self) -> Dict:
        return {
            'date': self.date,
            'language': self.language,
            'code': self.code,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SavedCode':
        return cls(
            date=data.get('date', ''),
            language=data.get('language', ''),
            code=data.get('code', ''),
            description=data.get('description', '')
        )

class BugStorage:
    """Handles saving and loading bug records."""
    
    def __init__(self, storage_file: str = "bug_history.json"):
        self.storage_file = storage_file
        self.bugs: List[BugRecord] = []
        self._load()
    
    def _load(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.bugs = [BugRecord.from_dict(b) for b in data]
            except (json.JSONDecodeError, KeyError):
                self.bugs = []
    
    def _save(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in self.bugs], f, indent=2)
    
    def add_bug(self, bug: BugRecord):
        self.bugs.append(bug)
        self._save()
    
    def get_all_bugs(self) -> List[BugRecord]:
        return self.bugs

class CodeStorage:
    """Handles saving and loading code snippets."""
    
    def __init__(self, storage_file: str = "saved_codes.json"):
        self.storage_file = storage_file
        self.codes: List[SavedCode] = []
        self._load()
    
    def _load(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.codes = [SavedCode.from_dict(c) for c in data]
            except (json.JSONDecodeError, KeyError):
                self.codes = []

    def _save(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in self.codes], f, indent=2)

    def add_code(self, code: SavedCode):
        self.codes.append(code)
        self._save()

    def get_all_codes(self) -> List[SavedCode]:
        return self.codes
