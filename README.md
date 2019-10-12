# 声明

> 此项目用于获取及设置token

# 部署方式

1. 安装python环境  
这里不再赘述，请参考:[python环境安装配置](https://github.com/bxxfighting/knowledge/blob/master/python/python%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)  

2. 安装依赖  
```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```
> 在你装好的虚拟环境下安装  

3. 配置supervisor  
```
command=/root/.pyenv/versions/3.6.6/envs/gt/bin/python /root/.pyenv/versions/gt/bin/gunicorn application:app --bind 0.0.0.0:8866
directory=/var/www/gt
```
> 命令指定到安装虚拟环境对应的bin目录下，指定打开端口  
> 指定程序目录  

4. nginx代理  
> 通过配置nginx将请求转发到8866端口  
```
server {
        listen 80;
        listen [::]:80;

        server_name gt.buxingxing.com;

        root /var/www/gt;
        index index.html;

        location / {
                proxy_redirect off;
                proxy_pass http://localhost:8866;
        }
}
```
