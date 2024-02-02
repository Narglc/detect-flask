
##  0. 开启虚拟环境
python -m venv .env
. .env/bin/activate

## 1. 运行flask
flask run  -h 0.0.0.0 -p 5000
或
./run.sh
> 注：logs 文件夹必须存在!

## 2. 测试
curl -X POST -H "Content-Type: application/json" -d '{"text": "你還好嗎?"}' http://localhost:5000/detect-language

## 2. 生成 requirements.txt
pip freeze >requirements.txt

## 3. 利用requirements.txt安装依赖
pip install -r requirements.txt