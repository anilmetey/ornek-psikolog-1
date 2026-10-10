import os

mark_path = "assets/mark.svg"
with open(mark_path, "r") as f:
    content = f.read()
content = content.replace("#193f36", "#282625")
with open(mark_path, "w") as f:
    f.write(content)

mind_path = "assets/psychology-mind.svg"
with open(mind_path, "r") as f:
    content = f.read()
content = content.replace("#63816b", "#76716a")
with open(mind_path, "w") as f:
    f.write(content)

print("SVG colors fixed.")
