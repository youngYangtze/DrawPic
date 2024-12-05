# @Time    : 12/2/2024
# @Author  : wzyang
# @File    : DrawPic.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
import os


class DrawPic:
    """Python draw picture class"""

    def __init__(
        self,
        xlabel="X-axis",
        ylabel="Y-axis",
        zlabel="Z-axis",
        use_seaborn=True,
        seaborn_style="whitegrid",
    ):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.default_figsize = (16, 9)
        self.default_colors = ["#8891DB", "#C7988C", "#A5C496"]
        self.use_seaborn = use_seaborn
        self.seaborn_style = seaborn_style
        if use_seaborn:
            self.set_seaborn_style()  # 设置Seaborn风格

        plt.rcParams["font.family"] = "Times New Roman"  # 设置默认字体为Times New Roman

    def set_seaborn_style(self):
        sns.set_theme(style=self.seaborn_style)  # 设置Seaborn风格

    def _convert_df(self, df, x_col, y_col, z_col=None):
        if z_col:
            return df[x_col].values, df[y_col].values, df[z_col].values
        return df[x_col].values, df[y_col].values

    def plot_line(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.plot(x, y, label=label, color=color)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_bar(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        n_bars = len(args) // 3
        indices = np.arange(len(args[0]))  # 在循环外定义indices
        bar_width = 0.35 / n_bars
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.bar(indices + i * bar_width, y, bar_width, label=label, color=color)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_xticks(indices + bar_width * (n_bars - 1) / 2)
        ax.set_xticklabels(args[0])
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_scatter(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.scatter(x, y, label=label, color=color)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_3d_line(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 4):
            x, y, z, label = args[i], args[i + 1], args[i + 2], args[i + 3]
            color = colors[i // 4 % len(colors)]
            ax.plot(x, y, z, label=label, color=color)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_3d_scatter(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 4):
            x, y, z, label = args[i], args[i + 1], args[i + 2], args[i + 3]
            color = colors[i // 4 % len(colors)]
            ax.scatter(x, y, z, label=label, color=color)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_3d_bar(
        self,
        *args,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        show=True
    ):
        if figsize is None:
            figsize = self.default_figsize
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 6):  # 修改为6以包含label
            x, y, z, dx, dy, label = (
                args[i],
                args[i + 1],
                args[i + 2],
                args[i + 3],
                args[i + 4],
                args[i + 5],
            )
            color = colors[i // 6 % len(colors)]
            ax.bar3d(x, y, 0, dx, dy, z, label=label, color=color, shade=True)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()


def create_directory(directory):
    """Creat Directory

    Args:
        directory (string): file directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def test_DrawPic():
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


if __name__ == "__main__":
    test_DrawPic()
