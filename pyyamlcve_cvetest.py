import yaml

# Example YAML content
yaml_content = """
name: John Doe
age: 30
address:
  street: 123 Main St
  city: Anytown
  state: CA
  zip: 12345
"""

# Load the YAML content
data = yaml.load(yaml_content,Loader=yaml.Loader)

# Print the loaded data
print(data)
