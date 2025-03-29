def init_crc16():
    """
    CRC-16/IBMの初期値を返す
    
    Returns:
        int: CRC-16/IBMの初期値
    """
    return 0x0000

def update_crc16(crc, byte):
    """
    CRC-16/IBMを更新
    
    Args:
        crc (int): 現在のCRC値
        byte (int): 更新するバイト値 (0-255)
    
    Returns:
        int: 更新後のCRC値
    """
    # byteを8ビット分、1ビットずつ処理する
    for _ in range(8):
        mix = (crc ^ byte) & 0x01
        crc >>= 1   # 右シフト
        if mix:
            crc ^= 0xA001  # 生成多項式(反転形)
        byte >>= 1
    return crc

def calc_crc16(data):
    """
    CRC-16/IBMを計算 (入力: バイト列)
    
    Args:
        data (bytes): CRCを計算するデータ
    
    Returns:
        int: CRC-16/IBM値
    """
    crc = init_crc16()
    for byte in data:
        crc = update_crc16(crc, byte)
    return crc  # 最終XOR不要

if __name__ == "__main__":
    # テスト用データ
    test_data = b"123456789"
    result = calc_crc16(test_data)
    print(f"CRC-16/IBM(ARC) for {test_data} => 0x{result:04X}")  
    # 期待値: 0xBB3D (有名な"123456789"のCRC16/IBM)
