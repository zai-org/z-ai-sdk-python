from typing import Optional

from typing_extensions import TypedDict


class SensitiveWordCheckRequest(TypedDict, total=False):
	"""
	Sensitive word check request parameters
	
	Attributes:
		type: Sensitive word type, currently only supports ALL
		status: Sensitive word enable/disable status
			Enable: ENABLE
			Disable: DISABLE
			Note: Sensitive word checking is enabled by default. To disable it, you need to
			      contact business to obtain corresponding permissions, otherwise the disable
			      setting will not take effect.
	"""
	type: Optional[str]
	status: Optional[str]
