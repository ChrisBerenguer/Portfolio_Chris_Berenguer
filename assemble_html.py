import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('timeline.html', 'r', encoding='utf-8') as f:
    timeline_html = f.read()

# 1. Inject IntersectionObserver script
head_js = """    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: "0px 0px -10px 0px" });

            document.querySelectorAll('.animate-on-scroll').forEach((el) => {
                el.style.animationPlayState = 'paused';
                observer.observe(el);
            });
        });
    </script>
</head>"""

if 'IntersectionObserver' not in content:
    content = content.replace('</head>', head_js)


# 2. Inject Section 2
section_2 = f"""    <!-- Second Section (Video & Timeline) -->
    <section class="relative z-10 w-full pb-32 mt-20">
        
        <!-- Video Container -->
        <div class="max-w-[1000px] mx-auto px-6 mb-40 z-20 relative animate-on-scroll [animation:fadeInUpBlur_1s_cubic-bezier(0.2,0.8,0.2,1)_both]">
            <!-- Glowing background aura for the video -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-[120%] bg-brand-500/10 blur-[80px] rounded-full -z-10"></div>
            
            <div class="relative w-full aspect-video bg-neutral-900 rounded-[32px] p-[2px] electric-card overflow-hidden group">
                <!-- Border Gradient -->
                <div class="absolute inset-0 bg-gradient-to-br from-brand-300 via-brand-600 to-transparent opacity-80 z-0 group-hover:opacity-100 transition-opacity duration-700"></div>
                
                <div class="relative z-10 bg-[#050505] rounded-[30px] h-full w-full overflow-hidden">
                    <iframe 
                        class="w-full h-full object-cover rounded-[30px]"
                        src="https://www.youtube.com/embed/AQBDy5XBnpg?si=FbpkzDu0P3wkCRjY&color=white&modestbranding=1" 
                        title="YouTube video player" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                        allowfullscreen>
                    </iframe>
                </div>
            </div>
        </div>

        <!-- Vertical Timeline -->
        <div class="max-w-5xl mx-auto px-6 relative">
            
            <!-- Section Header -->
            <div class="mb-24 text-center animate-on-scroll [animation:fadeInUpBlur_1s_cubic-bezier(0.2,0.8,0.2,1)_both]">
                <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full border border-white/10 bg-white/5 backdrop-blur-sm text-[11px] text-neutral-300 mb-6 cursor-default">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-brand-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-gradient-to-tr from-brand-600 to-brand-400"></span>
                    </span>
                    <span class="uppercase tracking-[0.2em] font-bold text-brand-200">Trajetória</span>
                </div>
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-sans font-semibold text-white tracking-tighter text-glow">
                    Experiência <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-200 to-brand-500">Comprovada</span>
                </h2>
            </div>
            
            <!-- Timeline Axis -->
            <!-- Note: timeline axis stops matching exactly the dots if we don't size it right, it's just a background line -->
            <div class="absolute left-6 md:left-1/2 top-[220px] bottom-0 w-px bg-gradient-to-b from-brand-500/0 via-brand-500/40 to-brand-500/0 md:-translate-x-1/2"></div>
            
            <!-- Timeline Items Wrapper -->
            <div class="space-y-24 relative z-10 overflow-hidden md:overflow-visible py-4">
{timeline_html}
            </div>
        </div>
    </section>

</body>"""

if '<!-- Second Section' not in content:
    content = content.replace('</body>', section_2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
