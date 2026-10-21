# APM · 一页版

本地用 pdflatex 编译过，刚好一页，每条 bullet 1–2 行、两端对齐，没有只剩一两个词的尾行。下面先是文字版，再是 Overleaf 代码。这一版的删减和改写只在这个 tab 里，不影响上一级的文字版和完整版代码。

## 和完整版相比改了什么

- 版式和你参考 PDF 一致：Education 在最上面，bullet 两端对齐。
- TubeScience：T1 压成一行，T4 和 T5 合成一条。
- Dreamwriter：D1 和 D2 合成一条（内容日历 + 40 人验证）。Adobe：A1 压成一行。Fabrica：F1 压成一行。
- 可选的 F3、F4 没放。Summary 压到两行，去掉了 Dreamwriter（下面经历里有）。

## 文字版

Selena Zhi · Portfolio · GitHub · LinkedIn

Berkeley MEng (HCI) graduate and Product Manager who ships fast and prototypes with code and LLMs. As TubeScience's first PM hire, took an AI tool from prototype to MVP launch in 3 weeks; prior product work at Adobe and Cider.

*Product Sense · Rapid Prototyping · User Research · A/B Testing · LLM Workflows · Technical Fluency*

### Education

**University of California, Berkeley** · Master of Engineering, Human-Computer Interaction · Sep 2024 – May 2026

**Beijing Foreign Studies University** · Bachelor of Arts, History · Sep 2019 – Jul 2023

### Experience

**TubeScience, Inc.** · Product Manager, Ads Product & Automation · Los Angeles, CA · Aug 2026 – Present

- First PM hire; led a company-critical AI initiative with a staff engineer, a data scientist, and C-suite partners
- Built an AI ad reference discovery tool 0-to-1, prototyping in Claude Code in 3 days and launching the MVP in 3 weeks; used user research to narrow a video-based concept into a lightweight text-based MVP
- Defined search, retrieval, and ranking logic across 189K+ ads using performance, cost, and brand/industry signals, cutting reference discovery from 3.5 hours to under 5 minutes; reached \~75% adoption across a 180-person creative org

**Dreamwriter, Inc.** · Product Management Intern, Growth · San Francisco, CA · Jun 2025 – Aug 2025

- Launched an AI content calendar that auto-generates personalized multi-week plans, validating it with 40 users via LLM prototypes before engineering build; grew WAU 8% in the first month after launch
- A/B tested messaging, email order, and send cadence, lifting CTR by 11%, sign-ups by 4%, and paid conversion by 13.5%

**Adobe Creative Cloud × UC Berkeley Co-op Program** · Product Strategy & Design Project, Subscription Growth · Berkeley, CA · Sep 2024 – Dec 2024

- Analyzed data on 160K companies, showing businesses under 50 employees drive 53% of customers and 71% of revenue
- Authored a PRD and prototyped a segmented purchase flow with user-type routing and separate subscription and payment steps; in usability tests with 40+ users, cut time-to-purchase by 37% and lifted SMB completion by 15%

**Fabrica (UC Berkeley Lean LaunchPad Venture)** · Product Manager, B2B Fashion Sourcing Marketplace · Berkeley, CA · Oct 2024 – May 2025

- Launched an MVP marketplace linking 155K+ US SMB fashion brands with 12K+ vetted Asian suppliers via smart search

**Cider, Inc.** · Product Management Intern, E-commerce Ops & Consumer Experience · Los Angeles, CA · May 2024 – Aug 2024

- Launched personalized size recommendations using body measurements and historical fit and return data, lifting purchase conversion by 5% and cutting size-related returns by 7% across 130+ markets

### Awards

- **Agent Master Hackathon (1st Prize)**: Defined the product vision and scoped the MVP for an LLM-based agent pipeline that automates reward function generation for RL, translating requirements into agent workflows and specs for engineers
- **Google DeepMind Hackathon**: Designed the end-to-end UX for an iOS app that lets users control an LLM-powered agent hands-free via eye tracking, prototyping gaze-based flows in Figma and iterating through user testing

### Technical Skills

- **Product & Analysis**: SQL, A/B Testing, PostHog, HubSpot, Roadmap Planning, Jira, Agile/Scrum
- **Coding**: Python, JavaScript, HTML/CSS, C++
- **AI & Prototyping**: LLM APIs, Prompt Engineering, Claude Code, Cursor, Lovable, Figma, Framer, Adobe Creative Suite
- **Research & Strategy**: User Research, JTBD, Journey Mapping, Qualitative & Quantitative Analysis
- **Language**: English & Mandarin (Bilingual), Spanish (Limited), Korean (Basic)

## Overleaf 代码

