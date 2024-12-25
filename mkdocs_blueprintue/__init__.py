"""
MkDocs BlueprintUE plugin package.
"""

import os
import re
import shutil
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import uuid
import html
from markupsafe import Markup

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('mkdocs.plugins.blueprintue')

class BlueprintUEPlugin(BasePlugin):
    """
    MkDocs plugin for rendering Unreal Engine Blueprint nodes.
    """
    
    config_scheme = (
        ('css_path', config_options.Type(str, default=None)),
        ('js_path', config_options.Type(str, default=None)),
    )

    def __init__(self):
        """Initialize the plugin."""
        self.enabled = True
        self._assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        logger.info('BlueprintUE plugin initialized')
        logger.info('Assets directory: %s', self._assets_dir)
    
    def on_config(self, config):
        """Add our custom CSS and JavaScript files to the config."""
        self._copy_assets(config)
        return config
    
    def on_page_markdown(self, markdown, page, config, files):
        """Called when each page's markdown is loaded.

        This method processes the markdown content to render blueprint nodes.
        It handles two types of syntax:
        1. ![uebp]{{{...}}} - For inline blueprint text or URL
        2. ```uebp height="500px" ... ``` - For blueprint code blocks with optional height
        
        The processing is done in this order:
        1. First split the content into code blocks and non-code blocks
        2. For non-code blocks, process inline blueprint syntax
        3. For code blocks, only process those marked as uebp
        """
        logger.info('Processing markdown for page: %s', page.file.src_path)
        
        # First split the content into code blocks and non-code blocks
        parts = []
        last_end = 0
        code_block_pattern = r'```(\w+)(?:\s+height="(\d+(?:px|em|vh)?)")?\n(.*?)```'
        
        # Find all code blocks
        for match in re.finditer(code_block_pattern, markdown, re.DOTALL):
            start, end = match.span()
            if start > last_end:
                # Process the text before this code block
                text_part = markdown[last_end:start]
                # Handle inline blueprints in text
                text_part = self._process_inline_blueprints(text_part)
                parts.append(text_part)
                
            # Handle code blocks
            block_type = match.group(1)
            block_height = match.group(2)
            block_content = match.group(3)
            
            if block_type == 'uebp':
                # Render blueprint code blocks with optional height
                parts.append(self._render_blueprint(block_content.strip(), block_height))
            else:
                # Keep other code blocks as is
                parts.append(match.group(0))
                
            last_end = end
            
        if last_end < len(markdown):
            # Process any remaining text
            text_part = markdown[last_end:]
            text_part = self._process_inline_blueprints(text_part)
            parts.append(text_part)
            
        return ''.join(parts)
    
    def _process_inline_blueprints(self, text):
        """Process inline blueprint syntax in text."""
        def _replace(match):
            return self._render_blueprint(match.group(1).strip())
            
        return re.sub(r'!\[uebp\]\{{{(.*?)}}}', _replace, text, flags=re.DOTALL)
        
    def _render_blueprint(self, text: str, height: str = None) -> str:
        """Render a blueprint to HTML.
        
        Args:
            text: The blueprint text or URL to render
            height: Optional height for the container (e.g. "500px")
            
        Returns:
            HTML output for the blueprint
        """
        # Generate unique IDs for this blueprint
        container_id = f'bue_container_{uuid.uuid4().hex[:8]}'
        blueprint_id = f'bue_data_{uuid.uuid4().hex[:8]}'
        
        # Default height if none specified
        if not height:
            height = "643px"
        elif not any(height.endswith(unit) for unit in ["px", "em", "vh"]):
            height = f"{height}px"
        
        # Check if the text is a URL
        if text.strip().startswith('http'):
            # For URLs, use iframe
            return Markup(f'<div class="bue-render"><iframe src="{text.strip()}" scrolling="no" allowfullscreen style="width: 100%; height: {height}; border: none;"></iframe></div>')
        
        # For blueprint text, use the renderer
        html_output = f'''<div class="bue-render">
            <div class="playground" id="{container_id}"></div>
            <textarea id="{blueprint_id}_data" style="display:none">{text}</textarea>
            <script>
            (function() {{
                function initBlueprintRenderer() {{
                    const textarea = document.getElementById('{blueprint_id}_data');
                    const container = document.getElementById('{container_id}');
                    if (!textarea || !container) return;
                    if (!window.blueprintUE || !window.blueprintUE.render || !window.blueprintUE.render.Main) {{
                        setTimeout(initBlueprintRenderer, 100);
                        return;
                    }}
                    try {{
                        new window.blueprintUE.render.Main(textarea.value, container, {{height:"{height}"}}).start();
                    }} catch(e) {{
                        console.error('Error initializing blueprint renderer:', e);
                    }}
                }};
                if (document.readyState === 'complete') {{
                    initBlueprintRenderer();
                }} else {{
                    window.addEventListener('load', initBlueprintRenderer);
                }}
            }})();
            </script>
        </div>'''
        
        return Markup(html_output)

    def _copy_assets(self, config):
        """Copy the required assets to the docs directory."""
        assets_path = os.path.join(os.path.dirname(__file__), 'assets')
        css_path = os.path.join(assets_path, 'bue-render', 'render.css')
        js_path = os.path.join(assets_path, 'bue-render', 'render.js')
        copy_css_path = os.path.join(assets_path, 'bue-render', 'copy-button.css')
        copy_js_path = os.path.join(assets_path, 'bue-render', 'copy-button.js')

        # Append our CSS and JavaScript files to the config
        # Use forward slashes for web paths
        config['extra_css'] = config.get('extra_css', []) + [
            'assets/bue-render/render.css',
            'assets/bue-render/copy-button.css'
        ]
        config['extra_javascript'] = config.get('extra_javascript', []) + [
            'assets/bue-render/render.js',
            'assets/bue-render/copy-button.js'
        ]

        # Copy the assets to the docs directory
        # Use os.path.join for filesystem paths
        docs_assets_path = os.path.join(config['docs_dir'], 'assets', 'bue-render')
        os.makedirs(docs_assets_path, exist_ok=True)

        shutil.copy2(css_path, os.path.join(docs_assets_path, 'render.css'))
        shutil.copy2(js_path, os.path.join(docs_assets_path, 'render.js'))
        shutil.copy2(copy_css_path, os.path.join(docs_assets_path, 'copy-button.css'))
        shutil.copy2(copy_js_path, os.path.join(docs_assets_path, 'copy-button.js'))
