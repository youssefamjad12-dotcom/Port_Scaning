import socket
import errno


def TCP_Scan(ip_addr, port_num):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # تحديد Timeout لمدة ثانية
        s.settimeout(1)

        # محاولة الاتصال
        result = s.connect_ex((ip_addr, port_num))

        if result == 0:
            print(f"[+] Port {port_num} is OPEN")
        else:
            print(f"[-] Port {port_num} is CLOSED")

        # إغلاق الـ Socket

    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close


def UDP_Scan(ip_addr, port_num):
    dns_query = (
        b"\x12\x34"  # Transaction ID
        b"\x01\x00"  # Standard query
        b"\x00\x01"  # Questions
        b"\x00\x00"
        b"\x00\x00"
        b"\x00\x00"
        b"\x07example"
        b"\x03com"
        b"\x00"
        b"\x00\x01"  # Type A
        b"\x00\x01"  # Class IN
    )
    try:
        s = None
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # تحديد Timeout لمدة ثانية
        s.settimeout(1)

        # محاولة الاتصال
        s.sendto(
            (dns_query), (ip_addr, port_num)
        )  # send small packet and wait responce

        try:
            data, addr = s.recvfrom(1024)
            print(f"[+] port {port_num} is OPEN & data = {data} & address = {addr}")
        except socket.timeout:
            print(f"[?] port {port_num} is OPEN | FILTERED")
        except ConnectionRefusedError:
            print(f"[-] port {port_num} is Closed")

    except OSError as e:
        if e.errno == errno.ECONNREFUSED:
            print(f"[-] Port {port_num} is CLOSED")
        else:
            print(f"Error: {e}")

    finally:
        if s is not None:
            s.close()
