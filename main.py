import networkx as nx
import ast
import inspect
import fib_fun


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.graph = nx.Graph()
        self.curr_node = 0
        self.attributes = {}

    def generic_visit(self, node):
        num = self.curr_node
        self.curr_node += 1
        # print(node.__class__.__name__ + str(num))
        children = []
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        c = self.visit(item)
                        if not isinstance(c, list):
                            children.append(c)
            elif isinstance(value, ast.AST):
                c = self.visit(value)
                if not isinstance(c, list):
                    children.append(c)

        self.graph.add_edges_from(map(lambda x: (num, x), children))
        return num


    def visit_For(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'peachpuff1', 'label': node.__class__.__name__, 'shape': 'rectangular'}
        return num

    def visit_Name(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightcyan1', 'label': "Variable '{}'".format(node.id), 'shape': 'rectangular'}
        return num

    def visit_BinOp(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightyellow1', 'label': node.__class__.__name__, 'shape': 'ellipse'}
        return num

    def visit_Subscript(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Attribute(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightyellow1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Sub(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Call(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'ellipse'}
        return num

    def visit_Expr(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Constant(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightcyan1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_List(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightgoldenrod1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_arg(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightgoldenrod1', 'label': "Variable '{}'".format(node.arg),
                                'shape': 'rectangular'}
        return num

    def visit_Assign(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'ellipse'}
        return num

    def visit_Add(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightyellow1', 'label': node.__class__.__name__,
                                'shape': 'ellipse '}
        return num

    def visit_arguments(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightgoldenrod1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Return(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'peachpuff1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Store(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightgoldenrod1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Load(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'grey90', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_Module(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'peachpuff1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num

    def visit_FunctionDef(self, node):
        num = self.generic_visit(node)
        self.attributes[num] = {'style': 'filled', 'fillcolor': 'lightgoldenrod1', 'label': node.__class__.__name__,
                                'shape': 'rectangular'}
        return num


def main():
    source = inspect.getsource(fib_fun)
    tree = ast.parse(source)
    v = Visitor()
    v.visit(tree)
    # set attributes to each node
    visual = nx.drawing.nx_agraph.to_agraph(nx.dfs_tree(v.graph))
    for node in visual.nodes():
        for key, value in v.attributes[int(node)].items():
            node.attr[key] = value

    visual.layout('dot')
    visual.draw('artifacts/ast.png', format='png')

if __name__ == "__main__":
    main()
    