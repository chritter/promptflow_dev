from jinja2 import Environment, FileSystemLoader


from pathlib import Path

# Get the current file path
parent_dir = Path(__file__).parent.resolve()

# Set up the Jinja2 environment
file_loader = FileSystemLoader(parent_dir)
env = Environment(loader=file_loader)

# Load the template file
template = env.get_template('classify_with_llm.jinja2')

# Render the template with a variable

examples = [
    {
        "url": "http://example.com/1",
        "text_content": "Example text content 1",
        "category": "news",
        "evidence": "Evidence text 1"
    },
    {
        "url": "http://example.com/2",
        "text_content": "Example text content 2",
        "category": "blog",
        "evidence": "Evidence text 2"
    }
]

data = {
    "url": "http://example.com/new",
    "text_content": "New example text content"
}

rendered = template.render(examples=examples, **data)
print(rendered)  # Outputs: Hello, World!