# cd nas-file-checker/backend-python/
# source venv/bin/activate


import threading
import webbrowser
from nas_reader2 import app

def start_server():
    # 關閉 debug 避免重啟問題
    app.run(host='127.0.0.1', port=5000, debug=False)

if __name__ == '__main__':
    # 啟動 Flask 伺服器（在子執行緒中執行）
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # 使用 webbrowser.open() 打開系統預設瀏覽器
    webbrowser.open('http://127.0.0.1:5000/')

    # 保持主執行緒存活，等使用者按下 Enter 再關閉
    input("Press Enter to stop the server...\n")

