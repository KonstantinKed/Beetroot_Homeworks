
import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = math_exp.split()
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['and', 'or', 'not']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['and', 'or', 'not', ')']:
            try:
                i = True if i.lower() == 'true' else False # turn str to bool
                current_tree.set_root_val((i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'and': operator.and_, 'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child())+')'
    return s_val


if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree(" ( True and False ) ")
    print(evaluate(pt))
    pt1: BinaryTree = build_parse_tree(" ( True or False ) ")
    print(evaluate(pt1))
    pt2: BinaryTree = build_parse_tree(" ( False and True ) ")
    print(evaluate(pt2))
    pt3: BinaryTree = build_parse_tree(" ( False or False ) ")
    print(evaluate(pt3))
    pt4: BinaryTree = build_parse_tree(" ( True and True ) ")
    print(evaluate(pt4))
    pt5: BinaryTree = build_parse_tree(" ( not True ) ")
    print(evaluate(pt5))
    print("__")
    print(print_exp(pt5))