# B2B SaaS PM · 一页版

本地用 pdflatex 编译过，刚好一页，每条 bullet 1–2 行、两端对齐，没有只剩一两个词的尾行。下面先是文字版，再是 Overleaf 代码。这一版的删减和改写只在这个 tab 里，不影响上一级的文字版和完整版代码。

## 和完整版相比改了什么

- 版式改成你参考 PDF 的样子：Education 放在 Experience 前面，bullet 两端对齐。
- TubeScience：T1 压成一行，T4 和 T5 合成一条。
- Dreamwriter：D1 压成一行。Adobe：A1、A2 各压成一行。Fabrica：F2 压成一行。Cider：C1 压成一行。
- 可选的 F3、C3 没放，一页放不下。Summary 压到两行，关键词加了 Roadmapping。

## 文字版

Selena Zhi · Portfolio · GitHub · LinkedIn

Product Manager shipping B2B and internal platform products for business users. Took an internal AI tool to \~75% adoption across a 180-person organization and built a B2B sourcing marketplace MVP; Berkeley MEng in HCI.

*B2B SaaS · Internal Tools · Customer Discovery · Stakeholder Management · PRDs · Roadmapping · Adoption*

### Education

**University of California, Berkeley** · Master of Engineering, Human-Computer Interaction · Sep 2024 – May 2026

**Beijing Foreign Studies University** · Bachelor of Arts, History · Sep 2019 – Jul 2023

### Experience

**TubeScience, Inc.** · Product Manager, Ads Product & Automation · Los Angeles, CA · Aug 2026 – Present

- First PM hire; led a company-critical AI initiative with a staff engineer, a data scientist, and C-suite partners
- Built an AI ad reference discovery tool 0-to-1, prototyping in Claude Code in 3 days and launching the MVP in 3 weeks; used user research to narrow a video-based concept into a lightweight text-based MVP
- Defined search, retrieval, and ranking logic across 189K+ ads using performance, cost, and brand/industry signals, cutting reference discovery from 3.5 hours to under 5 minutes; reached \~75% adoption across a 180-person creative org

**Dreamwriter, Inc.** · Product Management Intern, Growth · San Francisco, CA · Jun 2025 – Aug 2025

- Grew WAU 8% in the first month by launching an AI content calendar that auto-generates personalized multi-week plans
- A/B tested messaging, email order, and send cadence, lifting CTR by 11%, sign-ups by 4%, and paid conversion by 13.5%

**Adobe Creative Cloud × UC Berkeley Co-op Program** · Product Strategy & Design Project, Subscription Growth · Berkeley, CA · Sep 2024 – Dec 2024

- Analyzed data on 160K companies, showing businesses under 50 employees drive 53% of customers and 71% of revenue
- Interviewed 20+ design-team buyers across 3 regions and mapped the purchase flow, pinpointing 4 key drop-off points
- Authored a PRD and prototyped a segmented purchase flow with user-type routing and separate subscription and payment steps; in usability tests with 40+ users, cut time-to-purchase by 37% and lifted SMB completion by 15%

**Fabrica (UC Berkeley Lean LaunchPad Venture)** · Product Manager, B2B Fashion Sourcing Marketplace · Berkeley, CA · Oct 2024 – May 2025

- Launched an MVP marketplace connecting 155K+ US SMB fashion brands with 12K+ vetted Asian suppliers, featuring smart search, granular filters, sample requests, and centralized supplier conversations
- Validated a $59B sourcing opportunity through 80+ interviews with brands, designers, and agents (e.g., Nike, Alo Yoga)

**Cider, Inc.** · Product Management Intern, E-commerce Ops & Consumer Experience · Los Angeles, CA · May 2024 – Aug 2024

- Lifted purchase conversion by 5% and cut size-related returns by 7% via AI size recommendations in 130+ markets
- Standardized quality inspection across 3 US and China factories with a 3-level defect severity framework, cutting inspection time by 45%, saving 88 inspector hours per week, and reducing quality returns by 4%

### Awards

- **Agent Master Hackathon (1st Prize)**: Defined the product vision and scoped the MVP for an LLM-based agent pipeline that automates reward function generation for RL, translating requirements into agent workflows and specs for engineers

### Technical Skills

