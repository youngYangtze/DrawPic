import os
import numpy as np
from DrawPic import DrawPic
import matplotlib.pyplot as plt

def create_directory(directory):
    """Creat Directory

    Args:
        directory (string): file directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def test_DrawPic():
    """test draw picture class"""
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 3, 5, 7, 11]
    x2 = [1, 2, 3, 4, 5]
    y2 = [1, 4, 6, 8, 10]
    z1 = [1, 4, 6, 8, 10]
    z2 = [2, 5, 8, 11, 14]
    dx = 0.1
    dy = 0.1

    # 创建存储图像的目录
    create_directory("pic")

    plotter = DrawPic(
        xlabel="X", ylabel="Y", zlabel="Z", use_seaborn=True, seaborn_style="darkgrid"
    )

    # 测试叠加绘图
    ax = plotter.plot_line(x1, y1, "Line 1", show=False)
    plotter.plot_scatter(x2, y2, "Scatter 2", ax=ax, colors=["#FF5733"], show=False)
    ax.figure.savefig("pic/test_overlay.png")

    # 新增测试 plot_histogram 方法
    data2 = np.random.randn(500)
    plotter.plot_histogram(data2, bins=20, xlabel="Value", ylabel="Frequency", save_path="pic/test_histogram2.png")

    # 测试 plot_line 方法
    plotter.plot_line(x1, y1, "Line 1", save_path="pic/test_line1.png")
    plotter.plot_line(
        x1,
        y1,
        "Line 1",
        x2,
        y2,
        "Line 2",
        save_path="pic/test_line2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_line(
        x1,
        y1,
        "Line 1",
        save_path="pic/test_line3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_bar 方法
    plotter.plot_bar(x1, y1, "Bar 1", save_path="pic/test_bar1.png")
    plotter.plot_bar(
        x1,
        y1,
        "Bar 1",
        x2,
        y2,
        "Bar 2",
        save_path="pic/test_bar2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_bar(
        x1,
        y1,
        "Bar 1",
        save_path="pic/test_bar3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_scatter 方法
    plotter.plot_scatter(x1, y1, "Scatter 1", save_path="pic/test_scatter1.png")
    plotter.plot_scatter(
        x1,
        y1,
        "Scatter 1",
        x2,
        y2,
        "Scatter 2",
        save_path="pic/test_scatter2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_scatter(
        x1,
        y1,
        "Scatter 1",
        save_path="pic/test_scatter3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_3d_line 方法
    plotter.plot_3d_line(x1, y1, z1, "3D Line 1", save_path="pic/test_3d_line1.png")
    plotter.plot_3d_line(
        x1,
        y1,
        z1,
        "3D Line 1",
        x2,
        y2,
        z2,
        "3D Line 2",
        save_path="pic/test_3d_line2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_3d_line(
        x1,
        y1,
        z1,
        "3D Line 1",
        save_path="pic/test_3d_line3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_3d_scatter 方法
    plotter.plot_3d_scatter(
        x1, y1, z1, "3D Scatter 1", save_path="pic/test_3d_scatter1.png"
    )
    plotter.plot_3d_scatter(
        x1,
        y1,
        z1,
        "3D Scatter 1",
        x2,
        y2,
        z2,
        "3D Scatter 2",
        save_path="pic/test_3d_scatter2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_3d_scatter(
        x1,
        y1,
        z1,
        "3D Scatter 1",
        save_path="pic/test_3d_scatter3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_3d_bar 方法
    plotter.plot_3d_bar(
        x1, y1, z1, dx, dy, "3D Bar 1", save_path="pic/test_3d_bar1.png"
    )
    plotter.plot_3d_bar(
        x1,
        y1,
        z1,
        dx,
        dy,
        "3D Bar 1",
        x2,
        y2,
        z2,
        dx,
        dy,
        "3D Bar 2",
        save_path="pic/test_3d_bar2.png",
        colors=["#FF5733", "#33FF57"],
        show=False,
    )
    plotter.plot_3d_bar(
        x1,
        y1,
        z1,
        dx,
        dy,
        "3D Bar 1",
        save_path="pic/test_3d_bar3.png",
        figsize=(10, 6),
        equal_aspect=True,
    )

    # 测试 plot_histogram 方法
    data = np.random.randn(1000)
    plotter.plot_histogram(data, bins=30, save_path="pic/test_histogram.png")

    # 测试 plot_pie 方法
    sizes = [15, 30, 45, 10]
    labels = ["A", "B", "C", "D"]
    plotter.plot_pie(sizes, labels, save_path="pic/test_pie.png")

if __name__ == "__main__":
    test_DrawPic()
