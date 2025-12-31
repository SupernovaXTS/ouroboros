"""Utilities: Data Ingester."""
from __future__ import annotations

import json
import pathlib
from types import SimpleNamespace
from typing import ClassVar

import attrs


@attrs.define
class Ingester:
    """Ingests data from JSON Files."""
    deltargets: ClassVar[list[str]] = ["resource","reference","id"] # we remove those from the dict to prevent issues
    path: str = "src/data/"
    def ingest(self,data: str) -> SimpleNamespace:
        """Docstring for ingest.

        :param self: Description
        :param data: Description
        :type data: str
        :return: Description
        :rtype: SimpleNamespace
        """
        obj = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        return self.removeattr(obj)
    def removeattr(self,obj: SimpleNamespace) -> SimpleNamespace:
        """Remove unwanted attributes."""
        for ban in self.deltargets:
            obj.delattr(ban)
        return obj
    def formatstring(self,string:str) -> str:
        """Taking a string: Removes whitespace and lowers it for keys."""
        string = string.lower()
        return string.replace(" ","")

    def ingestfile(self,filename:str) -> SimpleNamespace | None:
        """Taking a filename ending in json, extract the data."""
        path = self.path + filename
        path = pathlib.Path(path)
        if not path.exists():
            raise FileNotFoundError
        if path.is_dir():
            raise IsADirectoryError
        container = SimpleNamespace()
        with path.open(encoding="utf8") as f:
            stage1 = json.load(f)
        if not isinstance(stage1,list):
            raise TypeError
        for i in stage1:
            isn = SimpleNamespace(**i)
            key = self.formatstring(isn.name)
            setattr(container,key,isn)
        return container
