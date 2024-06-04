# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录中
COPY . .

# 安装 Flask 和 requests 库
RUN pip install --no-cache-dir Flask requests

# 对外暴露端口 5000
EXPOSE 8310

# 启动应用
CMD ["python", "app.py"]
