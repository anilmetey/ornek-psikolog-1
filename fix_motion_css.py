import re

with open("motion.css", "r") as f:
    css = f.read()

# Replacements
replacements = {
    "#193f36": "#282625",
    "#315745": "#322a24",
    "#315b48": "#322a24",
    "#345d47": "#322a24",
    "#376450": "#322a24",
    "#456f57": "#4f4035",  # Handle with transparency suffix implicitly if it matches
    "#68705a": "#76716a",
    "#afc9b7": "#dcd1c6",
    "#b2cbb7": "#dfd4c9",
    "#c8dbc2": "#e6dbcd",
    "#d1dfc5": "#e8e1d7",
    "#e8eee2": "#f5f0eb",
    "#e9eee5": "#f5f0eb",
    "#eceee6": "#f7f2ed",
    "#edf1e9": "#f8f4f0",
    "#f1ebe2": "#f9f6f2"
}

for old, new in replacements.items():
    css = css.replace(old, new)
    css = css.replace(old.upper(), new.upper())

with open("motion.css", "w") as f:
    f.write(css)

print("motion.css fixed.")
