import socket

# Tạo một đối tượng socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến máy chủ tại địa chỉ IP 192.168.1.1 và cổng 1234
s.connect(("192.168.1.1", 1234))

# Gửi dữ liệu
s.sendall(b"Hello, world!")

# Nhận dữ liệu
data = s.recv(1024)

# Đóng kết nối
s.close()