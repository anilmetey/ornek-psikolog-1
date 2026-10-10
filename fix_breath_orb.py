with open("style.css", "r") as f:
    css = f.read()

# Replace breath-orb colors
css = css.replace("#cfb88f", "#D2B48C") # Light brown/tan
css = css.replace("#9c835b", "#8B7355") # Warm brown
css = css.replace("#6c6945", "#5C4033") # Dark brown instead of olive

with open("style.css", "w") as f:
    f.write(css)

