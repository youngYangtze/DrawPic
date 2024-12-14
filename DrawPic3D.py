import matplotlib.pyplot as plt

class DrawPic3D:
    """3D 绘图方法"""

    def plot_3d_line(
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
        show: bool = None
    ):
        """绘制3D折线图"""
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

        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 4):
            x, y, z, label = args[i], args[i + 1], args[i + 2], args[i + 3]
            color = colors[i // 4 % len(colors)]
            ax.plot(x, y, z, label=label, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.set_zlabel(self.zlabel, fontsize=14)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_3d_scatter(
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
        show: bool = None
    ):
        """绘制3D散点图"""
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

        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 4):
            x, y, z, label = args[i], args[i + 1], args[i + 2], args[i + 3]
            color = colors[i // 4 % len(colors)]
            ax.scatter(x, y, z, label=label, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.set_zlabel(self.zlabel, fontsize=14)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_3d_bar(
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
        show: bool = None
    ):
        """绘制3D柱状图"""
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
        ax.set_xlabel(xlabel if xlabel else self.xlabel, fontsize=xlabel_fontsize)
        ax.set_ylabel(ylabel if ylabel else self.ylabel, fontsize=ylabel_fontsize)
        ax.set_zlabel(self.zlabel, fontsize=14)
        ax.legend()
        if equal_aspect:
            ax.set_box_aspect([1, 1, 1])  # aspect ratio is 1:1:1
        if save_path and save:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()
