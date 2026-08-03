from CTFd import create_app
from CTFd.models import db, Pages

app = create_app()
with app.app_context():
    p = Pages.query.filter_by(route='index').first()
    if not p:
        p = Pages(title="ROOTFORCE CTF", route="index", auth_required=False)
        db.session.add(p)

    p.title = "ROOTFORCE CTF PLATFORM"
    p.content = """
<canvas id="cyber-canvas"></canvas>

<div class="rf-hero-container text-center">

    <!-- Status Pill -->
    <div class="mb-4">
        <div class="rf-badge-pill">
            <span class="rf-badge-dot"></span>
            <span>SYSTEM ONLINE // CTF PHASE II LIVE</span>
        </div>
    </div>

    <!-- Hero Logo -->
    <div class="rf-hero-logo-wrapper">
        <img src="/themes/core/static/img/rootforce_logo.png" alt="ROOTFORCE CTF Logo" class="rf-hero-logo">
    </div>

    <!-- Title & Subtitle -->
    <h1 class="rf-hero-title">ROOTFORCE CTF</h1>
    <div class="rf-hero-subtitle mb-4">THE ULTIMATE CYBERSECURITY COMPETITION ARENA</div>

    <p class="rf-hero-desc mx-auto mb-5">
        Test and elevate your cybersecurity capabilities across web exploitation, cryptography, reverse engineering, forensics, binary exploitation, and OSINT. Compete against elite security researchers worldwide.
    </p>

    <!-- Action Buttons -->
    <div class="rf-btn-group mb-5">
        <a href="/challenges" class="rf-btn rf-btn-primary">
            <i class="fas fa-crosshairs"></i> ENTER ARENA
        </a>
        <a href="/scoreboard" class="rf-btn rf-btn-secondary">
            <i class="fas fa-trophy"></i> LEADERBOARD
        </a>
        <a href="/register" class="rf-btn rf-btn-outline">
            <i class="fas fa-user-plus"></i> REGISTER TEAM
        </a>
    </div>

    <!-- Metric Stat Cards -->
    <div class="row g-4 mb-5 text-start">
        <div class="col-6 col-md-3">
            <div class="rf-card-glass">
                <div class="rf-stat-icon"><i class="fas fa-layer-group"></i></div>
                <div class="rf-stat-number">6 DOMAINS</div>
                <div class="rf-stat-label">Exploitation Modules</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="rf-card-glass">
                <div class="rf-stat-icon"><i class="fas fa-bolt"></i></div>
                <div class="rf-stat-number">REAL-TIME</div>
                <div class="rf-stat-label">Dynamic Flag Scoring</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="rf-card-glass">
                <div class="rf-stat-icon"><i class="fas fa-shield-alt"></i></div>
                <div class="rf-stat-number">ISOLATED</div>
                <div class="rf-stat-label">Dockerized Targets</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="rf-card-glass">
                <div class="rf-stat-icon"><i class="fas fa-medal"></i></div>
                <div class="rf-stat-number">GLOBAL</div>
                <div class="rf-stat-label">Live Team Scoreboard</div>
            </div>
        </div>
    </div>

    <!-- Category Showcase Grid -->
    <div class="mb-5">
        <h3 class="font-heading fw-bold text-white mb-4 text-start">
            <i class="fas fa-terminal me-2 text-cyan"></i>COMPETITION DOMAINS
        </h3>
        <div class="row g-4">
            <!-- Web -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-globe"></i></div>
                        <h4 class="rf-cat-title">WEB EXPLOITATION</h4>
                    </div>
                    <p class="text-muted small">Analyze web applications to uncover SQL injections, XSS, SSRF, authentication bypasses, and RCE vulnerabilities.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">SQLi</span>
                        <span class="rf-tag">XSS</span>
                        <span class="rf-tag">SSRF</span>
                        <span class="rf-tag">JWT</span>
                    </div>
                </div>
            </div>
            <!-- Crypto -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-key"></i></div>
                        <h4 class="rf-cat-title">CRYPTOGRAPHY</h4>
                    </div>
                    <p class="text-muted small">Break mathematical ciphers, exploit weak RSA keys, analyze ECC implementations, and crack hashing algorithms.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">RSA</span>
                        <span class="rf-tag">AES</span>
                        <span class="rf-tag">ECC</span>
                        <span class="rf-tag">ZKP</span>
                    </div>
                </div>
            </div>
            <!-- Reverse -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-microchip"></i></div>
                        <h4 class="rf-cat-title">REVERSE ENGINEERING</h4>
                    </div>
                    <p class="text-muted small">Decompile binaries, dissect obfuscated code, reverse assembly logic using Ghidra, IDA Pro, and GDB.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">x86/x64</span>
                        <span class="rf-tag">Ghidra</span>
                        <span class="rf-tag">ARM</span>
                        <span class="rf-tag">Malware</span>
                    </div>
                </div>
            </div>
            <!-- Forensics -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-search"></i></div>
                        <h4 class="rf-cat-title">FORENSICS & PCAP</h4>
                    </div>
                    <p class="text-muted small">Inspect network packet captures, analyze disk images, extract hidden data in steganography, and dissect memory dumps.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">Wireshark</span>
                        <span class="rf-tag">Volatility</span>
                        <span class="rf-tag">PCAP</span>
                    </div>
                </div>
            </div>
            <!-- Pwn -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-bug"></i></div>
                        <h4 class="rf-cat-title">BINARY EXPLOITATION</h4>
                    </div>
                    <p class="text-muted small">Exploit memory safety vulnerabilities including stack buffer overflows, ROP chains, format strings, and heap exploitation.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">ROP</span>
                        <span class="rf-tag">Buffer Overflow</span>
                        <span class="rf-tag">Heap</span>
                    </div>
                </div>
            </div>
            <!-- OSINT -->
            <div class="col-md-4">
                <div class="rf-card-glass rf-category-card">
                    <div class="rf-cat-header">
                        <div class="rf-cat-icon"><i class="fas fa-user-secret"></i></div>
                        <h4 class="rf-cat-title">OSINT & RECON</h4>
                    </div>
                    <p class="text-muted small">Gather open source intelligence, perform digital footprinting, trace threat actors, and analyze metadata.</p>
                    <div class="rf-cat-tags">
                        <span class="rf-tag">Recon</span>
                        <span class="rf-tag">Footprinting</span>
                        <span class="rf-tag">Metadata</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Live Terminal Box -->
    <div class="rf-terminal-box mb-5">
        <div class="rf-terminal-header">
            <div class="rf-term-dot red"></div>
            <div class="rf-term-dot yellow"></div>
            <div class="rf-term-dot green"></div>
            <div class="rf-term-title">rootforce@arena:~ (zsh)</div>
        </div>
        <div class="rf-terminal-body">
            <div><span class="rf-term-prompt">rootforce@arena:~$</span> <span class="rf-term-cmd">ctf status --verbose</span></div>
            <div class="rf-term-out">[+] Connecting to RootForce CTF Infrastructure...</div>
            <div class="rf-term-out">[+] Status: <span class="rf-term-success">ALL SYSTEMS OPERATIONAL (100% UPTIME)</span></div>
            <div class="rf-term-out">[+] Target Environment: Isolated Docker Containers</div>
            <div><span class="rf-term-prompt">rootforce@arena:~$</span> <span class="rf-term-cmd">cat /etc/motd</span></div>
            <div class="rf-term-success">"Welcome to RootForce. Hack hard, exploit safely, and conquer the leaderboard!"</div>
        </div>
    </div>

</div>

<script>
(function() {
    // Particle Canvas Animation
    const canvas = document.getElementById('cyber-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
    
    window.addEventListener('resize', function() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });
    
    const particles = [];
    const particleCount = Math.min(Math.floor(width / 18), 70);
    
    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.6,
            vy: (Math.random() - 0.5) * 0.6,
            radius: Math.random() * 2 + 1,
            alpha: Math.random() * 0.5 + 0.2
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, width, height);
        
        for (let i = 0; i < particles.length; i++) {
            const p = particles[i];
            p.x += p.vx;
            p.y += p.vy;
            
            if (p.x < 0 || p.x > width) p.vx *= -1;
            if (p.y < 0 || p.y > height) p.vy *= -1;
            
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 240, 255, ${p.alpha})`;
            ctx.shadowBlur = 10;
            ctx.shadowColor = '#00f0ff';
            ctx.fill();
            
            for (let j = i + 1; j < particles.length; j++) {
                const p2 = particles[j];
                const dx = p.x - p2.x;
                const dy = p.y - p2.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist < 130) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(0, 153, 255, ${0.25 * (1 - dist / 130)})`;
                    ctx.lineWidth = 0.8;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(animate);
    }
    animate();
})();
</script>
"""
    db.session.commit()
    print("SUCCESS: RootForce CTF Index Page updated!")
