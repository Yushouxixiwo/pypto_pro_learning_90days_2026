"""CPU 教学模型：不是 PyPTO 内核，也不是性能基准。"""
import ast
import inspect
import math


def scalar_add(x, y):
    return x + y


def reference(xs, ys):
    if len(xs) != len(ys):
        raise ValueError('输入长度必须相等')
    return [a + b for a, b in zip(xs, ys)]


def tiled_add(xs, ys, tile=64):
    if len(xs) != len(ys):
        raise ValueError('输入长度必须相等')
    if tile <= 0:
        raise ValueError('tile 必须为正')
    n = len(xs)
    guard = object()
    output = [guard] * (n + 2)
    for base in range(0, n, tile):
        valid = min(tile, n - base)
        # 简化模型：真实设备的物理读拍和 DMA 有自己的容量/对齐合同。
        local_x = [0.0] * tile
        local_y = [0.0] * tile
        for lane in range(valid):
            local_x[lane] = xs[base + lane]
            local_y[lane] = ys[base + lane]
        for lane in range(valid):
            output[1 + base + lane] = local_x[lane] + local_y[lane]
    assert output[0] is guard and output[-1] is guard
    return output[1:-1]


def main():
    tree = ast.parse(inspect.getsource(scalar_add))
    print('普通 Python 函数的 AST（不是 PyPTO IR）：')
    print(ast.dump(tree, indent=2))
    lengths = [0, 1, 63, 64, 65, 127, 128, 129]
    for n in lengths:
        xs = [float(i - 37) for i in range(n)]
        ys = [float((i % 7) - 3) for i in range(n)]
        assert tiled_add(xs, ys) == reference(xs, ys)
    print('PASS：8种长度的值与输出守卫检查；仅CPU功能模型。')
    for tile in [0, -1]:
        try:
            tiled_add([1.0], [2.0], tile)
        except ValueError:
            pass
        else:
            raise AssertionError('非法 tile 未被拒绝')
    print('PASS：非法tile检查。')


if __name__ == '__main__':
    main()
