# DrawPic 📊

`DrawPic` 是一个用于绘制各种图表的 Python 类，支持 2D 和 3D 图表。该类提供了多种绘图方法，包括折线图、柱状图、散点图、直方图和饼图等。

## 安装 🛠️

确保已安装以下依赖项：

- matplotlib
- seaborn
- pandas
- numpy

可以使用以下命令安装依赖项：

```bash
pip install matplotlib seaborn pandas numpy
```

## 使用方法 📈

### 初始化

```python
from DrawPic import DrawPic

plotter = DrawPic(
    xlabel="X", ylabel="Y", zlabel="Z", use_seaborn=True, seaborn_style="darkgrid"
)
```

### 绘制折线图 📉

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
plotter.plot_line(x1, y1, "Line 1", save_path="pic/line.png")
```

### 绘制柱状图 📊

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
plotter.plot_bar(x1, y1, "Bar 1", save_path="pic/bar.png")
```

### 绘制散点图 🔵

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
plotter.plot_scatter(x1, y1, "Scatter 1", save_path="pic/scatter.png")
```

### 绘制直方图 📊

```python
data = np.random.randn(1000)
plotter.plot_histogram(data, bins=30, save_path="pic/histogram.png")
```

### 绘制饼图 🥧

```python
sizes = [15, 30, 45, 10]
labels = ["A", "B", "C", "D"]
plotter.plot_pie(sizes, labels, save_path="pic/pie.png")
```

### 绘制 3D 折线图 📈

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
z1 = [1, 4, 6, 8, 10]
plotter.plot_3d_line(x1, y1, z1, "3D Line 1", save_path="pic/3d_line.png")
```

### 绘制 3D 散点图 🔵

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
z1 = [1, 4, 6, 8, 10]
plotter.plot_3d_scatter(x1, y1, z1, "3D Scatter 1", save_path="pic/3d_scatter.png")
```

### 绘制 3D 柱状图 📊

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
z1 = [1, 4, 6, 8, 10]
dx = 0.1
dy = 0.1
plotter.plot_3d_bar(x1, y1, z1, dx, dy, "3D Bar 1", save_path="pic/3d_bar.png")
```

### 叠加绘图 🔄

```python
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 6, 8, 10]

ax = plotter.plot_line(x1, y1, "Line 1", show=False)
plotter.plot_scatter(x2, y2, "Scatter 2", ax=ax, colors=["#FF5733"], show=False)
ax.figure.savefig("pic/overlay.png")
```

## 测试 🧪

可以使用以下命令运行测试：

```bash
python test.py
```

## 许可证 📜

此项目使用 MIT 许可证。

