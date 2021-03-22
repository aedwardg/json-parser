from parglare import get_collector
from parglare.actions import pass_inner

action = get_collector()

# Non-terminal rule actions
@action("Array")
def array_action(context, nodes):
    return pass_inner(context, nodes)


@action("Object")
def object_action(context, nodes):
    # Objects look like this before action:
    # ['{', [['key', ':', 'value'], ['key', ':', 'value'], ...], '}']
    if len(nodes) > 2:
        members = nodes[1:-1][0]
        return {member[0]: member[2] for member in members}
    else:
        return {}


@action("String")
def string_action(context, nodes):
    return pass_inner(context, nodes)


# Terminal Rule actions
@action("INT")
def int_action(context, value):
    return int(value)


@action("FLOAT")
def float_action(context, value):
    return float(value)


@action("NULL")
def null_action(context, value):
    return None


@action("TRUE")
def null_action(context, value):
    return True


@action("FALSE")
def null_action(context, value):
    return False
