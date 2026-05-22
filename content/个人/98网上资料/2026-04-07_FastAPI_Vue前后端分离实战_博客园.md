# FastAPI + Vue 前后端分离实战：我的项目结构"避坑指南"

## 作者信息
- **作者**：一名程序媛呀
- **平台**：博客园 (cnblogs.com)
- **原始链接**：https://www.cnblogs.com/ymtianyu/p/19828178

## 核心内容

### 文章脉络
- 一个让你血压飙升的联调场景
- 我的"强迫症"项目结构（直接拿去用）
- 通信的3个核心配置（少一个都会炸）
- 开发环境 vs 生产环境：别再手改baseURL了！
- 那些文档不会告诉你的"隐形坑"
- 进阶思考：拆分vs聚合，你的项目适合哪种？

### 真实"案发现场"
小张花了一周写完FastAPI接口，用Postman测试全部通过。但一联调就遇到：
- `Access-Control-Allow-Origin` 错误
- 装错cors库（flask-cors vs FastAPI）
- POST请求报 `422 Unprocessable Entity` — 前端传的JSON格式后端不认

### 项目结构
```
fastapi_vue_project/
├── backend/                 # FastAPI后端
│   ├── app/
│   │   ├── api/           # 路由层（按模块分）
│   │   ├── core/          # 配置、安全、数据库连接
│   │   ├── models/        # SQLAlchemy模型
│   │   ├── schemas/       # Pydantic模型
│   │   ├── services/      # 业务逻辑层
│   │   └── main.py        # 入口
│   ├── requirements.txt
│   └── .env
├── frontend/              # Vue3前端
│   ├── src/
│   │   ├── api/          # 封装axios请求
│   │   ├── views/        # 页面
│   │   ├── router/      # 路由
│   │   └── utils/       # 工具函数
│   └── .env.development/.env.production
└── docker-compose.yml
```

### 通信的3个核心配置

**1. FastAPI的CORS中间件**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,  # 注意！不是 "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)
```
坑：如果前端用 `axios` 带上了 `withCredentials: true`，后端 `allow_origins` 就不能是 `"*"`

**2. Vue的代理配置（Vite）**
```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, '')
    }
  }
}
```
坑：rewrite规则写错会导致404

**3. 统一的响应格式**
```python
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar('T')
class ResponseModel(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[T] = None
```

### 环境变量管理
```bash
# frontend/.env.development
VITE_API_BASE_URL = '/api'

# frontend/.env.production  
VITE_API_BASE_URL = 'https://your-api-domain.com'

# frontend/src/api/request.js
const request = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    timeout: 10000
})
```

### 关键教训
- 生产环境 `allow_origins` 千万别用 `["*"]`
- 环境变量永远不要写死在代码里
- 统一响应格式，减少前后端沟通成本
- 错误码至少约定401/403/422，别让前端猜

---

*来源：博客园 - 一名程序媛呀*
