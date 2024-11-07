import sys
from functools import reduce

if sys.version_info >= (3,12):
    from typing import override
else:
    from typing_extensions import override

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    @override
    def __init__(self, tag: str, children: list[str | HTMLNode] | None, props: dict[str, str] | None = None):
        super().__init__(None, tag, children, props)
        self.children = children

    def to_html(self) -> str:
        if not self.tag: raise ValueError("Tag not found") 
        if not self.children: raise ValueError("Children not found")
        
        children_html = reduce(lambda acc, child: acc + (child.to_html() if isinstance(child, HTMLNode) else child), self.children, "")
        return f"<{self.tag}>{children_html}</{self.tag}>"