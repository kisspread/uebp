# MkDocs BlueprintUE Plugin

A MkDocs plugin that renders Unreal Engine Blueprint nodes in your documentation. Based on the excellent [blueprintue-self-hosted-edition](https://github.com/blueprintue/blueprintue-self-hosted-edition) project.

## Features

- Render Unreal Engine Blueprint nodes in your MkDocs documentation
- Support both local blueprint text and blueprintue.com links
- Interactive node visualization with pan and zoom
- Node connection visualization
- Copy button for blueprint text

## Installation

Install the package with pip:

```bash
pip install mkdocs-blueprintue
```

## Usage

The plugin supports three ways to include blueprints in your markdown:

### 1. Inline Blueprint Text
```markdown
![uebp]{{{
Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_0"
   FunctionReference=(MemberName="PrintString",bSelfContext=True)
   NodePosX=0
   NodePosY=0
   NodeGuid=A0000000000000000000000000000000
End Object
}}}
```

### 2. Code Block (Recommended)
This format supports editor code folding and syntax highlighting:

````markdown
```uebp
Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_0"
   FunctionReference=(MemberName="PrintString",bSelfContext=True)
   NodePosX=0
   NodePosY=0
   NodeGuid=A0000000000000000000000000000000
End Object
```
````

### 3. Blueprintue.com Links
```markdown
![uebp]{{{https://blueprintue.com/render/your-blueprint-id/}}}
```

For example:
```markdown
![uebp]{{{https://blueprintue.com/render/50aau0g_/}}}
```

## Configuration

You can configure the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - blueprintue:
        css_path: 'custom/css/path'  # Optional: custom path to CSS files
        js_path: 'custom/js/path'    # Optional: custom path to JavaScript files
```

## Changelog

### 0.1.2 (2024-12-25)
- Fixed rendering issues in markdown list items
- Simplified textarea hiding method
- Fixed HTML escaping issues in JavaScript code

### 0.1.1 (2024-12-25)
- Fixed JavaScript code HTML escaping issues
- Improved code formatting and structure

### 0.1.0 (2024-12-25)
- Initial release
- Support for rendering local blueprint text
- Support for embedding blueprintue.com links
- Added copy-to-clipboard functionality
- Basic documentation and examples

## Project Status

 Core Features
- [x] Local blueprint rendering
- [x] Blueprintue.com embedding
- [x] Copy to clipboard functionality
- [x] Markdown list compatibility
- [x] Basic documentation

 Future Improvements
- [ ] Add support for custom height configuration
- [ ] Add support for dark/light theme switching
- [ ] Add support for custom styling options
- [ ] Improve error handling and user feedback
- [ ] Add more comprehensive documentation and examples

## Known Issues

Currently, there are no known major issues. If you encounter any problems, please [open an issue](https://github.com/ohiyo/mkdocs-blueprintue/issues).

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install -e .[dev]`
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This plugin is based on [blueprintue-self-hosted-edition](https://github.com/blueprintue/blueprintue-self-hosted-edition), a fantastic project that provides the core functionality for rendering Unreal Engine Blueprint nodes. We are grateful to the original authors for their excellent work.

The blueprint rendering functionality has been extracted and adapted from the original project to work as a MkDocs plugin, while maintaining the same high quality and interactive features of the original implementation.
