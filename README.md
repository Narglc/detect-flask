
## 宿主机上启动
###  0. 开启虚拟环境
python -m venv .env
. .env/bin/activate

### 1. 运行flask
flask run  -h 0.0.0.0 -p 5000
或
./run.sh
> 注：logs 文件夹必须存在!
> 注：如果之前曾经使用docker compose启动过，请删除logs/detect.srv.log文件，再运行。

### 2. 测试
```bash
# 容器验证测试:根据上述1,2步骤运行,使用默认端口5000启动
curl -X POST -H "Content-Type: application/json" -d '{"text": "你還好嗎?"}' http://localhost:9527/detect-language
```

### 3. 生成 requirements.txt
pip freeze >requirements.txt

### 4. 利用requirements.txt安装依赖
pip install -r requirements.txt


## 容器运行
### 1. 启动
```bash
docker compose up -d
```
### 2. 测试验证
```bash
# 使用容器测试, 映射端口不一样
curl -X POST -H "Content-Type: application/json" -d '{"text": "你還好嗎?"}' http://localhost:9527/detect-language
```