"""
MkDocs plugin for rendering Unreal Engine Blueprint nodes.
"""

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class BlueprintUEPlugin(BasePlugin):
    """
    MkDocs plugin for rendering Unreal Engine Blueprint nodes.
    """
    
    config_scheme = (
        ('css_path', config_options.Type(str, default='css')),
        ('js_path', config_options.Type(str, default='js')),
    )

    def on_config(self, config):
        """
        The config event is the first event called on build and is run immediately 
        after the user configuration is loaded and validated. Any alterations to 
        the config should be made here.
        """
        return config

    def on_page_markdown(self, markdown, page, config, files):
        """
        The page_markdown event is called after the page's markdown is loaded 
        from file and can be used to alter the Markdown source text. 
        The meta-data has been stripped off and is available as page.meta 
        at this point.
        """
        return markdown

    def on_post_page(self, output, page, config):
        """
        The post_page event is called after the page is rendered, but before it 
        is written to disk. It can be used to alter the output of the page. 
        This is the last chance to modify the page.
        """
        return output
