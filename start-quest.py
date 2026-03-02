#!/usr/bin/env python3
"""Cross-platform launcher for Spider-Man VR browser prototype.

Auto-detects a LAN IP, prints the Quest URL, and starts a local HTTP server.
"""

from __future__ import annotations

import argparse
import ipaddress
import socket
import subprocess
import sys
from typing import Iterable


def detect_ip_candidates() -> list[str]:
    candidates: list[str] = []

    # Best-effort route-based local IP discovery (works without external connectivity).
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("1.1.1.1", 80))
        candidates.append(sock.getsockname()[0])
    except OSError:
        pass
    finally:
        sock.close()

    # Hostname lookup fallback.
    try:
        _, _, addrs = socket.gethostbyname_ex(socket.gethostname())
        candidates.extend(addrs)
    except OSError:
        pass

    # Remove duplicates and non-LAN/loopback addresses.
    unique: list[str] = []
    for raw in candidates:
        try:
            ip = ipaddress.ip_address(raw)
        except ValueError:
            continue
        if ip.version != 4 or ip.is_loopback:
            continue
        if raw not in unique:
            unique.append(raw)
    return unique


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Start Quest-accessible local server")
    parser.add_argument("--port", type=int, default=4173, help="Port to bind (default: 4173)")
    parser.add_argument(
        "--ip",
        default=None,
        help="Override auto-detected local IP (useful on multi-network machines)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print detected URL; do not start server",
    )
    return parser


def main(argv: Iterable[str]) -> int:
    args = build_parser().parse_args(list(argv))

    local_ip = args.ip
    if not local_ip:
        candidates = detect_ip_candidates()
        if not candidates:
            print("Could not auto-detect a non-loopback local IP.", file=sys.stderr)
            print("Run manually: python3 -m http.server 4173 --bind 0.0.0.0", file=sys.stderr)
            return 1
        local_ip = candidates[0]

    url = f"http://{local_ip}:{args.port}"
    print("Starting Spider-Man VR browser prototype...")
    print(f"Open on Meta Quest: {url}")
    print("If unreachable: use same Wi-Fi and allow firewall inbound on this port.")

    if args.dry_run:
        return 0

    cmd = [sys.executable, "-m", "http.server", str(args.port), "--bind", "0.0.0.0"]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
