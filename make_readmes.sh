#!/bin/bash
# Create README.tex files in existing Vigrahaksetra subdirectories

declare -A dirs
dirs=(
  ["phaseIR"]="Schemas of periodicities, invariants, calibration, uncertainty."
  ["operators"]="Resonance functions and operator signatures."
  ["tests"]="Fail-safe glyphs, compiler harness, death protocols."
  ["codex"]="Mythic entries, glyph taxonomies, rites of remembrance."
  ["calibration"]="Energy minimization, semantic continuity protocols."
)

for d in "${!dirs[@]}"; do
  if [ -d "$d" ]; then
    cat > "$d/README.tex" <<EOF
\\section*{$d}
${dirs[$d]}

\\input{../benediction.tex}
EOF
    echo "Created $d/README.tex"
  else
    echo "Directory $d does not exist, skipping."
  fi
done