- **Product & Analysis**: SQL, A/B Testing, PostHog, HubSpot, Roadmap Planning, Jira, Agile/Scrum
- **Research & Strategy**: User Research, JTBD, Journey Mapping, Qualitative & Quantitative Analysis
- **AI & Prototyping**: LLM APIs, Prompt Engineering, Claude Code, Cursor, Lovable, Figma, Framer, Adobe Creative Suite
- **Coding**: Python, JavaScript, HTML/CSS, C++
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
Product Manager shipping B2B and internal platform products for business users. Took an internal AI tool to $\sim$75\% adoption across a 180-person organization and built a B2B sourcing marketplace MVP; Berkeley MEng in HCI.
\par}
\vspace{6pt}
{\small\noindent
B2B SaaS\sep Internal Tools\sep Customer Discovery\sep Stakeholder Management\sep PRDs\sep Roadmapping\sep Adoption
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
            \resumeItem{Grew WAU 8\% in the first month by launching an AI content calendar that auto-generates personalized multi-week plans}
            \resumeItem{A/B tested messaging, email order, and send cadence, lifting CTR by 11\%, sign-ups by 4\%, and paid conversion by 13.5\%}
        \resumeItemListEnd

        \resumeSubheading{Adobe Creative Cloud $\times$ UC Berkeley Co-op Program}{Berkeley, CA}{Product Strategy \& Design Project, Subscription Growth}{Sep 2024 -- Dec 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Analyzed data on 160K companies, showing businesses under 50 employees drive 53\% of customers and 71\% of revenue}
            \resumeItem{Interviewed 20+ design-team buyers across 3 regions and mapped the purchase flow, pinpointing 4 key drop-off points}
            \resumeItem{Authored a PRD and prototyped a segmented purchase flow with user-type routing and separate subscription and payment steps; in usability tests with 40+ users, cut time-to-purchase by 37\% and lifted SMB completion by 15\%}
        \resumeItemListEnd

        \resumeSubheading{Fabrica (UC Berkeley Lean LaunchPad Venture)}{Berkeley, CA}{Product Manager, B2B Fashion Sourcing Marketplace}{Oct 2024 -- May 2025}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched an MVP marketplace connecting 155K+ US SMB fashion brands with 12K+ vetted Asian suppliers, featuring smart search, granular filters, sample requests, and centralized supplier conversations}
            \resumeItem{Validated a \$59B sourcing opportunity through 80+ interviews with brands, designers, and agents (e.g., Nike, Alo Yoga)}
        \resumeItemListEnd

        \resumeSubheading{Cider, Inc.}{Los Angeles, CA}{Product Management Intern, E-commerce Ops \& Consumer Experience}{May 2024 -- Aug 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Lifted purchase conversion by 5\% and cut size-related returns by 7\% via AI size recommendations in 130+ markets}
            \resumeItem{Standardized quality inspection across 3 US and China factories with a 3-level defect severity framework, cutting inspection time by 45\%, saving 88 inspector hours per week, and reducing quality returns by 4\%}
        \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------AWARDS-----------
\vspace{-3pt}
\section{Awards}
    \begin{itemize}[leftmargin=0.0in, label={}]
    \small{
        \item{\justifying
            \textbf{Agent Master Hackathon (1st Prize)}{: Defined the product vision and scoped the MVP for an LLM-based agent pipeline that automates reward function generation for RL, translating requirements into agent workflows and specs for engineers}\par} } \end{itemize}

%-----------TECHNICAL SKILLS-----------
\section{Technical Skills}
    \begin{itemize}[leftmargin=0.0in, label={}]
    \small{
        \item{
            \textbf{Product \& Analysis}{: SQL, A/B Testing, PostHog, HubSpot, Roadmap Planning, Jira, Agile/Scrum} \\
            \textbf{Research \& Strategy}{: User Research, JTBD, Journey Mapping, Qualitative \& Quantitative Analysis} \\
            \textbf{AI \& Prototyping}{: LLM APIs, Prompt Engineering, Claude Code, Cursor, Lovable, Figma, Framer, Adobe Creative Suite} \\
            \textbf{Coding}{: Python, JavaScript, HTML/CSS, C++} \\
            \textbf{Language}{: English \& Mandarin (Bilingual), Spanish (Limited), Korean (Basic)} } } \end{itemize}
%-------------------------------------------
\end{document}
```
