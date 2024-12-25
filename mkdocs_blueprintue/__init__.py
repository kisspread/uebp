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
        ('css_path', config_options.Type(str, default='bue-render/render.css')),
        ('js_path', config_options.Type(str, default='bue-render/render.js')),
    )

    def __init__(self):
        """Initialize the plugin."""
        self.enabled = True
        self._assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        logger.info('BlueprintUE plugin initialized')
        logger.info('Assets directory: %s', self._assets_dir)
    
    def on_config(self, config):
        """Add our custom CSS and JavaScript files to the config."""
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

        return config
    
    def on_page_markdown(self, markdown, page, config, files):
        """
        Convert blueprint code blocks to HTML.
        
        Args:
            markdown: Input markdown content
            page: Current page object
            config: Global configuration object
            files: Object containing all project files
            
        Returns:
            Modified markdown content
        """
        logger.info('Processing markdown for page: %s', page.file.src_path)
        
        # Split the markdown into code blocks and non-code blocks
        parts = []
        last_end = 0
        code_block_pattern = r'```.*?```'
        for match in re.finditer(code_block_pattern, markdown, re.DOTALL):
            start, end = match.span()
            if start > last_end:
                # Add non-code block
                parts.append(('text', markdown[last_end:start]))
            # Add code block
            parts.append(('code', match.group(0)))
            last_end = end
        if last_end < len(markdown):
            parts.append(('text', markdown[last_end:]))

        # Process only non-code blocks
        result = ''
        blueprint_pattern = r'!\[uebp\]\{{{(.*?)}}}' 
        for part_type, content in parts:
            if part_type == 'text':
                # Replace blueprints in non-code blocks
                for match in re.finditer(blueprint_pattern, content, re.DOTALL):
                    blueprint_text = match.group(1).strip()
                    html_output = self._render_blueprint(blueprint_text)
                    content = content.replace(match.group(0), html_output)
            result += content
        
        return result
    
    def _render_blueprint(self, text: str) -> str:
        """Render a blueprint to HTML."""
        # Check if the text is a blueprintue.com URL
        if text.strip().startswith('https://blueprintue.com/render/'):
            return Markup(f'<div class="bue-render"><iframe src="{text.strip()}" scrolling="no" allowfullscreen style="width: 100%; height: 643px; border: none;"></iframe></div>')

        # Create a unique ID for this blueprint
        blueprint_id = f"blueprint_{uuid.uuid4().hex}"
        container_id = f"container_{blueprint_id}"
        
        # Create the HTML output without extra indentation
        html_output = f'<div class="bue-render"><div class="playground" id="{container_id}"></div><textarea id="{blueprint_id}_data" style="display:none">{html.escape(text)}</textarea><script>(function(){{function initBlueprintRenderer(){{const textarea=document.getElementById(\'{blueprint_id}_data\');const container=document.getElementById(\'{container_id}\');if(!textarea||!container)return;if(!window.blueprintUE||!window.blueprintUE.render||!window.blueprintUE.render.Main){{setTimeout(initBlueprintRenderer,100);return;}}try{{new window.blueprintUE.render.Main(textarea.value,container,{{height:"643px"}}).start();}}catch(e){{console.error(\'Error initializing blueprint renderer:\',e);}}}};if(document.readyState===\'complete\'){{initBlueprintRenderer();}}else{{window.addEventListener(\'load\',initBlueprintRenderer);}}}})();</script></div>'
        
        return Markup(html_output)
