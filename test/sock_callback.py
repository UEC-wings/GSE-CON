import socket

HOST = "localhost"
PORT = 50000

def echo_server(host=HOST, port=PORT):
    # TCP/IPソケットを作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # アドレスの再利用を許可
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # ホストとポートにバインド
        server_socket.bind((host, port))
        # 接続待ち状態にする（最大5件の接続をキューに待機可能）
        server_socket.listen(5)
        print(f"エコーサーバーは {host}:{port} で待機中です")
        
        try:
            while True:
                # 接続要求を受け入れる
                conn, addr = server_socket.accept()
                
                with conn:
                    print(f"接続されました: {addr}")
                    
                    while True:
                        # クライアントからデータを受信（最大1024バイト）
                        data = conn.recv(1024)
                        
                        if not data:
                            # 受信データがない場合はクライアントが切断したとみなす
                            print(f"切断されました: {addr}")
                            return
                        else:
                            # 受信したデータをそのまま送り返す
                            conn.sendall(data)
                            data = int.from_bytes(data, byteorder='little', signed=False)
                            print(f"size: {len(data.to_bytes((data.bit_length() + 7) // 8, byteorder='little'))}")
                            print(f"received: {' '.join(f'{byte:02x}' for byte in data.to_bytes((data.bit_length() + 7) // 8, byteorder='little'))}")
                            print(f"sent: {' '.join(f'{byte:02x}' for byte in data.to_bytes((data.bit_length() + 7) // 8, byteorder='little'))}")
                            
        except KeyboardInterrupt:
            print("サーバーを停止します")
            return
                        
if __name__ == "__main__":
    echo_server()
