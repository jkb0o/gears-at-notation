import re
import os

from gears.asset_attributes import AssetAttributes
from gears.processors.directives import DirectivesProcessor
from gears.directives_parser import DirectivesParser


class AtDirectivesParser(DirectivesParser):
    directive_re = re.compile(r"""
        ^ \s* (?:\*|//|\#) \s* @ ( \w+ [./'"\s\w-]* ) $
    """, re.X)

class AtDirectivesProcessor(DirectivesProcessor):
    
    def parse(self):
        directives, source = AtDirectivesParser().parse(self.asset.processed_source)

        self.directives = directives
        self.asset.processed_source = source
    
    def find(self, require_path):
        require_path = self.get_relative_path(require_path)
        asset_attributes = AssetAttributes(self.asset.attributes.environment, require_path)
        return self.asset.attributes.environment.find(asset_attributes)

    def get_relative_path(self, require_path, is_directory=False):
        require_path = os.path.join(self.asset.attributes.dirname, require_path)
        require_path = os.path.normpath(require_path)
        return require_path

