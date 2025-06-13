import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
import numpy as np
from DrawPic.DrawPic2D import DrawPic2D
from DrawPic.DrawPic3D import DrawPic3D

class DrawPic(DrawPic2D, DrawPic3D):
    """Python draw picture class"""

    def __init__(
        self,
        xlabel: str = "X-axis",
        ylabel: str = "Y-axis",
        zlabel: str = "Z-axis",
        figsize: tuple = (16, 3),
        use_seaborn: bool = True,
        seaborn_style: str = "whitegrid",
        default_save: bool = True,
        default_show: bool = True,
        xlabel_fontsize: int = 25,
        ylabel_fontsize: int = 25,
    ):
        """初始化绘图类

        Args:
            xlabel (str): X轴标签
            ylabel (str): Y轴标签
            zlabel (str): Z轴标签
            figsize (tuple): 图像尺寸
            use_seaborn (bool): 是否使用Seaborn风格
            seaborn_style (str): Seaborn风格
            default_save (bool): 是否默认保存图像
            default_show (bool): 是否默认显示图像
            xlabel_fontsize (int): X轴标签字体大小
            ylabel_fontsize (int): Y轴标签字体大小
        """
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.default_figsize = figsize
        self.default_colors = ["#8891DB", "#C7988C", "#A5C496", "#F9C784", "#A5C4E1", "#C4A5E1"]
        self.use_seaborn = use_seaborn
        self.seaborn_style = seaborn_style
        self.default_save = default_save
        self.default_show = default_show
        self.xlabel_fontsize = xlabel_fontsize
        self.ylabel_fontsize = ylabel_fontsize
        if use_seaborn:
            self.set_seaborn_style()  # 设置Seaborn风格

        plt.rcParams["font.family"] = "Times New Roman"  # 设置默认字体为Times New Roman

    def set_seaborn_style(self):
        """设置Seaborn风格"""
        sns.set_theme(style=self.seaborn_style)  # 设置Seaborn风格

    def _convert_df(self, df: pd.DataFrame, x_col: str, y_col: str, z_col: str = None):
        """转换DataFrame为数组

        Args:
            df (pd.DataFrame): 数据框
            x_col (str): X轴列名
            y_col (str): Y轴列名
            z_col (str, optional): Z轴列名

        Returns:
            tuple: 转换后的数组
        """
        if z_col:
            return df[x_col].values, df[y_col].values, df[z_col].values
        return df[x_col].values, df[y_col].values
