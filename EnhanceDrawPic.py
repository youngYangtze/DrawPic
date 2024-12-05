# @Time    : 12/5/2024
# @Author  : wzyang
# @File    : EnhanceDrawPic.py
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
import numpy as np
from DrawPic import DrawPic


class EnhancedDrawPic(DrawPic):
    """Enhanced Python draw picture class with additional functionality for DataFrame and more plot types"""

    def __init__(
        self,
        xlabel="X-axis",
        ylabel="Y-axis",
        zlabel="Z-axis",
        figsize=(16, 9),
        use_seaborn=True,
        seaborn_style="whitegrid",
        default_save=True,
        default_show=True,
    ):
        super().__init__(
            xlabel,
            ylabel,
            zlabel,
            figsize,
            use_seaborn,
            seaborn_style,
            default_save,
            default_show,
        )

    def plot_from_df(
        self,
        df,
        x_col,
        y_col,
        plot_type="line",
        label=None,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        save=None,
        show=None,
    ):
        """General method to plot from DataFrame"""
        x = df[x_col].values
        y = df[y_col].values
        label = label if label else y_col

        if plot_type == "line":
            self.plot_line(
                x,
                y,
                label,
                save_path=save_path,
                figsize=figsize,
                equal_aspect=equal_aspect,
                colors=colors,
                save=save,
                show=show,
            )
        elif plot_type == "bar":
            self.plot_bar(
                x,
                y,
                label,
                save_path=save_path,
                figsize=figsize,
                equal_aspect=equal_aspect,
                colors=colors,
                save=save,
                show=show,
            )
        elif plot_type == "scatter":
            self.plot_scatter(
                x,
                y,
                label,
                save_path=save_path,
                figsize=figsize,
                equal_aspect=equal_aspect,
                colors=colors,
                save=save,
                show=show,
            )
        else:
            raise ValueError(f"Unsupported plot_type: {plot_type}")

    def plot_hist(
        self,
        data,
        bins=10,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        colors=None,
        save=None,
        show=None,
    ):
        """Plot histogram"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

        fig, ax = plt.subplots(figsize=figsize)
        color = colors[0] if colors else self.default_colors[0]
        ax.hist(data, bins=bins, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.grid(True)
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_box(
        self,
        data,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        colors=None,
        save=None,
        show=None,
    ):
        """Plot boxplot"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

        fig, ax = plt.subplots(figsize=figsize)
        color = colors[0] if colors else self.default_colors[0]
        ax.boxplot(data, patch_artist=True, boxprops=dict(facecolor=color))
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.grid(True)
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_density(
        self,
        data,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        colors=None,
        save=None,
        show=None,
    ):
        """Plot density plot"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

        fig, ax = plt.subplots(figsize=figsize)
        color = colors[0] if colors else self.default_colors[0]
        sns.kdeplot(data, ax=ax, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.grid(True)
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()


# 使用示例
def test_EnhancedDrawPic():
    df = pd.DataFrame(
        {"X": [1, 2, 3, 4, 5], "Y": [2, 4, 6, 8, 10], "Z": [1, 3, 5, 7, 9]}
    )

    plotter = EnhancedDrawPic(
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        figsize=(10, 6),
        use_seaborn=True,
        seaborn_style="darkgrid",
    )

    # 测试从 DataFrame 绘图
    plotter.plot_from_df(
        df, "X", "Y", plot_type="line", save_path="df_line_example.png"
    )

    # 测试直方图
    plotter.plot_hist(df["Y"], bins=5, save_path="hist_example.png")

    # 测试箱线图
    plotter.plot_box(df["Y"], save_path="box_example.png")

    # 测试密度图
    plotter.plot_density(df["Y"], save_path="density_example.png")


if __name__ == "__main__":
    test_EnhancedDrawPic()
