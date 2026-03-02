# Spider-Man VR Browser Prototype

## GitHub Pages 404 checklist (exact fix)

If you still see **404** at `https://rodcast141.github.io/spider-man-vr/`, do these in order:

1. Ensure repository name is exactly **spider-man-vr** (same spelling/case in URL path).
2. Ensure the repository is **Public** (free GitHub Pages requires public repos on personal accounts).
3. Push this branch to your repo default branch (`main` for most repos).
4. In **Settings → Pages**, set **Source = GitHub Actions**.
5. In **Actions**, open **Deploy static site to GitHub Pages** and confirm it is green/success.
6. Hard refresh browser (Ctrl+F5) and open:
   - <https://rodcast141.github.io/spider-man-vr/>

If step 5 is missing, the workflow file may not be on the default branch yet.


## GitHub Pages link (fix for 404)

If `https://rodcast141.github.io/spider-man-vr/` shows 404, your Pages site is not deployed yet.

1. Push this repo to GitHub.
2. In **GitHub → Settings → Pages**, set **Source = GitHub Actions**.
3. Go to **Actions** tab and wait for **Deploy static site to GitHub Pages** to finish.
4. Open: <https://rodcast141.github.io/spider-man-vr/>

If it still shows 404:
- Confirm your repo default branch has the latest commit.
- In **Actions**, open the latest "Deploy static site to GitHub Pages" run and verify it succeeded.
- In **Settings → Pages**, ensure it says **"Your site is live"** and points to the Pages URL.


## Auto-detect IP launcher (recommended)

Use the launcher that auto-detects your computer's local IP and prints the exact Quest link:

```bash
python3 start-quest.py
```

It prints something like:

- `http://192.168.1.24:4173`

Then open that URL in Meta Quest browser.

### Optional flags

```bash
python3 start-quest.py --port 4173
python3 start-quest.py --ip 192.168.1.24
python3 start-quest.py --dry-run
```

## Shell shortcut (macOS/Linux)

```bash
./start-quest.sh
```

## Manual fallback

```bash
python3 -m http.server 4173 --bind 0.0.0.0
```

Then use this format in Quest:

- `http://<YOUR_COMPUTER_LOCAL_IP>:4173`

## Fix `ERR_ADDRESS_UNREACHABLE`

- Quest and computer must be on the **same Wi-Fi**.
- VPN should be off (or same route) on both devices.
- Firewall must allow inbound TCP on your chosen port (default `4173`).
- Use your computer IP (not `localhost`, not headset IP).

## Browser gameplay

- Move Spider-Man with WASD/Arrow keys.
- Touch mission markers (`!`, `X`, `⚡`) to complete stealth, regular, and boss encounters.
- Defeat all 4 bosses to unlock replay/free enemy-boss mode.
