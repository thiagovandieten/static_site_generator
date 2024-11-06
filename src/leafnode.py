from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str,
        tag: str | None = None,
        props: dict[str, str] | None = None      
    ):
        super().__init__(value, tag, None, props)

    def to_html(self) -> str:
        if not self.value: raise ValueError("Value empty or not defined")
        if not self.tag: return self.value

        return f"<{self.tag}{" " + self.props_to_string() if self.props else ""}>{self.value}</{self.tag}>"
    
    def props_to_string(self) -> str:
        return super().props_to_string()