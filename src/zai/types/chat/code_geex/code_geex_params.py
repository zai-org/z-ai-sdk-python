from typing import List, Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = [
	'CodeGeexTarget',
	'CodeGeexContext',
	'CodeGeexExtra',
]


class CodeGeexTarget(TypedDict, total=False):
	"""
	Code completion target parameters

	Attributes:
		path (str | None): File path
		language (Literal[]): Programming language, such as python
		code_prefix (str): The text before the completion position
		code_suffix (str): The text after the completion position
	"""

	path: Optional[str]
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
	code_prefix: Required[str]
	code_suffix: Required[str]


class CodeGeexContext(TypedDict, total=False):
	"""
	Additional code

	Attributes:
		path (str): Path to the additional code file
		code (str): Additional code content
	"""

	path: Required[str]
	code: Required[str]


class CodeGeexExtra(TypedDict, total=False):
	"""
	Code completion extra parameters

	Attributes:
		target (CodeGeexTarget): Code completion target parameters
		contexts (List[CodeGeexContext] | None): Additional code
	"""

	target: Required[CodeGeexTarget]
	contexts: Optional[List[CodeGeexContext]]
