import os

# Get the `package_name` from the Cookiecutter context
package_name = '{{ cookiecutter.package_name }}'
plugin_category = '{{ cookiecutter.plugin_category }}'
plugin_type = '{{ cookiecutter.plugin_type }}'

# Convert the package name (dot notation) into a directory path
package_dir = os.path.join('src', 'main', 'java', *package_name.split('.'), plugin_category, plugin_type)

# Ensure the directory exists (creates intermediate directories if needed)
os.makedirs(package_dir, exist_ok=True)

print(f"Created package directory structure at: {package_dir}")
