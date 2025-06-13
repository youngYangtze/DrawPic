import matplotlib.pyplot as plt
import numpy as np
import os

class DrawPic2D:
    """2D 绘图方法"""

    def plot_line(
        self,
        *args,
        xlabel: str = None,
        ylabel: str = None,
        xlabel_fontsize: int = None,
        ylabel_fontsize: int = None,
        save_path: str = None,
        figsize: tuple = None,
        equal_aspect: bool = False,
        colors: list = None,
        save: bool = None,
        show: bool = None,
        ax: plt.Axes = None
    ):
        """绘制折线图"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show
        if xlabel_fontsize is None:
            xlabel_fontsize = self.xlabel_fontsize
        if ylabel_fontsize is None:
            ylabel_fontsize = self.ylabel_fontsize

        fig = None
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.plot(x, y, label=label, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
       
        if save and save_path and fig is not None:
            # 获取保存路径的目录部分
            save_dir = os.path.dirname(save_path)
            # 如果目录不存在，则创建目录
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            fig.savefig(save_path, dpi=300)
        if show and fig is not None:
            plt.show()
        return ax

    def plot_bar(
        self,
        *args,
        xlabel: str = None,
        ylabel: str = None,
        xlabel_fontsize: int = None,
        ylabel_fontsize: int = None,
        save_path: str = None,
        figsize: tuple = None,
        equal_aspect: bool = False,
        colors: list = None,
        save: bool = None,
        show: bool = None,
        ax: plt.Axes = None
    ):
        """绘制柱状图"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show
        if xlabel_fontsize is None:
            xlabel_fontsize = self.xlabel_fontsize
        if ylabel_fontsize is None:
            ylabel_fontsize = self.ylabel_fontsize

        fig = None
        if ax is None:
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
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.set_xticks(indices + bar_width * (n_bars - 1) / 2)
        ax.set_xticklabels(args[0])
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save and save_path and fig is not None:
            fig.savefig(save_path, dpi=300)
        if show and fig is not None:
            plt.show()
        return ax

    def plot_scatter(
        self,
        *args,
        xlabel: str = None,
        ylabel: str = None,
        xlabel_fontsize: int = None,
        ylabel_fontsize: int = None,
        save_path: str = None,
        figsize: tuple = None,
        equal_aspect: bool = False,
        colors: list = None,
        save: bool = None,
        show: bool = None,
        s: float = 1.0,
        ax: plt.Axes = None
    ):
        """绘制散点图"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show
        if xlabel_fontsize is None:
            xlabel_fontsize = self.xlabel_fontsize
        if ylabel_fontsize is None:
            ylabel_fontsize = self.ylabel_fontsize

        fig = None
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.scatter(x, y, label=label, color=color, s=s)
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save and save_path and fig is not None:
            fig.savefig(save_path, dpi=300)
        if show and fig is not None:
            plt.show()
        return ax

    def plot_histogram(
        self,
        data: np.ndarray,
        bins: int = 10,
        xlabel: str = None,
        ylabel: str = None,
        xlabel_fontsize: int = None,
        ylabel_fontsize: int = None,
        save_path: str = None,
        figsize: tuple = None,
        colors: list = None,
        save: bool = None,
        show: bool = None,
        ax: plt.Axes = None
    ):
        """绘制直方图"""
        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show
        if xlabel_fontsize is None:
            xlabel_fontsize = self.xlabel_fontsize
        if ylabel_fontsize is None:
            ylabel_fontsize = self.ylabel_fontsize

        fig = None
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        color = colors[0] if colors else self.default_colors[0]
        ax.hist(data, bins=bins, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.grid(True)
        if save and save_path and fig is not None:
            fig.savefig(save_path, dpi=300)
        if show and fig is not None:
            plt.show()
        return ax
