# @Time    : 12/5/2024
# @Author  : wzyang
# @File    : InterActive.py
# @brife   : DrawPic With Interactive function
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


class DrawPic:
    """Python draw picture class"""

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
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.default_figsize = figsize
        self.default_colors = ["#8891DB", "#C7988C", "#A5C496"]
        self.use_seaborn = use_seaborn
        self.seaborn_style = seaborn_style
        self.default_save = default_save
        self.default_show = default_show
        if use_seaborn:
            self.set_seaborn_style()  # 设置Seaborn风格

        plt.rcParams["font.family"] = "Times New Roman"  # 设置默认字体为Times New Roman

    def set_seaborn_style(self):
        sns.set_theme(style=self.seaborn_style)  # 设置Seaborn风格

    def _convert_df(self, df, x_col, y_col, z_col=None):
        if z_col:
            return df[x_col].values, df[y_col].values, df[z_col].values
        return df[x_col].values, df[y_col].values

    def _get_user_input(self, prompt, options):
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Select an option: ")
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Using default.")
        except ValueError:
            print("Invalid input. Using default.")
        return None

    def plot_line(
        self,
        *args,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        save=None,
        show=None,
        interactive=False,
    ):
        if interactive:
            figsize = self._get_user_input(
                "Select figsize:", [(16, 9), (10, 6), (8, 4)]
            )
            equal_aspect = self._get_user_input("Equal aspect?", [True, False])
            colors = self._get_user_input(
                "Select colors:", [None, ["#FF5733", "#33FF57"], ["#A5C496", "#C7988C"]]
            )
            save = self._get_user_input("Save plot?", [True, False])
            show = self._get_user_input("Show plot?", [True, False])
            save_path = (
                input("Enter save path (leave empty to skip): ") if save else None
            )

        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

        fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.plot(x, y, label=label, color=color)
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_bar(
        self,
        *args,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        save=None,
        show=None,
        interactive=False,
    ):
        if interactive:
            figsize = self._get_user_input(
                "Select figsize:", [(16, 9), (10, 6), (8, 4)]
            )
            equal_aspect = self._get_user_input("Equal aspect?", [True, False])
            colors = self._get_user_input(
                "Select colors:", [None, ["#FF5733", "#33FF57"], ["#A5C496", "#C7988C"]]
            )
            save = self._get_user_input("Save plot?", [True, False])
            show = self._get_user_input("Show plot?", [True, False])
            save_path = (
                input("Enter save path (leave empty to skip): ") if save else None
            )

        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

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
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.set_xticks(indices + bar_width * (n_bars - 1) / 2)
        ax.set_xticklabels(args[0])
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()

    def plot_scatter(
        self,
        *args,
        xlabel=None,
        ylabel=None,
        save_path=None,
        figsize=None,
        equal_aspect=False,
        colors=None,
        save=None,
        show=None,
        s=1.0,
        interactive=False,
    ):
        if interactive:
            figsize = self._get_user_input(
                "Select figsize:", [(16, 9), (10, 6), (8, 4)]
            )
            equal_aspect = self._get_user_input("Equal aspect?", [True, False])
            colors = self._get_user_input(
                "Select colors:", [None, ["#FF5733", "#33FF57"], ["#A5C496", "#C7988C"]]
            )
            save = self._get_user_input("Save plot?", [True, False])
            show = self._get_user_input("Show plot?", [True, False])
            s = float(input("Enter scatter size: "))
            save_path = (
                input("Enter save path (leave empty to skip): ") if save else None
            )

        if figsize is None:
            figsize = self.default_figsize
        if save is None:
            save = self.default_save
        if show is None:
            show = self.default_show

        fig, ax = plt.subplots(figsize=figsize)
        if colors is None:
            colors = self.default_colors
        for i in range(0, len(args), 3):
            x, y, label = args[i], args[i + 1], args[i + 2]
            color = colors[i // 3 % len(colors)]
            ax.scatter(x, y, label=label, color=color, s=s)
        ax.set_xlabel(xlabel if xlabel else self.xlabel)
        ax.set_ylabel(ylabel if ylabel else self.ylabel)
        ax.legend()
        ax.grid(True)
        if equal_aspect:
            ax.set_aspect("equal", adjustable="box")
        if save and save_path:
            plt.savefig(save_path, dpi=300)
        if show:
            plt.show()


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
        interactive=True,
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


if __name__ == "__main__":
    test_DrawPic()
