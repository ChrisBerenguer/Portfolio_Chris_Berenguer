import json

data = [
    {
        "year": "2025",
        "company": "Hapvida",
        "role": "GPM | Inovação & IA",
        "context": "HealthTech em larga escala + IA aplicada em produção",
        "bullets": [
            "Liderança de discovery e PoCs com IA assistencial",
            "Gestão de portfólio e alinhamento executivo",
            "Projetos com impacto direto em eficiência clínica e operacional"
        ]
    },
    {
        "year": "2024",
        "company": "Ibrowse",
        "role": "Senior Product Owner",
        "context": "Transformação digital no setor público de saúde",
        "bullets": [
            "Liderança de times ágeis em ERP hospitalar",
            "Implantação de sistemas em campo (hospitais reais)",
            "Estruturação de processos, requisitos e KPIs"
        ]
    },
    {
        "year": "2023",
        "company": "TappnEd",
        "role": "Product Manager | GenAI – Internacional",
        "context": "Startup de IA generativa aplicada à educação",
        "bullets": [
            "Desenvolvimento de PoCs com LLMs em Python",
            "Tradução de negócio → solução técnica",
            "Criação end-to-end de produto com IA"
        ]
    },
    {
        "year": "2023",
        "company": "Bamboo",
        "role": "PO | Fintech B2B",
        "context": "Data Analytics para mercado financeiro",
        "bullets": [
            "Implementação de Scrum e organização do time",
            "Gestão de backlog, métricas e OKRs",
            "Ganho expressivo de performance da squad"
        ]
    },
    {
        "year": "2022",
        "company": "PagSeguro",
        "role": "Product Owner | Crypto",
        "context": "Produto financeiro em ambiente regulatório e competitivo",
        "bullets": [
            "Gestão de produto de investimentos em cripto",
            "Definição de métricas e evolução contínua",
            "Atuação end-to-end no ciclo do produto"
        ]
    },
    {
        "year": "2021",
        "company": "Lovecrypto",
        "role": "Growth Product Manager",
        "context": "Startup early-stage de pagamentos em cripto",
        "bullets": [
            "Estratégia de crescimento (GTM + aquisição)",
            "Testes A/B, discovery e Product-Market Fit",
            "Escala de base de usuários e engajamento"
        ]
    }
]

html = ""
for i, item in enumerate(data):
    reversed_class = "md:flex-row-reverse" if i % 2 != 0 else ""
    year_pl = "w-full md:w-5/12 pl-8 md:pl-12 md:text-left" if i % 2 != 0 else "w-full md:w-5/12 pl-8 md:pl-0 md:pr-12 md:text-right"
    card_pl = "w-full md:w-5/12 pl-8 md:pl-0 md:pr-12 md:text-right" if i % 2 != 0 else "w-full md:w-5/12 pl-8 md:pl-12 text-left"
    
    bullets_html = ""
    for bullet in item["bullets"]:
        bullets_html += f'''                                    <li class="text-sm text-slate-400 font-light flex items-start gap-2 text-left">
                                        <iconify-icon icon="solar:check-circle-bold" class="text-brand-500 shrink-0 mt-0.5"></iconify-icon>
                                        <span>{bullet}</span>
                                    </li>\n'''

    html += f'''
                <!-- {item['company']} -->
                <div class="relative flex flex-col md:flex-row {reversed_class} items-start md:items-center md:justify-between group animate-on-scroll [animation:fadeInUpBlur_1s_cubic-bezier(0.2,0.8,0.2,1)_both]">
                    <!-- Timeline Node -->
                    <div class="absolute left-0 md:left-1/2 w-4 h-4 rounded-full bg-[#0B0C15] border-2 border-brand-400 md:-translate-x-1/2 -translate-x-[7px] mt-[10px] md:mt-0 z-20 group-hover:scale-150 group-hover:bg-brand-500 transition-all duration-300 shadow-[0_0_15px_rgba(91,46,255,0.6)]"></div>
                    
                    <!-- Year -->
                    <div class="{year_pl} flex md:block items-center mb-2 md:mb-0">
                        <span class="text-xl md:text-3xl font-bricolage font-medium text-brand-300 group-hover:text-brand-100 transition-colors">{item['year']}</span>
                    </div>
                    
                    <!-- Card -->
                    <div class="{card_pl}">
                        <div class="bg-white/[0.02] border border-white/5 rounded-2xl p-6 md:p-8 hover:bg-white/[0.05] hover:border-brand-500/40 transition-all duration-500 shadow-xl group-hover:scale-[1.02] text-left relative overflow-hidden">
                            <div class="absolute inset-0 bg-gradient-to-br from-brand-500/0 via-transparent to-brand-500/0 group-hover:from-brand-500/10 group-hover:to-brand-800/10 transition-all duration-500"></div>
                            
                            <h3 class="text-xl md:text-2xl font-sans font-semibold text-white mb-1 relative z-10">{item['company']}</h3>
                            <div class="text-xs text-brand-400 uppercase tracking-widest font-medium mb-5 relative z-10">{item['role']}</div>
                            
                            <div class="mb-5 relative z-10">
                                <span class="text-[10px] text-slate-500 uppercase tracking-[0.2em] font-semibold block mb-1">Contexto</span>
                                <p class="text-sm text-slate-300 font-light leading-relaxed">{item['context']}</p>
                            </div>
                            
                            <div class="relative z-10">
                                <span class="text-[10px] text-slate-500 uppercase tracking-[0.2em] font-semibold block mb-2">O que fiz:</span>
                                <ul class="space-y-2">
{bullets_html}                                </ul>
                            </div>
                        </div>
                    </div>
                </div>\n'''

with open('timeline.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
