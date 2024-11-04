from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str,
        tag: str | None = None,
        children: None = None,
        props: dict[str, str] | None = None      
    ):
        super().__init__(value, tag, None, props)

    def to_html(self) -> str:
        if not self.value: raise ValueError("Value empty or not defined")
        if not self.tag: return self.value

        #TODO: Need to include all the props in this string. Might want to build a props to string in HTMLNode
        return f"<{self.tag}>{self.value}</{self.tag}>"