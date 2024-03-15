FROM python:3.9

# 设置工作目录
WORKDIR /Fastapi

# 复制应用程序代码到容器中
#把所有代码复制到/app里面
COPY . /Fastapi

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 容器启动命令
CMD ["python", "main.py"]
