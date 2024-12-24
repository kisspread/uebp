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

Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
    - search
    - blueprintue
```

### Local Blueprint Text

Use the following syntax to render blueprint nodes from text:

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

### BlueprintUE.com Links

You can also embed blueprints from blueprintue.com using their share links:

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
