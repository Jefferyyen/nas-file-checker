# nas-file-checker
AS File Checker – A web-based solution to list and analyze files &amp; Excel data from NAS.
# Side Project Overview

## 1. Side Project 整體目標與功能

### 主要目標
- **從 NAS（或網路磁碟）路徑中，讀取檔案清單、Excel 檔等資料。**  
- **透過後端提供 API，前端呼叫並顯示檔案狀態、名稱、內容**（例如 Excel 的指定工作表內容）。  
- **適度進行運算**（加總、判斷、分析），最終在網頁上呈現報告或列表。

### 進階功能（未來可擴充）
- 登入/權限管理  
- 寫入資料庫（如 MySQL / MongoDB），做更複雜的篩選或歷史紀錄  
- 圖表視覺化 (Chart.js)  
- 資料檔案的操作（新增、刪除、搬移）  
- 文件預覽或版本控制  

---

## 2. 打算分兩階段做後端

### 階段 1：Python 後端 + JS 前端
- **Python 以 Flask（或 FastAPI）為主：**
  - 負責讀取 NAS 上檔案、開啟並解析 Excel 等  
  - 提供 RESTful API (JSON) 給前端使用  

- **前端以「HTML + JavaScript (或 React)」來實作：**
  - 接收 API 回傳的 JSON，並動態渲染在網頁上（表格/清單/運算結果）

### 階段 2：Node.js 後端 + JS 前端
- **重新用 Node.js（Express / NestJS / Koa 等）開發同樣 API：**
  - 同樣從 NAS 讀檔、解析 Excel  
  - 保持與 Python 版相同的資料結構與路徑設計（例如 `GET /api/files`、`GET /api/excel-data` 等）

- **前端直接沿用「階段 1」的程式碼**，不需大幅改動，只要換一下 API 連線位置即可。

> **好處：** 能充分練習前後端分離的概念，練習 Python & Node 的熟悉程度。

---

## 3. 運用的主要技術與套件

### Python 後端 (Flask/FastAPI)
- **openpyxl** 或 **pandas**：讀取 Excel、做資料處理  
- **os** 或 **pathlib**：存取 NAS 路徑，列出檔案  
- **Flask / FastAPI**：建立 REST API (JSON 回傳)

### Node.js 後端 (Express/NestJS)
- **fs / path**：存取 NAS 路徑  
- **xlsx** 或 **ExcelJS**：讀取 Excel 檔  
- **Express**：建立 REST API (JSON 回傳)

### 前端 (JS / React)
- **若純 JS + HTML：**
  - `fetch` 或 `axios` 來呼叫後端 API  
  - DOM 操控或使用一些前端套件 (DataTables / chart.js / etc.) 來顯示資料

- **若用 React：**
  - 建立 components，透過 `fetch('/api/...')` 拿 JSON  
  - 使用 state & props 來渲染表格、列表或圖表

### Git & GitHub
- **多分支開發 (Branches)：**  
  - `python-backend` vs. `node-backend`
- **Pull Requests / Issues：**  
  - 紀錄功能開發、版本演進
- **README 整理：**  
  - 教大家如何啟動後端、如何啟動前端

---

## 4. 建議的 GitHub 目錄分配

### 作法 A：在同一個 Repository 中分目錄管理

```plaintext
my-side-project/
├── README.md                 # 專案總覽、特色、如何部署
├── .gitignore                # 忽略檔案設定
├── python-backend/           # Python 後端
│   ├── app.py                # Flask/FastAPI 主程式
│   ├── requirements.txt      # Python 套件列表
│   └── ...                   # 其他 Python 模組、設定檔等
├── node-backend/             # Node.js 後端
│   ├── package.json          # Node 套件列表
│   ├── server.js             # Express 主程式
│   └── ...                   # 其他設定檔、路由檔案等
└── frontend/
    ├── index.html
    ├── main.js
    ├── ...                   # 若使用 React，這裡可以有 src/ public/ 等資料夾
```
#### 優點
- 同一個 repo 就能看見兩種後端版本；frontend 與後端在同一層級。  
- 清楚區隔 Python/Node 後端程式碼。  

#### 缺點
- 如果想要單獨部署 Python 或 Node 版本，可能在設定上要多注意（但大多數情況下沒問題）。  

---

### 作法 B：同一個 Repo，但用分支 (Branch) 隔開
- **main**：主要前端 (或僅存放最基礎的 README & .gitignore)。  
- **python-backend**：包含了 Python 後端 + 前端。  
- **node-backend**：包含了 Node 後端 + 前端。

#### 優點
- 能清楚看到兩個分支的 diff，對比 Python/Node 版本。  
- main 可保持一個「乾淨的基礎」。  

#### 缺點
- 可能在切換分支時，會整個目錄都不一樣；如果前端程式碼要在「Python/Node」兩條分支都同時進行修改，需要合併/Cherry-pick。  

---

### 作法 C：分成兩個 Repo
- **my-side-project-python**  
- **my-side-project-node**  

> Frontend 可以放在其中一個 Repo 或拆成第三個獨立 Repo。  

**優缺點**：對應於大專案的微服務概念，但對目前 Side Project 可能稍顯複雜，不建議。  

---

## 五、最適合的綜合建議

- **採用「同一個 Repo + 目錄區分」** 會相對直覺：
  - 例如：
    - `python-backend/` 下開發 Python 版本。
    - `node-backend/` 下開發 Node 版本。
    - `frontend/` 放公共的前端。  
  - 讓人一看就知道「這裡有兩個後端版本，同一個前端」。

### 前端共用
- 在 `frontend/` 中，可以在程式裡設定一個 `BASE_API_URL`（可用環境變數、或在 `.env` 中設定），切換要呼叫 `http://localhost:5000` (Python) 或 `http://localhost:3000` (Node) 都行。  
- 這樣一套前端就可以無縫串接兩個後端。

### 在 README 中記得寫明
- 專案背景、需求、功能列表。  
- **如何啟動 Python 後端：**
  ```bash
  cd python-backend
  pip install -r requirements.txt
  python app.py
```
## 如何啟動 Node 後端

```bash
cd node-backend
npm install
npm start
```
## 如何啟動前端

### 若純 HTML/JS
直接打開 `frontend/index.html`。

### 若是 React 專案

```bash
cd frontend
npm install
npm run start
```
## Git 分支運用（可搭配目錄式管理一起使用）

- **main**：放可用的 Python 版或放穩定版。
- **feature/python-excel**：專門開發讀 Excel 功能。
- **feature/node-excel**：Node 版的讀 Excel 功能。

> 開好後再透過 PR 合併回 `main`，依個人習慣調整即可。

---

## 六、總結

### 結構概念
這是一個 **全端應用**，需要清楚區分後端與前端的程式。

### 技術
- **後端**：Python/Node 各自讀取 NAS + Excel，並提供 JSON。
- **前端**：使用原生 JavaScript 或 React 顯示及處理 API 傳回的資料。

### GitHub 目錄建議
建議同一個 Repo，下有：
`python-backend/`
`node-backend/`
`frontend/`

並在 README 中做總覽說明，這樣維護和呈現都相對簡單。

### 益處
- 一次練習兩種後端技術，展示多樣化的技能，並擁有清楚的專案結構。。
- 前後端分離練習。
- Git 與 GitHub 版本管理實務。
- 這樣的架構未來在做功能擴充、Bug 修復、或搬移到雲端平台時更有條理。



