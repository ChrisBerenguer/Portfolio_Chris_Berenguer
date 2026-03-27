import re

html_path = "c:\\Users\\chris\\OneDrive\\Documentos\\Asimov_Academy\\Vibe Design\\Portfolio Website IA\\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD CSS CLASSES
new_css = """
        /* Advanced Reveal Animations */
        .reveal-element {
            will-change: transform, opacity, filter;
        }

        /* 1. Blur Fades */
        .reveal-blur {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
            filter: blur(10px);
            transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .reveal-blur.is-revealed {
            opacity: 1;
            transform: translateY(0) scale(1);
            filter: blur(0);
        }

        /* 2. Slide Right */
        .reveal-slide-right {
            opacity: 0;
            transform: translateX(-40px);
            filter: blur(5px);
            transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .reveal-slide-right.is-revealed {
            opacity: 1;
            transform: translateX(0);
            filter: blur(0);
        }

        /* 3. Slide Left */
        .reveal-slide-left {
            opacity: 0;
            transform: translateX(40px);
            filter: blur(5px);
            transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .reveal-slide-left.is-revealed {
            opacity: 1;
            transform: translateX(0);
            filter: blur(0);
        }

        /* 4. Pop Scale */
        .reveal-pop {
            opacity: 0;
            transform: scale(0.5);
            transition: all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .reveal-pop.is-revealed {
            opacity: 1;
            transform: scale(1);
        }

        /* Delay Utilities */
        .delay-100 { transition-delay: 100ms; }
        .delay-200 { transition-delay: 200ms; }
        .delay-300 { transition-delay: 300ms; }
        .delay-400 { transition-delay: 400ms; }
        .delay-500 { transition-delay: 500ms; }
        .delay-600 { transition-delay: 600ms; }
"""

html = html.replace('</style>', new_css + '\n    </style>')

# 2. INJECT JAVASCRIPT
new_js = """
    <!-- Advanced Scroll Animations Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const observerOptions = {
                root: null,
                rootMargin: '0px 0px -10% 0px', // Trigger sligthly before bottom
                threshold: 0
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-revealed');
                    } else {
                        // Remove class when out of view bounds to reset animation
                        const rect = entry.target.getBoundingClientRect();
                        // Only reset if we scroll PAST them (either up or down) far enough
                        // To make it feel natural, we reset when they leave viewport completely
                        if (entry.intersectionRatio <= 0) {
                            entry.target.classList.remove('is-revealed');
                        }
                    }
                });
            }, observerOptions);

            const revealElements = document.querySelectorAll('.reveal-element');
            revealElements.forEach(el => observer.observe(el));
        });
    </script>
</body>"""

html = html.replace('</body>', new_js)

# 3. REPLACE CLASSES

# Hero Section replacements (animate-entry)
html = html.replace('animate-entry', 'reveal-element reveal-blur')

# Timeline/Video Section replacements
# Current string: `animate-on-scroll [animation:fadeInUpBlur_1s_cubic-bezier(0.2,0.8,0.2,1)_both]`

target_string = 'animate-on-scroll [animation:fadeInUpBlur_1s_cubic-bezier(0.2,0.8,0.2,1)_both]'

# Replace the first two (Video container and Section Header) with reveal-blur
# Actually, let's just use re.sub or generic replacement depending on context.
# We have Timeline nodes that look better sliding in from left/right.

# Find all occurrences
occurrences = [m.start() for m in re.finditer(re.escape(target_string), html)]

# We will just replace all of them with 'reveal-element reveal-blur' first as a baseline
html = html.replace(target_string, 'reveal-element reveal-blur')

# Now inject delays into timeline cards!
# Timeline items are in `.space-y-24`
# Let's add alternating slide-right and slide-left to the cards to make them dynamic.
# The card main container is usually: class="relative flex flex-col md:flex-row ... items-start group reveal-element reveal-blur"
# We can change it for timeline specifically.

html = html.replace('class="relative flex flex-col md:flex-row  items-start md:items-center md:justify-between group reveal-element reveal-blur"', 'class="relative flex flex-col md:flex-row  items-start md:items-center md:justify-between group reveal-element reveal-slide-right delay-100"')
html = html.replace('class="relative flex flex-col md:flex-row md:flex-row-reverse items-start md:items-center md:justify-between group reveal-element reveal-blur"', 'class="relative flex flex-col md:flex-row md:flex-row-reverse items-start md:items-center md:justify-between group reveal-element reveal-slide-left delay-200"')

# Fix Timeline Nodes to Pop
html = html.replace('absolute left-0 md:left-1/2 w-4 h-4 rounded-full', 'absolute left-0 md:left-1/2 w-4 h-4 rounded-full reveal-element reveal-pop delay-300')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML modified successfully.")
