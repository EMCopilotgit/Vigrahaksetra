import os

# Path to the repo root and template
repo_root = r"C:/Users/Meisner/Vigrahaksetra"
template_path = os.path.join(repo_root, "Codex_template.tex")

# Domain mapping
domains = {
    "elliptic": "Elliptic",
    "fractal": "Fractal",
    "spectral": "Spectral",
    "thermo": "Thermodynamic",
    "pAdic": "p-Adic",
}

# Load the template once
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# Fill each domain Codex
for folder, name in domains.items():
    domain_dir = os.path.join(repo_root, "PhaseIR", folder)
    os.makedirs(domain_dir, exist_ok=True)

    output_path = os.path.join(domain_dir, "Codex.tex")
    content = template.replace("[Domain Name]", name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created {output_path}")
