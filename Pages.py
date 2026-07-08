# -------------------------------------------------------
#   DGTL-Phone-Connect (Hardcore Cyber Edition with Music)
#   Code by Afridi | Er Aryan Afridi
#   Pages & Routes Module
# -------------------------------------------------------

import os
import json
import shutil
import sys

# Disable __pycache__ creation
sys.dont_write_bytecode = True

from flask import jsonify, send_from_directory, request, render_template_string

class Pages:
    def __init__(self, config, afridi, server):
        self.config = config
        self.afridi = afridi
        self.server = server
    
    def home(self):
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <title>🔴 DGTL-PHØNE-CONNECT || N3UR0L1NK v2.0</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                user-select: none;
            }

            body {
                background: radial-gradient(circle at 20% 30%, #0a0f0a, #000000);
                font-family: 'Share Tech Mono', 'Courier New', 'Fira Code', monospace;
                min-height: 100vh;
                overflow-x: hidden;
                position: relative;
                color: #0f0;
            }

            body::before {
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: repeating-linear-gradient(0deg, 
                    rgba(0, 255, 0, 0.03) 0px, 
                    rgba(0, 255, 0, 0.03) 2px, 
                    transparent 2px, 
                    transparent 6px);
                pointer-events: none;
                z-index: 2;
                animation: scanMove 8s linear infinite;
            }

            @keyframes scanMove {
                0% { transform: translateY(0); }
                100% { transform: translateY(100%); }
            }

            #matrixCanvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 0;
                opacity: 0.2;
                pointer-events: none;
            }

            .container {
                position: relative;
                z-index: 10;
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }

            .cyber-header {
                text-align: center;
                margin-bottom: 40px;
                border-bottom: 2px solid #0f0;
                padding-bottom: 20px;
                position: relative;
                background: rgba(0, 0, 0, 0.6);
                backdrop-filter: blur(3px);
                border-radius: 0 0 20px 20px;
                box-shadow: 0 10px 30px rgba(0, 255, 0, 0.2);
            }

            .glitch-text {
                font-size: 3.2rem;
                font-weight: 900;
                text-transform: uppercase;
                color: #0f0;
                text-shadow: -3px 0 #ff00c1, 3px 0 #00fff9;
                animation: glitch 3s infinite;
                letter-spacing: 8px;
            }

            @keyframes glitch {
                0%, 100% { text-shadow: -2px 0 #ff00c1, 2px 0 #00fff9; transform: skew(0deg);}
                20% { text-shadow: 2px 0 #ff00c1, -2px 0 #00fff9; transform: skew(1deg);}
                40% { text-shadow: -3px 0 #ff00c1, 3px 0 #00fff9; transform: skew(-1deg);}
                60% { text-shadow: 3px 0 #ff00c1, -3px 0 #00fff9; transform: skew(0deg);}
                80% { text-shadow: -1px 0 #ff00c1, 1px 0 #00fff9; transform: skew(2deg);}
            }

            .sub {
                font-size: 0.8rem;
                letter-spacing: 3px;
                color: #8f8;
                background: #000000aa;
                display: inline-block;
                padding: 4px 15px;
                border-radius: 20px;
                backdrop-filter: blur(5px);
            }

            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 50px;
            }

            .stat-card {
                background: rgba(0, 0, 0, 0.75);
                border: 1px solid #0f0;
                border-radius: 8px;
                padding: 20px;
                text-align: center;
                transition: all 0.3s ease;
                backdrop-filter: blur(2px);
                position: relative;
                overflow: hidden;
            }

            .stat-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.1), transparent);
                transition: left 0.5s;
            }

            .stat-card:hover::before {
                left: 100%;
            }

            .stat-card:hover {
                transform: translateY(-8px);
                border-color: #f0f;
                box-shadow: 0 0 20px #0f0, inset 0 0 10px #0f0;
            }

            .stat-card .icon {
                font-size: 2.5rem;
                filter: drop-shadow(0 0 4px #0f0);
            }

            .stat-label {
                font-size: 0.7rem;
                text-transform: uppercase;
                letter-spacing: 3px;
                margin: 10px 0 5px;
                color: #8f8;
            }

            .stat-value {
                font-family: 'Courier New', monospace;
                font-size: 1rem;
                font-weight: bold;
                word-break: break-word;
                color: #0f0;
            }

            .feature-matrix {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 35px;
                margin: 40px 0;
            }

            .hack-btn {
                background: #000000cc;
                border: 2px solid #0f0;
                padding: 35px 30px;
                min-width: 260px;
                text-align: center;
                cursor: pointer;
                transition: 0.3s ease;
                backdrop-filter: blur(8px);
                position: relative;
                border-radius: 12px;
                overflow: hidden;
            }

            .hack-btn::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.2), transparent);
                transition: left 0.5s;
            }

            .hack-btn:hover::before {
                left: 100%;
            }

            .hack-btn .big-icon {
                font-size: 3.8rem;
                display: block;
                margin-bottom: 12px;
            }

            .hack-btn span {
                font-size: 1.6rem;
                font-weight: bold;
                letter-spacing: 2px;
                text-transform: uppercase;
            }

            .hack-btn small {
                display: block;
                font-size: 0.7rem;
                margin-top: 10px;
                color: #8f8;
            }

            .hack-btn:hover {
                background: #0f0;
                color: black;
                box-shadow: 0 0 35px #0f0;
                border-color: white;
                transform: scale(1.02);
            }

            .hack-btn:hover .big-icon {
                filter: drop-shadow(0 0 5px black);
            }

            .terminal-log {
                background: #0a0a0a;
                border-left: 5px solid #0f0;
                padding: 15px;
                margin: 20px 0;
                font-size: 0.75rem;
                font-family: 'Courier New', monospace;
                max-height: 200px;
                overflow-y: auto;
            }

            .terminal-log::-webkit-scrollbar {
                width: 5px;
            }

            .terminal-log::-webkit-scrollbar-track {
                background: #000;
            }

            .terminal-log::-webkit-scrollbar-thumb {
                background: #0f0;
            }

            .footer-hack {
                margin-top: 50px;
                border-top: 1px solid #0f0;
                padding: 20px;
                text-align: center;
                background: #00000099;
                font-size: 0.7rem;
                letter-spacing: 1px;
            }

            .command-line {
                font-family: monospace;
                background: #111;
                display: inline-block;
                padding: 5px 12px;
                border-left: 3px solid #0f0;
            }

            .vol-panel {
                position: fixed;
                bottom: 20px;
                left: 20px;
                background: rgba(0, 0, 0, 0.9);
                border: 1px solid #0f0;
                border-radius: 40px;
                padding: 8px 18px;
                backdrop-filter: blur(12px);
                z-index: 99;
                display: flex;
                gap: 12px;
                align-items: center;
            }

            .vol-panel input {
                background: black;
                width: 110px;
                height: 3px;
                -webkit-appearance: none;
                background: #0f0;
                outline: none;
            }

            .vol-panel input::-webkit-slider-thumb {
                -webkit-appearance: none;
                width: 12px;
                height: 12px;
                background: #fff;
                border-radius: 0;
                cursor: pointer;
                box-shadow: 0 0 5px #0f0;
            }

            .music-toggle {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: rgba(0, 0, 0, 0.9);
                border: 1px solid #0f0;
                border-radius: 40px;
                padding: 8px 18px;
                cursor: pointer;
                z-index: 99;
                backdrop-filter: blur(5px);
                font-weight: bold;
                transition: 0.3s;
                font-family: monospace;
            }

            .music-toggle:hover {
                background: #0f0;
                color: black;
                box-shadow: 0 0 15px #0f0;
            }

            @keyframes pulse {
                0%, 100% { opacity: 0.6; text-shadow: 0 0 2px #0f0; }
                50% { opacity: 1; text-shadow: 0 0 8px #0f0; }
            }

            .blink {
                animation: pulse 1.5s infinite;
            }

            @media (max-width: 760px) {
                .glitch-text { font-size: 1.8rem; letter-spacing: 3px; }
                .hack-btn { padding: 20px; min-width: 200px; }
                .hack-btn .big-icon { font-size: 2.5rem; }
                .hack-btn span { font-size: 1.1rem; }
            }
        </style>
    </head>
    <body>

    <canvas id="matrixCanvas"></canvas>

    <div class="container">
        <div class="cyber-header">
            <div class="glitch-text">DGTL-PHØNE-CONNECT</div>
            <div class="sub">[ N3UR0L1NK v2.0 ] // ROOT://ACCESS_GRANTED</div>
            <div style="margin-top: 15px; font-size: 0.7rem;">🔓 ENCRYPTION: AES-256 | 🧬 FIREWALL: QUANTUM_ACTIVE</div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="icon">⚡</div>
                <div class="stat-label">KERNEL STATUS</div>
                <div class="stat-value">[ HARDENED ]</div>
            </div>
            <div class="stat-card">
                <div class="icon">🕸️</div>
                <div class="stat-label">LOCAL IP</div>
                <div class="stat-value" id="localIpAddr">FETCHING...</div>
            </div>
            <div class="stat-card">
                <div class="icon">🛡️</div>
                <div class="stat-label">THREAT LEVEL</div>
                <div class="stat-value blink">🟢 SECURE</div>
            </div>
        </div>

        <div class="feature-matrix">
            <div class="hack-btn" id="btnDeviceSpecs">
                <div class="big-icon">📡</div>
                <span>DEVICE_SPECS</span>
                <small>> decode hardware fingerprint</small>
            </div>
            <div class="hack-btn" id="btnFileSystem">
                <div class="big-icon">🗂️</div>
                <span>FS_EXPLORER</span>
                <small>> full filesystem access</small>
            </div>
            <div class="hack-btn" id="btnNetworkMap">
                <div class="big-icon">🌐</div>
                <span>NET_MATRIX</span>
                <small>> active connections scan</small>
            </div>
        </div>

        <div class="terminal-log">
            <span style="color:#0f0">$> neural_link --live --verbose</span>
            <div id="syslog"><span style="color:#aaa">[BOOT] NeuroLink daemon v2.0 initialized...</span></div>
        </div>

        <div class="footer-hack">
            <div>🔻 DEVELOPED BY <span style="color:#0f0">ARYAN AFRIDI</span> | DARKNET COLLECTIVE</div>
            <div class="command-line" style="margin-top: 8px;">>_ SERVER: ACTIVE // MANAGER FILE: ONLINE // ENCRYPTED_CHANNEL</div>
        </div>
    </div>

    <audio id="bgAudio" loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" type="audio/mpeg">
    </audio>

    <div class="vol-panel">
        <span style="color:#0f0">🎧 VOL</span>
        <input type="range" id="volumeCtrl" min="0" max="100" value="25">
    </div>
    <div class="music-toggle" id="musicToggleBtn">
        🎵 SYNC_ACTIVE
    </div>

    <script>
        (function() {
            // ========== ENHANCED MATRIX RAIN EFFECT ==========
            const canvas = document.getElementById('matrixCanvas');
            const ctx = canvas.getContext('2d');
            
            let width, height;
            let columns = [];
            let drops = [];
            
            const chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*<>?/\\|{}[]~`";
            const charsArray = chars.split('');
            const colors = ['#0f0', '#0a0', '#0c0', '#0e0', '#0f0', '#0d0'];
            
            function initMatrix() {
                width = window.innerWidth;
                height = window.innerHeight;
                canvas.width = width;
                canvas.height = height;
                columns = Math.floor(width / 25);
                drops = [];
                for(let i = 0; i < columns; i++) {
                    drops[i] = {
                        y: Math.random() * height / 25,
                        speed: 0.5 + Math.random() * 1.5,
                        chars: []
                    };
                }
            }
            
            function drawMatrix() {
                if(!ctx) return;
                ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
                ctx.fillRect(0, 0, width, height);
                ctx.font = "bold 18px 'Courier New', monospace";
                
                for(let i = 0; i < columns; i++) {
                    const char = charsArray[Math.floor(Math.random() * charsArray.length)];
                    const colorIndex = Math.floor(Math.random() * colors.length);
                    ctx.fillStyle = colors[colorIndex];
                    const x = i * 25;
                    const y = drops[i].y * 25;
                    ctx.fillText(char, x, y);
                    
                    if(drops[i].y < 2) {
                        ctx.fillStyle = '#fff';
                        ctx.fillText(char, x, y);
                    }
                    
                    drops[i].y += drops[i].speed;
                    if(drops[i].y * 25 > height && Math.random() > 0.975) {
                        drops[i].y = 0;
                        drops[i].speed = 0.5 + Math.random() * 1.5;
                    }
                }
                requestAnimationFrame(drawMatrix);
            }
            
            window.addEventListener('resize', () => {
                initMatrix();
            });
            
            initMatrix();
            drawMatrix();

            // ========== UPTIME ==========
            let startTime = Date.now();
            function updateUptime() {
                let diff = Math.floor((Date.now() - startTime) / 1000);
                let hrs = Math.floor(diff / 3600);
                let mins = Math.floor((diff % 3600) / 60);
                let secs = diff % 60;
                document.getElementById('uptimeDisplay').innerHTML = hrs.toString().padStart(2,'0') + ':' + mins.toString().padStart(2,'0') + ':' + secs.toString().padStart(2,'0');
            }
            setInterval(updateUptime, 1000);
            
            // ========== IP ==========
            function updateLocalIP() {
                fetch('/api/ip')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('localIpAddr').innerHTML = data.local_ip + ' <span style="color:#aaa;">(secure)</span>';
                    });
            }
            updateLocalIP();
            setInterval(updateLocalIP, 30000);

            // ========== TERMINAL LOGS ==========
            const logDiv = document.getElementById('syslog');
            const logsList = [
                "[✓] Kernel module loaded: neuro_link.so",
                "[⚠️] Intrusion attempt detected → BLOCKED",
                "[✓] Filesystem integrity check: PASSED",
                "[🔥] Firewall rule updated: 12,847 active rules",
                "[🎧] Neural audio handshake: ESTABLISHED",
                "[🧬] NeuroLink heartbeat: OK | Latency: 2ms",
                "[🔑] RSA-4096 key exchange: COMPLETED",
                "[💀] Packet injection defense: ACTIVE",
                "[⚡] CPU governor: performance | 4 cores online",
                "[📡] Secure channel: ESTABLISHED",
                "[🔒] Quantum encryption layer: DEPLOYED",
                "[🎵] Audio stream: SYNCED | Bitrate: 320kbps",
                "[🌐] Network scan: 0 threats detected",
                "[🛡️] Firewall: HARDCORE MODE ACTIVE",
                "[📊] System load: 12% | Memory: 2.4GB/8GB"
            ];
            let logIndex = 0;
            setInterval(() => {
                const newMsg = logsList[logIndex % logsList.length];
                const newDiv = document.createElement('div');
                newDiv.style.color = '#0f0';
                newDiv.style.marginTop = '5px';
                newDiv.innerHTML = '> ' + newMsg;
                logDiv.appendChild(newDiv);
                logDiv.scrollTop = logDiv.scrollHeight;
                if(logDiv.children.length > 12) logDiv.removeChild(logDiv.children[1]);
                logIndex++;
            }, 2800);

            // ========== AUDIO SYSTEM ==========
            const audio = document.getElementById('bgAudio');
            const volumeSlider = document.getElementById('volumeCtrl');
            const toggleBtn = document.getElementById('musicToggleBtn');
            let isPlaying = false;
            
            function setVolume(vol) {
                audio.volume = vol / 100;
            }
            volumeSlider.addEventListener('input', (e) => {
                setVolume(e.target.value);
            });
            
            function startAudio() {
                audio.play().then(() => {
                    isPlaying = true;
                    toggleBtn.innerHTML = "🎵 SYNC_ACTIVE";
                    toggleBtn.style.background = "rgba(0,255,0,0.2)";
                }).catch(err => {
                    toggleBtn.innerHTML = "🔇 CLICK TO PLAY";
                    isPlaying = false;
                });
            }
            
            audio.volume = 0.25;
            startAudio();
            
            toggleBtn.addEventListener('click', () => {
                if(isPlaying) {
                    audio.pause();
                    isPlaying = false;
                    toggleBtn.innerHTML = "⏸️ MUTE_SYNC";
                    toggleBtn.style.background = "#220000";
                } else {
                    audio.play().then(() => {
                        isPlaying = true;
                        toggleBtn.innerHTML = "🎵 SYNC_ACTIVE";
                        toggleBtn.style.background = "rgba(0,255,0,0.2)";
                    }).catch(e => { console.log(e); });
                }
            });
            
            document.body.addEventListener('click', function enableOnce() {
                if(!isPlaying && audio.paused) {
                    audio.play().catch(()=>{});
                }
            }, { once: true });

            // ========== MODALS ==========
            function openDeviceModal() {
                fetch('/api/device_info')
                    .then(response => response.json())
                    .then(data => {
                        const modalHtml = `
                        <div id="hackModal" style="position:fixed; top:0; left:0; width:100%; height:100%; background:#000000ee; backdrop-filter:blur(12px); z-index:1000; display:flex; justify-content:center; align-items:center;">
                            <div style="background:#000; border:2px solid #0f0; max-width:700px; width:90%; padding:25px; border-radius:8px; font-family:monospace; color:#0f0; animation: fadeIn 0.3s ease;">
                                <div style="display:flex; justify-content:space-between; margin-bottom:15px;">
                                    <h2>📟 DEVICE_SCAN.EXE</h2>
                                    <button id="closeModalBtn" style="background:#0f0; color:#000; border:none; padding:5px 15px; cursor:pointer; font-weight:bold;">✖ CLOSE</button>
                                </div>
                                <pre style="background:#0a0a0a; padding:20px; margin:15px 0; overflow:auto; font-size:0.85rem; border-left:3px solid #0f0;">
${data.info}
                                </pre>
                                <div style="font-size:0.7rem; border-top:1px solid #0f0; padding-top:10px;">🔒 Hardware scan complete - SECURE BOOT VERIFIED</div>
                            </div>
                        </div>`;
                        document.body.insertAdjacentHTML('beforeend', modalHtml);
                        document.getElementById('closeModalBtn').addEventListener('click', () => {
                            document.getElementById('hackModal').remove();
                        });
                    });
            }
            
            function openFileExplorerModal() {
                window.open('/files?path=/sdcard', '_blank');
            }
            
            function openNetworkModal() {
                const connections = [
                    "192.168.1.1:443 (GATEWAY) - ESTABLISHED",
                    "34.120.8.23:8080 (CDN) - ESTABLISHED",
                    "172.217.168.46:80 (GOOGLE) - TIME_WAIT",
                    "185.130.5.253:9001 (TOR_NODE) - ENCRYPTED",
                    "10.0.0.2:5353 (mDNS) - CLOSED",
                    "94.140.14.14:53 (DNS) - CONNECTED",
                    "192.168.1.105:54321 (LOCAL) - LISTENING"
                ];
                let connectionsHtml = connections.map(ip => '<div style="border-left:2px solid #0f0; margin:8px 0; padding-left:10px;">🔌 ' + ip + '</div>').join('');
                const modalHtml = `
                <div id="hackModal" style="position:fixed; top:0; left:0; width:100%; height:100%; background:#000000ee; backdrop-filter:blur(12px); z-index:1000; display:flex; justify-content:center; align-items:center;">
                    <div style="background:#000; border:2px solid #0f0; max-width:700px; width:90%; padding:25px; border-radius:8px;">
                        <div style="display:flex; justify-content:space-between;">
                            <h2>🌐 NET_MATRIX // ACTIVE CONNS</h2>
                            <button id="closeModalBtn" style="background:#0f0; color:#000; border:none; padding:5px 15px; cursor:pointer;">X</button>
                        </div>
                        <div style="background:#0a0a0a; margin-top:20px; padding:15px; max-height:400px; overflow-y:auto;">
                            ${connectionsHtml}
                            <div style="margin-top:15px; padding-top:10px; border-top:1px solid #0f0;">
                                <div>> Packets: ${Math.floor(Math.random() * 3000 + 1000)}/s | Dropped: 0</div>
                                <div>> Firewall: QUANTUM_IPSET | Rules: 12,847</div>
                                <div>> Encrypted tunnels: 4 ACTIVE</div>
                                <div>> Bandwidth: ${Math.floor(Math.random() * 50 + 10)} Mbps</div>
                            </div>
                        </div>
                    </div>
                </div>`;
                document.body.insertAdjacentHTML('beforeend', modalHtml);
                document.getElementById('closeModalBtn').addEventListener('click', () => {
                    document.getElementById('hackModal').remove();
                });
            }

            document.getElementById('btnDeviceSpecs').addEventListener('click', openDeviceModal);
            document.getElementById('btnFileSystem').addEventListener('click', openFileExplorerModal);
            document.getElementById('btnNetworkMap').addEventListener('click', openNetworkModal);
            
            // ========== DYNAMIC THREAT LEVEL ==========
            setInterval(() => {
                const threatDiv = document.querySelector('.stat-card:last-child .stat-value');
                if(threatDiv) {
                    const levels = ['🟢 SECURE', '🟢 LOW', '🟡 MONITORING', '🟢 STABLE'];
                    const newLevel = levels[Math.floor(Math.random() * levels.length)];
                    if(Math.random() > 0.65) {
                        threatDiv.innerHTML = newLevel;
                    }
                }
            }, 8000);
            
            console.log("%c╔════════════════════════════════════════╗", "color: #0f0");
            console.log("%c║     DGTL CONNECT // NEURO INTERFACE     ║", "color: #0f0");
            console.log("%c║        v2.0 - HARDCORE EDITION          ║", "color: #0f0");
            console.log("%c╚════════════════════════════════════════╝", "color: #0f0");
            console.log("%c[!] SYSTEM: ONLINE | ENCRYPTION: ACTIVE", "color: #0f0");
            console.log("%c[!] TELEGRAM BOT: CONNECTED", "color: #0f0");
            console.log("%c[!] DEVELOPED BY ARYAN AFRIDI", "color: #ff00ff");
        })();
    </script>
    </body>
    </html>
    """
    
    def api_ip(self):
        return jsonify({
            "local_ip": self.afridi.get_local_ip(),
            "public_url": self.afridi.public_url
        })
    
    def api_device_info(self):
        return jsonify({"info": self.afridi.get_device_info()})
    
    def device(self):
        output = self.afridi.get_device_info()
        return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>[DEVICE_INFO] || DGTL PHONE CONNECT</title>
        <style>
            body {{
                background: #000000;
                color: #00ff00;
                font-family: 'Courier New', monospace;
                padding: 20px;
                margin: 0;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: #000000;
                border: 3px solid #00ff00;
                padding: 40px;
                animation: fadeIn 0.5s ease;
                box-shadow: 0 0 50px rgba(0, 255, 0, 0.2);
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(-20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            pre {{
                background: #0a0a0a;
                padding: 30px;
                overflow-x: auto;
                font-size: 1.1em;
                line-height: 1.6;
                border-left: 4px solid #00ff00;
                color: #00ff00;
                font-family: 'Courier New', monospace;
            }}
            .back-btn {{
                background: #00ff00;
                color: #000000;
                padding: 15px 30px;
                text-decoration: none;
                display: inline-block;
                margin-top: 25px;
                font-weight: bold;
                transition: all 0.3s;
                font-size: 1em;
                border: none;
                cursor: pointer;
                font-family: 'Courier New', monospace;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            .back-btn:hover {{
                background: #ffffff;
                color: #000000;
                box-shadow: 0 0 30px #00ff00;
                transform: scale(1.05);
            }}
            h1 {{
                margin-bottom: 20px;
                font-size: 2em;
                text-align: center;
                text-shadow: 0 0 10px #00ff00;
                letter-spacing: 3px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>>_ DEVICE_SCAN.EXE</h1>
            <pre>{output}</pre>
            <div style="text-align: center;">
                <a href="/" class="back-btn">← RETURN TO DASHBOARD</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    def files(self):
        path = request.args.get("path", "/sdcard")
        
        # Security: Prevent directory traversal attacks
        if '..' in path:
            return "Access Denied", 403
        
        # Get file list with details
        items = []
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                info = self.afridi.get_file_info(full_path)
                if info:
                    items.append(info)
            
            # Sort: directories first, then files
            items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
            
        except PermissionError:
            items = []
        except Exception as e:
            items = []
        
        html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[FILE_BROWSER] || DGTL PHONE CONNECT</title>
        <style>
            body {{
                background: #000000;
                color: #00ff00;
                font-family: 'Courier New', monospace;
                padding: 20px;
                margin: 0;
            }}
            .container {{
                max-width: 1400px;
                margin: 0 auto;
                background: #000000;
                border: 3px solid #00ff00;
                padding: 30px;
                animation: fadeIn 0.5s ease;
                box-shadow: 0 0 50px rgba(0, 255, 0, 0.2);
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(-20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            .path-bar {{
                background: #0a0a0a;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #00ff00;
                word-break: break-all;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
            }}
            .path-bar span {{
                color: #00ff00;
                font-size: 0.9em;
            }}
            .path-bar .path-text {{
                font-size: 0.8em;
                color: #00ff00;
            }}
            .file-list {{
                background: #0a0a0a;
                padding: 15px;
                margin: 20px 0;
                max-height: 600px;
                overflow-y: auto;
                border: 1px solid #00ff00;
            }}
            .file-item {{
                padding: 10px 15px;
                margin: 5px 0;
                border-bottom: 1px solid #003300;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: all 0.3s ease;
            }}
            .file-item:hover {{
                background: #003300;
                padding-left: 25px;
            }}
            .file-item .file-name {{
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .file-item .file-name a {{
                color: #00ff00;
                text-decoration: none;
                font-size: 0.95em;
            }}
            .file-item .file-name a:hover {{
                text-decoration: underline;
            }}
            .file-item .file-info {{
                display: flex;
                gap: 20px;
                font-size: 0.75em;
                color: #668866;
                align-items: center;
            }}
            .file-item .file-actions {{
                display: flex;
                gap: 10px;
            }}
            .file-item .file-actions button {{
                background: transparent;
                border: 1px solid #00ff00;
                color: #00ff00;
                padding: 3px 10px;
                cursor: pointer;
                font-family: 'Courier New', monospace;
                font-size: 0.7em;
                transition: all 0.3s;
            }}
            .file-item .file-actions button:hover {{
                background: #00ff00;
                color: #000;
            }}
            .file-item .file-actions .delete-btn {{
                border-color: #ff0000;
                color: #ff0000;
            }}
            .file-item .file-actions .delete-btn:hover {{
                background: #ff0000;
                color: #fff;
            }}
            .file-item .file-actions .zip-btn {{
                border-color: #ffaa00;
                color: #ffaa00;
            }}
            .file-item .file-actions .zip-btn:hover {{
                background: #ffaa00;
                color: #000;
            }}
            .file-item .icon {{
                font-size: 1.2em;
            }}
            .controls {{
                display: flex;
                gap: 15px;
                margin: 20px 0;
                flex-wrap: wrap;
            }}
            .controls input, .controls button {{
                background: #000;
                border: 1px solid #00ff00;
                color: #00ff00;
                padding: 10px 15px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}
            .controls input {{
                flex: 1;
                min-width: 200px;
            }}
            .controls button {{
                cursor: pointer;
                transition: all 0.3s;
            }}
            .controls button:hover {{
                background: #00ff00;
                color: #000;
            }}
            .back-btn {{
                background: #00ff00;
                color: #000000;
                padding: 12px 25px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s;
                font-family: 'Courier New', monospace;
                text-transform: uppercase;
                letter-spacing: 2px;
                display: inline-block;
            }}
            .back-btn:hover {{
                background: #ffffff;
                box-shadow: 0 0 30px #00ff00;
                transform: scale(1.05);
            }}
            .upload-area {{
                border: 2px dashed #00ff00;
                padding: 30px;
                text-align: center;
                margin: 20px 0;
                cursor: pointer;
                transition: all 0.3s;
            }}
            .upload-area:hover {{
                background: #003300;
            }}
            .upload-area input[type="file"] {{
                display: none;
            }}
            .modal {{
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.9);
                z-index: 999;
                justify-content: center;
                align-items: center;
            }}
            .modal.active {{
                display: flex;
            }}
            .modal-content {{
                background: #000;
                border: 2px solid #00ff00;
                padding: 30px;
                max-width: 800px;
                width: 90%;
                max-height: 90vh;
                overflow-y: auto;
                position: relative;
            }}
            .modal-close {{
                position: absolute;
                top: 10px;
                right: 15px;
                background: none;
                border: none;
                color: #00ff00;
                font-size: 1.5em;
                cursor: pointer;
            }}
            .preview-text {{
                background: #0a0a0a;
                padding: 15px;
                margin: 10px 0;
                white-space: pre-wrap;
                font-size: 0.85em;
                max-height: 500px;
                overflow-y: auto;
            }}
            .preview-image {{
                max-width: 100%;
                max-height: 500px;
            }}
            .preview-audio, .preview-video {{
                width: 100%;
                max-height: 400px;
            }}
            .zip-modal input {{
                background: #000;
                border: 1px solid #00ff00;
                color: #00ff00;
                padding: 8px 12px;
                width: 100%;
                margin: 5px 0;
            }}
            .zip-modal button {{
                background: #00ff00;
                color: #000;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                margin-top: 10px;
            }}
            .zip-modal .password-hint {{
                color: #668866;
                font-size: 0.7em;
                margin-top: 5px;
            }}
            ::-webkit-scrollbar {{
                width: 10px;
            }}
            ::-webkit-scrollbar-track {{
                background: #000000;
            }}
            ::-webkit-scrollbar-thumb {{
                background: #00ff00;
            }}
            @media (max-width: 760px) {{
                .file-item {{
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 8px;
                }}
                .file-item .file-info {{
                    flex-wrap: wrap;
                }}
                .container {{ padding: 15px; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>>_ FILE_BROWSER.EXE</h1>
            
            <div class="path-bar">
                <span>📁 <span class="path-text">{path}</span></span>
                <span>📊 {len(items)} items</span>
            </div>
            
            <div class="controls">
                <input type="text" id="pathInput" value="{path}" placeholder="Enter path...">
                <button onclick="navigateToPath()">📂 GO</button>
                <button onclick="location.href='/'">🏠 HOME</button>
                <button onclick="location.href='/files?path=' + encodeURIComponent('{os.path.dirname(path)}')">⬆ UP</button>
            </div>
            
            <div class="upload-area" onclick="document.getElementById('fileUpload').click()">
                📤 <strong>CLICK OR DRAG</strong> to upload files
                <input type="file" id="fileUpload" multiple onchange="uploadFiles(event)" />
                <div style="font-size:0.7em; color:#668866; margin-top:5px;">Max size: 100MB per file</div>
            </div>
            
            <div class="file-list">
        """
        
        if items:
            parent = os.path.dirname(path)
            if path != '/':
                html += f"""
                <div class="file-item">
                    <div class="file-name">
                        <span class="icon">📂</span>
                        <a href="/files?path={parent}">..</a>
                    </div>
                    <div class="file-info">
                        <span>PARENT</span>
                    </div>
                </div>
                """
            
            for item in items[:500]:  # Limit to 500 items for performance
                icon = "📁" if item['is_dir'] else "📄"
                if item.get('ext') in ['.mp3', '.wav', '.m4a']:
                    icon = "🎵"
                elif item.get('ext') in ['.mp4', '.mkv', '.avi']:
                    icon = "🎬"
                elif item.get('ext') in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    icon = "🖼️"
                elif item.get('ext') in ['.pdf']:
                    icon = "📕"
                elif item.get('ext') in ['.apk']:
                    icon = "📦"
                elif item.get('ext') in ['.txt', '.md', '.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.json', '.xml']:
                    icon = "📝"
                elif item.get('ext') in ['.zip', '.rar', '.7z']:
                    icon = "🗜️"
                
                # Escape for HTML
                name = item['name'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                full_path = item['path'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                
                if item['is_dir']:
                    html += f"""
                    <div class="file-item">
                        <div class="file-name">
                            <span class="icon">{icon}</span>
                            <a href="/files?path={full_path}">{name}</a>
                        </div>
                        <div class="file-info">
                            <span>{item['modified']}</span>
                            <span>📁</span>
                        </div>
                        <div class="file-actions">
                            <button class="delete-btn" onclick="deleteItem('{full_path}')">🗑️</button>
                        </div>
                    </div>
                    """
                else:
                    html += f"""
                    <div class="file-item">
                        <div class="file-name">
                            <span class="icon">{icon}</span>
                            <a href="#" onclick="previewFile('{full_path}')" title="Click to preview">{name}</a>
                        </div>
                        <div class="file-info">
                            <span>{item['size_human']}</span>
                            <span>{item['modified']}</span>
                        </div>
                        <div class="file-actions">
                            <button onclick="previewFile('{full_path}')">👁️</button>
                            <button class="zip-btn" onclick="zipFile('{full_path}')">🗜️</button>
                            <button class="delete-btn" onclick="deleteItem('{full_path}')">🗑️</button>
                        </div>
                    </div>
                    """
        else:
            html += '<div style="padding:20px; text-align:center; color:#668866;">📭 No files found or access denied</div>'
        
        html += f"""
            </div>
            
            <div style="display:flex; gap:15px; flex-wrap:wrap; margin:20px 0;">
                <a href="/" class="back-btn">← RETURN TO DASHBOARD</a>
                <button onclick="refreshPage()" class="back-btn" style="background:#003300; color:#00ff00;">🔄 REFRESH</button>
            </div>
        </div>
        
        <!-- Preview Modal -->
        <div class="modal" id="previewModal">
            <div class="modal-content">
                <button class="modal-close" onclick="closeModal()">✖</button>
                <h3 id="previewTitle">File Preview</h3>
                <div id="previewContent"></div>
            </div>
        </div>
        
        <!-- ZIP Modal -->
        <div class="modal" id="zipModal">
            <div class="modal-content zip-modal">
                <button class="modal-close" onclick="closeZipModal()">✖</button>
                <h3>🗜️ Create Password Protected ZIP</h3>
                <p style="color:#668866; font-size:0.8em;">Selected: <span id="zipFileName">None</span></p>
                <input type="text" id="zipPassword" placeholder="Enter password for ZIP" />
                <div class="password-hint">🔒 Password required - ZIP file will ask for this password when opened</div>
                <input type="text" id="zipOutputName" placeholder="Output zip name (optional)" />
                <button onclick="createZip()">📦 CREATE ENCRYPTED ZIP</button>
                <div id="zipStatus" style="margin-top:10px; color:#ffaa00;"></div>
            </div>
        </div>
        
        <script>
        let currentPath = '{path}';
        let zipTarget = '';
        
        function navigateToPath() {{
            const p = document.getElementById('pathInput').value;
            if(p) location.href = '/files?path=' + encodeURIComponent(p);
        }}
        
        function refreshPage() {{
            location.reload();
        }}
        
        // ========== FILE UPLOAD ==========
        function uploadFiles(event) {{
            const files = event.target.files;
            const formData = new FormData();
            formData.append('path', currentPath);
            for(let i = 0; i < files.length; i++) {{
                formData.append('files[]', files[i]);
            }}
            
            const status = document.createElement('div');
            status.style.cssText = 'color:#ffaa00; padding:10px; text-align:center;';
            status.textContent = '📤 Uploading ' + files.length + ' files...';
            document.querySelector('.upload-area').after(status);
            
            fetch('/api/upload', {{
                method: 'POST',
                body: formData
            }})
            .then(res => res.json())
            .then(data => {{
                status.textContent = data.message;
                status.style.color = data.success ? '#00ff00' : '#ff0000';
                if(data.success) {{
                    setTimeout(() => location.reload(), 1500);
                }}
            }})
            .catch(err => {{
                status.textContent = '❌ Upload failed: ' + err;
                status.style.color = '#ff0000';
            }});
            
            document.getElementById('fileUpload').value = '';
        }}
        
        // ========== FILE PREVIEW ==========
        function previewFile(path) {{
            const modal = document.getElementById('previewModal');
            const content = document.getElementById('previewContent');
            const title = document.getElementById('previewTitle');
            
            modal.classList.add('active');
            title.textContent = '📄 ' + path.split('/').pop();
            content.innerHTML = '<div style="text-align:center; color:#668866;">⏳ Loading...</div>';
            
            fetch('/api/preview?path=' + encodeURIComponent(path))
                .then(res => res.json())
                .then(data => {{
                    if(data.error) {{
                        content.innerHTML = '<div style="color:#ff0000;">❌ ' + data.error + '</div>';
                        return;
                    }}
                    
                    if(data.type === 'text') {{
                        let displayContent = data.content || 'Empty file';
                        content.innerHTML = `
                            <div style="background:#0a0a0a; padding:15px; margin:10px 0; white-space:pre-wrap; font-size:0.85em; max-height:500px; overflow-y:auto; border-left:3px solid #00ff00;">
                                ` + displayContent + `
                            </div>
                            <div style="font-size:0.7em; color:#668866;">📊 ` + (data.line_count || 0) + ` lines</div>
                        `;
                    }} else if(data.type === 'image') {{
                        content.innerHTML = `
                            <div style="text-align:center; margin:10px 0;">
                                <img src="/api/preview?path=` + encodeURIComponent(path) + `&raw=1" class="preview-image" />
                            </div>
                            <div style="font-size:0.7em; color:#668866; text-align:center;">📐 ` + (data.width||'?') + `x` + (data.height||'?') + `</div>
                        `;
                    }} else if(data.type === 'audio') {{
                        content.innerHTML = `
                            <div style="margin:20px 0; text-align:center;">
                                <audio controls class="preview-audio">
                                    <source src="/api/preview?path=` + encodeURIComponent(path) + `&raw=1" type="` + (data.mime || 'audio/mpeg') + `" />
                                </audio>
                            </div>
                            <div style="font-size:0.7em; color:#668866; text-align:center;">🎵 ` + data.name + `</div>
                        `;
                    }} else if(data.type === 'video') {{
                        content.innerHTML = `
                            <div style="margin:20px 0; text-align:center;">
                                <video controls class="preview-video">
                                    <source src="/api/preview?path=` + encodeURIComponent(path) + `&raw=1" type="` + (data.mime || 'video/mp4') + `" />
                                </video>
                            </div>
                            <div style="font-size:0.7em; color:#668866; text-align:center;">🎬 ` + data.name + `</div>
                        `;
                    }} else {{
                        content.innerHTML = `
                            <div style="margin:20px 0; text-align:center; color:#668866;">
                                <div style="font-size:4em;">📄</div>
                                <p>` + data.name + `</p>
                                <p style="font-size:0.8em;">` + data.size_human + `</p>
                                <p style="font-size:0.7em;">Type: ` + data.mime + `</p>
                                <a href="/download?path=` + encodeURIComponent(path) + `" style="color:#00ff00; border:1px solid #00ff00; padding:10px 20px; text-decoration:none; display:inline-block; margin-top:10px;">
                                    ⬇️ DOWNLOAD
                                </a>
                            </div>
                        `;
                    }}
                }})
                .catch(err => {{
                    content.innerHTML = '<div style="color:#ff0000;">❌ Error: ' + err + '</div>';
                }});
        }}
        
        function closeModal() {{
            document.getElementById('previewModal').classList.remove('active');
        }}
        
        // ========== DELETE ==========
        function deleteItem(path) {{
            if(!confirm('⚠️ Delete this item?\\n\\n' + path)) return;
            
            fetch('/api/delete', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ path: path }})
            }})
            .then(res => res.json())
            .then(data => {{
                alert(data.message);
                if(data.success) location.reload();
            }});
        }}
        
        // ========== ZIP ==========
        function zipFile(path) {{
            zipTarget = path;
            document.getElementById('zipFileName').textContent = path.split('/').pop();
            document.getElementById('zipModal').classList.add('active');
        }}
        
        function closeZipModal() {{
            document.getElementById('zipModal').classList.remove('active');
        }}
        
        function createZip() {{
            const password = document.getElementById('zipPassword').value;
            if(!password) {{
                alert('⚠️ Please enter a password for the ZIP file!');
                document.getElementById('zipPassword').focus();
                return;
            }}
            
            let outputName = document.getElementById('zipOutputName').value.trim();
            if(!outputName) {{
                const base = zipTarget.split('/').pop();
                outputName = base + '.zip';
            }}
            
            const status = document.getElementById('zipStatus');
            status.textContent = '⏳ Creating encrypted ZIP...';
            status.style.color = '#ffaa00';
            
            fetch('/api/zip', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{
                    paths: [zipTarget],
                    output: outputName,
                    password: password
                }})
            }})
            .then(res => res.json())
            .then(data => {{
                status.textContent = data.message;
                status.style.color = data.success ? '#00ff00' : '#ff0000';
                if(data.success) {{
                    setTimeout(() => {{
                        closeZipModal();
                        location.reload();
                    }}, 2000);
                }}
            }});
        }}
        
        // ========== KEYBOARD SHORTCUTS ==========
        document.addEventListener('keydown', (e) => {{
            if(e.key === 'Escape') {{
                closeModal();
                closeZipModal();
            }}
            if(e.key === 'Enter' && document.activeElement === document.getElementById('pathInput')) {{
                navigateToPath();
            }}
        }});
        
        // Close modal on background click
        document.getElementById('previewModal').addEventListener('click', function(e) {{
            if(e.target === this) closeModal();
        }});
        document.getElementById('zipModal').addEventListener('click', function(e) {{
            if(e.target === this) closeZipModal();
        }});
        </script>
    </body>
    </html>
        """
        return html
    
    def preview(self):
        path = request.args.get("path")
        raw = request.args.get("raw") == "1"
        
        if not path or not os.path.exists(path):
            return jsonify({"error": "File not found"}), 404
        
        if os.path.isdir(path):
            return jsonify({"error": "Cannot preview directory"}), 400
        
        info = self.afridi.get_file_info(path)
        if not info:
            return jsonify({"error": "Cannot read file info"}), 400
        
        if raw:
            return send_from_directory(os.path.dirname(path), os.path.basename(path))
        
        # Check file type
        ext = info.get('ext', '').lower()
        
        if self.afridi.is_text_file(path):
            try:
                content = self.afridi.read_text_file(path)
                return jsonify({
                    "type": "text",
                    "content": content,
                    "line_count": len(content.split('\n')),
                    "name": info['name'],
                    "size_human": info['size_human']
                })
            except:
                return jsonify({"error": "Cannot read text file"}), 400
        
        elif self.afridi.is_image_file(path):
            try:
                from PIL import Image
                img = Image.open(path)
                return jsonify({
                    "type": "image",
                    "name": info['name'],
                    "size_human": info['size_human'],
                    "mime": info['mime'],
                    "width": img.width,
                    "height": img.height
                })
            except:
                return jsonify({
                    "type": "image",
                    "name": info['name'],
                    "size_human": info['size_human'],
                    "mime": info['mime']
                })
        
        elif self.afridi.is_audio_file(path):
            return jsonify({
                "type": "audio",
                "name": info['name'],
                "size_human": info['size_human'],
                "mime": info['mime']
            })
        
        elif self.afridi.is_video_file(path):
            return jsonify({
                "type": "video",
                "name": info['name'],
                "size_human": info['size_human'],
                "mime": info['mime']
            })
        
        else:
            return jsonify({
                "type": "binary",
                "name": info['name'],
                "size_human": info['size_human'],
                "mime": info['mime']
            })
    
    def upload(self):
        path = request.form.get("path", "/sdcard")
        files = request.files.getlist("files[]")
        
        if not files:
            return jsonify({"success": False, "message": "No files uploaded"})
        
        uploaded = 0
        for file in files:
            if file.filename:
                # Security: Prevent directory traversal
                filename = os.path.basename(file.filename)
                save_path = os.path.join(path, filename)
                
                # Check if file exists
                counter = 1
                while os.path.exists(save_path):
                    name, ext = os.path.splitext(filename)
                    save_path = os.path.join(path, f"{name}_{counter}{ext}")
                    counter += 1
                
                try:
                    file.save(save_path)
                    uploaded += 1
                except Exception as e:
                    return jsonify({"success": False, "message": f"Error uploading {filename}: {str(e)}"})
        
        return jsonify({
            "success": True,
            "message": f"✅ Uploaded {uploaded} file(s) to {path}"
        })
    
    def delete(self):
        data = request.get_json()
        path = data.get("path")
        
        if not path or not os.path.exists(path):
            return jsonify({"success": False, "message": "File not found"})
        
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
                return jsonify({"success": True, "message": f"✅ Deleted directory: {path}"})
            else:
                os.remove(path)
                return jsonify({"success": True, "message": f"✅ Deleted file: {path}"})
        except Exception as e:
            return jsonify({"success": False, "message": f"❌ Error: {str(e)}"})
    
    def zip_create(self):
        data = request.get_json()
        paths = data.get("paths", [])
        output_name = data.get("output", "archive.zip")
        password = data.get("password", "")
        
        if not paths:
            return jsonify({"success": False, "message": "No files selected"})
        
        # Password is required
        if not password or not password.strip():
            return jsonify({"success": False, "message": "❌ Password is required for encrypted ZIP!"})
        
        # Create zip in the same directory as the first file
        base_dir = os.path.dirname(paths[0]) if paths else "/sdcard"
        zip_path = os.path.join(base_dir, output_name)
        
        # Ensure unique name
        counter = 1
        while os.path.exists(zip_path):
            name, ext = os.path.splitext(output_name)
            zip_path = os.path.join(base_dir, f"{name}_{counter}{ext}")
            counter += 1
        
        # Create password protected zip
        success, message = self.afridi.create_password_zip(paths, zip_path, password)
        
        return jsonify({
            "success": success,
            "message": message,
            "zip_path": zip_path if success else None
        })
    
    def download(self):
        path = request.args.get("path")
        if not path or not os.path.exists(path):
            return "File not found", 404
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        return send_from_directory(directory, filename, as_attachment=True)