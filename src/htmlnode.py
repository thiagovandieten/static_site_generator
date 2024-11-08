from typing import Any

class HTMLNode:

    def __init__(
        self,
        value: str | None = None,
        tag: str | None = None,
        children: list[Any] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            raise NotImplementedError
        
        return True if vars(self) == vars(other) else False

    def __repr__(self) -> str:
        return (
            f"HTMLNode data:\n"
            f"value: {self.value}\n"
            f"tag: {self.tag}\n"
            f"children: {self.children}\n"
            f"props: {self.props}"
        )

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            raise ValueError("Props is empty")
        list_string = list(map(lambda x: f'{x[0]}="{x[1]}"', self.props.items()))
        return " ".join(list_string)

    def props_to_string(self) -> str:
        if self.props is None:
            raise ValueError("Props is empty")
        props_string = ""
        for i in self.props:
            props_string += f'{i}="{self.props[i]}" '
        return props_string.rstrip()
    
