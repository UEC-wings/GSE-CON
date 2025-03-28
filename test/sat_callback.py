import socket

HOST = "localhost"
PORT = 50000

def create_send_packet(data: bytearray) -> None:
    """データを送信するためのパケットを作成する関数
    Args:
        data (bytearray): 送信するデータ
    Returns:
        send_packet (bytearray): 送信するパケット
    """
    # start bit
    STX1 = 0x0F
    STX2 = 0xF0
    
    # packet index
    STX1_INDEX = 0
    STX2_INDEX = 1
    COUNT_INDEX = 2
    MODE_INDEX = 3
    CRC16_INDEX = 4
    
    # size
    size = len(data)
    
    # slice
    stx1 = data[STX1_INDEX]
    stx2 = data[STX2_INDEX]
    count = data[COUNT_INDEX]
    mode = data[MODE_INDEX]
    crc_hi = data[CRC16_INDEX]
    crc_lo = data[CRC16_INDEX + 1]
    
    # debug
    print("-" * 20)
    print(f"size: {size}")
    print("*" * 20)
    print(f"STX1: {stx1:02x}")
    print(f"STX2: {stx2:02x}")
    print(f"COUNT: {count:02x}")
    print(f"MODE: {mode:02x}")
    print(f"CRC16_HI: {crc_hi:02x}")
    print(f"CRC16_LO: {crc_lo:02x}")
    print("*" * 20)
    print("-" * 20)
    # debug end
    
    # create packet
    send_packet = bytearray(
        [
            STX1,
            STX2,
            count,
            mode,
            crc_hi,
            crc_lo,
        ]
    )
    return send_packet
    

def echo_server(host=HOST, port=PORT):
    '''エコーサーバーを起動する関数
    Args:
        host (str): ホスト名またはIPアドレス
        port (int): ポート番号
    '''
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
                            data_array = bytearray(data)
                            send_packet = create_send_packet(data_array)
                            conn.sendall(send_packet)
                            
                            
                            
        except KeyboardInterrupt:
            print("サーバーを停止します")
            return
                        
if __name__ == "__main__":
    echo_server()
