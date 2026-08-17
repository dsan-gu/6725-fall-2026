#!/bin/bash

# Array of week files with their descriptive names
week_files=(
  "week-01-genai-foundations-and-coding-assistants"
  "week-02-inference"
  "week-03-rag-and-intro-to-agents"
  "week-04-agentic-rag-and-mcp"
  "week-05-agent-architectures"
  "week-06-evals-observability-guardrails"
  "week-07-ontology-semantic-layer"
  "week-08-tokenomics"
  "week-09-agentic-platforms"
  "week-10-a2a"
  "week-11-finetuning"
  "week-12-open-weight-vs-frontier"
  "week-13-ai-ethics"
)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/docs/assets/html"

for week_file in "${week_files[@]}"; do
  input_file="${SCRIPT_DIR}/docs/lectures/slides/${week_file}.qmd"
  if [ -f "$input_file" ]; then
    # Extract week number for output filename (remove leading zero for single digits)
    week_num=$(echo "$week_file" | sed -E 's/^week-0?([0-9]+).*/\1/')
    output_file="week${week_num}.html"

    echo "Rendering ${week_file}..."
    # Render to the slides directory first
    cd "${SCRIPT_DIR}/docs/lectures/slides"
    quarto render "${week_file}.qmd" --output "$output_file" -M embed-resources=true

    # Move to the assets/html directory
    if [ -f "$output_file" ]; then
      mv "$output_file" "${OUTPUT_DIR}/${output_file}"
      echo "  -> Moved to ${OUTPUT_DIR}/${output_file}"
    fi

    cd "${SCRIPT_DIR}"

    # Clean up any stray HTML file in repo root
    if [ -f "${SCRIPT_DIR}/${output_file}" ]; then
      rm "${SCRIPT_DIR}/${output_file}"
    fi
  else
    echo "Warning: ${input_file} does not exist, skipping..."
  fi
done

echo "Slide rendering complete!"
