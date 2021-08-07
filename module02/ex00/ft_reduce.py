
def ft_reduce(function_to_apply, list_of_inputs):
    if not list_of_inputs:
        return

    result = list_of_inputs.pop(0)

    while list_of_inputs:
        result = function_to_apply(result, list_of_inputs.pop(0))

    return result