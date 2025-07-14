from typing import List, Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = [
	'CodeGeexTarget',
	'CodeGeexContext',
	'CodeGeexExtra',
]


class CodeGeexTarget(TypedDict, total=False):
	"""Completion content parameters"""

	path: Optional[str]
	"""File path"""
	language: Required[
		Literal[
			'c',
			'c++',
			'cpp',
			'c#',
			'csharp',
			'c-sharp',
			'css',
			'cuda',
			'dart',
			'lua',
			'objectivec',
			'objective-c',
			'objective-c++',
			'python',
			'perl',
			'prolog',
			'swift',
			'lisp',
			'java',
			'scala',
			'tex',
			'jsx',
			'tsx',
			'vue',
			'markdown',
			'html',
			'php',
			'js',
			'javascript',
			'typescript',
			'go',
			'shell',
			'rust',
			'sql',
			'kotlin',
			'vb',
			'ruby',
			'pascal',
			'r',
			'fortran',
			'lean',
			'matlab',
			'delphi',
			'scheme',
			'basic',
			'assembly',
			'groovy',
			'abap',
			'gdscript',
			'haskell',
			'julia',
			'elixir',
			'excel',
			'clojure',
			'actionscript',
			'solidity',
			'powershell',
			'erlang',
			'cobol',
			'alloy',
			'awk',
			'thrift',
			'sparql',
			'augeas',
			'cmake',
			'f-sharp',
			'stan',
			'isabelle',
			'dockerfile',
			'rmarkdown',
			'literate-agda',
			'tcl',
			'glsl',
			'antlr',
			'verilog',
			'racket',
			'standard-ml',
			'elm',
			'yaml',
			'smalltalk',
			'ocaml',
			'idris',
			'visual-basic',
			'protocol-buffer',
			'bluespec',
			'applescript',
			'makefile',
			'tcsh',
			'maple',
			'systemverilog',
			'literate-coffeescript',
			'vhdl',
			'restructuredtext',
			'sas',
			'literate-haskell',
			'java-server-pages',
			'coffeescript',
			'emacs-lisp',
			'mathematica',
			'xslt',
			'zig',
			'common-lisp',
			'stata',
			'agda',
			'ada',
		]
	]
	"""Code language type, such as python"""
	code_prefix: Required[str]
	"""The text before the completion position"""
	code_suffix: Required[str]
	"""The text after the completion position"""


class CodeGeexContext(TypedDict, total=False):
	"""Additional code"""

	path: Required[str]
	"""Path to the additional code file"""
	code: Required[str]
	"""Additional code content"""


class CodeGeexExtra(TypedDict, total=False):
	target: Required[CodeGeexTarget]
	"""Completion content parameters"""
	contexts: Optional[List[CodeGeexContext]]
	"""Additional code"""
