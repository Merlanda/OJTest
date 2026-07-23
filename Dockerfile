# 基础镜像：轻量级 Python
FROM python:3.11-slim

# 设置工作目录（容器内的目录）
WORKDIR /app

# 复制项目文件到容器中
COPY permutation_rank.py .
COPY test_permutation_rank.py .

# 默认运行测试（可被 docker run 命令覆盖）
CMD ["python", "test_permutation_rank.py"]
