import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def generate_theme_documentation(templates_dir: str, output_file: str, doc_template_path: str) -> None:
    """
    Generate themes documentation using a Jinja template.
    
    Args:
        templates_dir: Path to the directory containing theme files
        output_file: Path to the output file to generate
        doc_template_path: Path to the Jinja template
    """
    # Get all .html files from the directory
    theme_files = [f for f in os.listdir(templates_dir) if f.endswith('.html')]
    
    # Extract theme names (without .html extension)
    themes = sorted([os.path.splitext(f)[0] for f in theme_files])
    
    # Configure Jinja
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(doc_template_path)),
        lstrip_blocks=True,
        trim_blocks=True,
        autoescape=True,
    )
    template = env.get_template(os.path.basename(doc_template_path))
    
    # Generate content using the template
    content = template.render(themes=themes)
    
    # Create output directory if needed
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write content to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    # Default paths, adjust as needed
    templates_dir = "src/mkdocs_asciinema_player/templates/themes"
    doc_template_path = ".taskfiles/scripts/templates/themes.md"
    output_file = "docs/themes.md"
    
    generate_theme_documentation(templates_dir, output_file, doc_template_path)
