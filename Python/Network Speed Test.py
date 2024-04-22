import socket
import time

def test_speed(port, duration):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', port))

    data = b'1' * 1024  # 1KB of data
    total_bytes_sent = 0

    start_time = time.time()
    while time.time() - start_time < duration:
        client_socket.send(data)
        total_bytes_sent += len(data)
        client_socket.recv(1024)  # Receive response from server

    end_time = time.time()

    client_socket.close()
    server_socket.close()

    # Calculate network speed
    elapsed_time = end_time - start_time
    speed = total_bytes_sent / elapsed_time  # bytes per second
    speed_mbps = speed / (1024 * 1024)  # convert to megabits per second

    print("Network Speed: {:.2f} Mbps".format(speed_mbps))

if __name__ == "__main__":
    PORT = 12345
    DURATION = 5
    test_speed(PORT, DURATION)
