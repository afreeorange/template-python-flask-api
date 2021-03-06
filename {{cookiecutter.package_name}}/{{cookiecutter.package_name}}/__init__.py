from datetime import datetime
import os

from .factory import create_app


__title__ = '{{cookiecutter.package_name}}'
__version__ = '{{cookiecutter.version}}',
__author__ = '{{cookiecutter.author}}'
__author_email__ = '{{cookiecutter.email}}'
__license__ = 'MIT'
__copyright__ = '(c) {}'.format(datetime.now().year)
__url__ = '{{cookiecutter.project_repository}}'
__description__ = """
{{cookiecutter.project_description}}
"""

app = create_app(debug=os.getenv('DEBUG', False))
