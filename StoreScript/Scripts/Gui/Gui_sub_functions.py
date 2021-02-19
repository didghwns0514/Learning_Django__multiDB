import types

def alloc(call_back=None)->types.FunctionType:
	"""function allocater by name"""

	if call_back != None and isinstance(call_back, types.FunctionType):
		return call_back()