```latex
\documentclass[letterpaper, 11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome}
\usepackage{color}
\usepackage[normalem]{ulem}
\usepackage{url}
\usepackage{ragged2e}
\setlength{\JustifyingParindent}{0pt}

\input{glyphtounicode}

\DeclareUrlCommand\ULurl{%
  \renewcommand\UrlFont{\color{black}}%
  \renewcommand\UrlLeft{\uline\bgroup}%
  \renewcommand\UrlRight{\egroup}}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.6in}
\addtolength{\textwidth}{1.2in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{0.9in}
\setlength{\footskip}{5pt}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
    \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]
\titlespacing*{\section}{0pt}{3ex}{2ex}

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
    \item\small{
        {\justifying #1 \vspace{-2pt}\par}
    }
}

\newcommand{\resumeSubheading}[4]{
    \vspace{-2pt}
    \item
    \begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1}        & #2 \\
        \textit{\small #3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}\vspace{-2pt}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.15in]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-2pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\sep}{\hfill$\cdot$\hfill}
\begin{document}

\begin{center}
    \textbf{\Huge Selena Zhi} \\ \vspace{1pt}
    \href{https://www.selenazhi.com/}{\ULurl{Portfolio}} $|$
    \href{https://github.com/SelenaChi}{\ULurl{GitHub}} $|$
    \href{https://www.linkedin.com/in/selena-zhi/}{\ULurl{LinkedIn}}
\end{center}

%-----------SUMMARY-----------
\vspace{2pt}
{\small\setlength{\parindent}{0pt}\justifying
Berkeley MEng (HCI) graduate and Product Manager who ships fast and prototypes with code and LLMs. As TubeScience's first PM hire, took an AI tool from prototype to MVP launch in 3 weeks; prior product work at Adobe and Cider.
\par}
\vspace{6pt}
{\small\noindent
Product Sense\sep Rapid Prototyping\sep User Research\sep A/B Testing\sep LLM Workflows\sep Technical Fluency
\par}
\vspace{2pt}

%-----------EDUCATION-----------
\section{Education}
    \resumeSubHeadingListStart
        \resumeSubheading{University of California, Berkeley}{Sep 2024 -- May 2026}
        {Master of Engineering, Human-Computer Interaction}{}
        \resumeSubheading{Beijing Foreign Studies University}{Sep 2019 -- Jul 2023}
        {Bachelor of Arts, History}{}
    \resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\vspace{-1.4pt}
\section{Experience}
    \resumeSubHeadingListStart
        \resumeSubheading{TubeScience, Inc.}{Los Angeles, CA}{Product Manager, Ads Product \& Automation}{Aug 2026 -- Present}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{First PM hire; led a company-critical AI initiative with a staff engineer, a data scientist, and C-suite partners}
            \resumeItem{Built an AI ad reference discovery tool 0-to-1, prototyping in Claude Code in 3 days and launching the MVP in 3 weeks; used user research to narrow a video-based concept into a lightweight text-based MVP}
            \resumeItem{Defined search, retrieval, and ranking logic across 189K+ ads using performance, cost, and brand/industry signals, cutting reference discovery from 3.5 hours to under 5 minutes; reached $\sim$75\% adoption across a 180-person creative org}
        \resumeItemListEnd

        \resumeSubheading{Dreamwriter, Inc.}{San Francisco, CA}{Product Management Intern, Growth}{Jun 2025 -- Aug 2025}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched an AI content calendar that auto-generates personalized multi-week plans, validating it with 40 users via LLM prototypes before engineering build; grew WAU 8\% in the first month after launch}
            \resumeItem{A/B tested messaging, email order, and send cadence, lifting CTR by 11\%, sign-ups by 4\%, and paid conversion by 13.5\%}
        \resumeItemListEnd

        \resumeSubheading{Adobe Creative Cloud $\times$ UC Berkeley Co-op Program}{Berkeley, CA}{Product Strategy \& Design Project, Subscription Growth}{Sep 2024 -- Dec 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Analyzed data on 160K companies, showing businesses under 50 employees drive 53\% of customers and 71\% of revenue}
            \resumeItem{Authored a PRD and prototyped a segmented purchase flow with user-type routing and separate subscription and payment steps; in usability tests with 40+ users, cut time-to-purchase by 37\% and lifted SMB completion by 15\%}
        \resumeItemListEnd

        \resumeSubheading{Fabrica (UC Berkeley Lean LaunchPad Venture)}{Berkeley, CA}{Product Manager, B2B Fashion Sourcing Marketplace}{Oct 2024 -- May 2025}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched an MVP marketplace linking 155K+ US SMB fashion brands with 12K+ vetted Asian suppliers via smart search}
        \resumeItemListEnd

        \resumeSubheading{Cider, Inc.}{Los Angeles, CA}{Product Management Intern, E-commerce Ops \& Consumer Experience}{May 2024 -- Aug 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched personalized size recommendations using body measurements and historical fit and return data, lifting purchase conversion by 5\% and cutting size-related returns by 7\% across 130+ markets}
        \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------AWARDS-----------
\vspace{-3pt}
\section{Awards}
    \begin{itemize}[leftmargin=0.0in, label={}]
    \small{
        \item{\justifying
            \textbf{Agent Master Hackathon (1st Prize)}{: Defined the product vision and scoped the MVP for an LLM-based agent pipeline that automates reward function generation for RL, translating requirements into agent workflows and specs for engineers} \\[2pt]
            \textbf{Google DeepMind Hackathon}{: Designed the end-to-end UX for an iOS app that lets users control an LLM-powered agent hands-free via eye tracking, prototyping gaze-based flows in Figma and iterating through user testing}\par} } \end{itemize}

%-----------TECHNICAL SKILLS-----------
\section{Technical Skills}
    \begin{itemize}[leftmargin=0.0in, label={}]
    \small{
        \item{
            \textbf{Product \& Analysis}{: SQL, A/B Testing, PostHog, HubSpot, Roadmap Planning, Jira, Agile/Scrum} \\
            \textbf{Coding}{: Python, JavaScript, HTML/CSS, C++} \\
            \textbf{AI \& Prototyping}{: LLM APIs, Prompt Engineering, Claude Code, Cursor, Lovable, Figma, Framer, Adobe Creative Suite} \\
            \textbf{Research \& Strategy}{: User Research, JTBD, Journey Mapping, Qualitative \& Quantitative Analysis} \\
            \textbf{Language}{: English \& Mandarin (Bilingual), Spanish (Limited), Korean (Basic)} } } \end{itemize}
%-------------------------------------------
\end{document}
```
