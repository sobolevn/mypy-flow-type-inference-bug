from mypy.plugin import Plugin
from pprint import pprint


def _flow_inference(ctx):
    print(ctx)
    pprint(ctx.arg_types)
    print()

    print([
        ctx.api.expr_checker.accept(n) for n in ctx.args[1]
    ])

    # We don't really care what happens next in this example,
    # so we just return the default type
    return ctx.default_return_type


class _ExamplePlugin(Plugin):
    def get_function_hook(self, fullname):
        if fullname == 'example.functions.flow':
            return _flow_inference
        return None


def plugin(version):
    return _ExamplePlugin
