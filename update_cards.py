import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

testimonials = [
    {
        "name": "Patrícia Dias",
        "role": "Gerente na Hapvida",
        "img": "Depoimentos/Patricia.jpg",
        "text": '"Tive a oportunidade de trabalhar com Chris Berenguer no Hapvida NotreDame Intermédica, no time de Produtos / Inovação. Ao longo desse período, Chris se consolidou como uma referência em gestão de portfólio de produtos e como um verdadeiro disseminador de conhecimento. (...) Trabalhar com ele foi contar com um profissional que influenciou positivamente o time e gerou impacto."'
    },
    {
        "name": "Vivian Furlan",
        "role": "Product Manager na Hapvida",
        "img": "Depoimentos/Vivian.jpg",
        "text": '"Tive o prazer de trabalhar com o Chris, que sempre se destacou por ser um profissional parceiro, organizado e com excelente domínio técnico. Tem uma postura colaborativa, compartilha conhecimento com o time e contribui para um ambiente de trabalho mais eficiente e saudável."'
    },
    {
        "name": "Edmilson Rodrigues",
        "role": "CEO na Lovecrypto",
        "img": "Depoimentos/Edmilson.jpg",
        "text": '"Chris é um profissional excelente e multifuncional. Ele tem habilidades criativas, gerenciais e de comunicação interpessoal. Ele se encaixa bem em qualquer equipe e tem muito sangue no olho para procurar onde ele pode fazer sua contribuição. Qualquer equipe terá sorte em ter um profissional como o Chris!"'
    },
    {
        "name": "Paulo César",
        "role": "Diretor de TI na PagSeguro",
        "img": "Depoimentos/Paulo_Cesar.jpg",
        "text": '"Chris é um profissional detalhista e bem técnico, sempre trabalhando em conjunto com o time de Desenvolvimento para garantir as melhores entregas para os nossos clientes."'
    },
    {
        "name": "Wagner Frazão",
        "role": "CEO no Grupo ISEAD",
        "img": "Depoimentos/Wagner Frazao.jpg",
        "text": '"Chris é um excelente profissional que associa a competência técnica, com forte senso de equipe e altíssimo nível de relacionamento interpessoal. Some-se a isso, sua excelente formação acadêmica e seus conhecimentos decorrentes de suas relevantes experiências. Por esses motivos, recomendo fortemente Chris para atuação em equipes de alta performance."'
    },
    {
        "name": "Nicolas Nogueira",
        "role": "Business Analyst na PagSeguro",
        "img": "Depoimentos/Nicolas Ferreira.jpg",
        "text": '"O Chris domina o conhecimento em criptoativos e assuntos ligados à tecnologia e desenvolvimento, o que contribui para o seu excelente desempenho na área!"'
    }
]

def format_card(data):
    return f'''                    <!-- {data["name"]} -->
                    <div class="w-[350px] md:w-[480px] shrink-0 relative group rounded-[32px] bg-white/[0.02] backdrop-blur-xl border border-white/[0.08] overflow-hidden hover:-translate-y-4 hover:shadow-[0_30px_60px_-15px_rgba(91,46,255,0.3)] hover:border-brand-500/50 hover:bg-white/[0.04] transition-all duration-700 ease-out p-10 flex flex-col justify-between">
                        <!-- subtle inner glow -->
                        <div class="absolute inset-0 bg-gradient-to-br from-brand-500/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                        
                        <div class="relative z-10 mb-8">
                            <svg class="w-10 h-10 text-brand-500/40 mb-6 group-hover:scale-110 group-hover:text-brand-400 transition-all duration-500" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                            <p class="text-slate-300 text-base md:text-lg leading-[1.8] font-light group-hover:text-white transition-colors duration-500">
                                {data["text"]}
                            </p>
                        </div>
                        
                        <div class="relative z-10 flex items-center gap-5 mt-auto pt-6 border-t border-white/5 group-hover:border-white/10 transition-colors duration-500">
                            <div class="relative">
                                <div class="absolute -inset-1 bg-gradient-to-r from-brand-400 to-[#00E5C0] rounded-full blur opacity-0 group-hover:opacity-50 transition-opacity duration-500"></div>
                                <img src="{data["img"]}" alt="{data["name"]}" class="relative w-14 h-14 rounded-full object-cover border-2 border-white/10 group-hover:border-white/40 transition-colors duration-500" loading="lazy">
                            </div>
                            <div>
                                <h4 class="text-white font-bold text-base md:text-lg tracking-wide group-hover:text-brand-300 transition-colors duration-500">{data["name"]}</h4>
                                <p class="text-[#00E5C0] text-xs font-bold tracking-[0.2em] uppercase mt-1">{data["role"]}</p>
                            </div>
                        </div>
                    </div>'''

cards_html = "\\n".join([format_card(c) for c in testimonials])

new_section_inner = f"""
                <!-- Set 1 (Original 6) -->
                <div class="flex gap-6 pr-6">
{cards_html}
                </div>

                <!-- Set 2 (Duplicated for Seamless Infinite Loop) -->
                <div class="flex gap-6 pr-6" aria-hidden="true">
{cards_html}
                </div>
            </div>
        </div>
    </section>"""

start_str = '<div class="flex w-max animate-marquee hover:[animation-play-state:paused] cursor-grab active:cursor-grabbing">'
end_str = '</section>'

import re
# Use re.sub to match everything between start_str and end_str, and replace it.
# We will match the start_str, then everything up to </section>
pattern = re.compile(re.escape(start_str) + r'.*?<\/section>', re.DOTALL)

if pattern.search(html):
    new_html = pattern.sub(start_str + new_section_inner, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("re.sub success")
else:
    print("pattern not found")
