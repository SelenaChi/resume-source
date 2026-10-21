# Data-heavy PM · Overleaf 代码

整段复制到 Overleaf 的 main.tex 里就能看到排版。内容和上一级「Data-heavy PM」tab 的文字版一致，这版没有 Awards。

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
        {#1 \vspace{-2pt}}
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

\usepackage{ragged2e}
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
Product Manager who turns data into product decisions, from defining north-star metrics and running A/B tests to standardizing data for downstream analysis. Works hands-on with SQL, PostHog, and Python; Berkeley MEng in Human-Computer Interaction.
\par}
\vspace{6pt}
{\small\noindent
Metrics Definition\sep A/B Testing\sep SQL\sep Funnel Analysis\sep Data Standardization\sep Search \& Ranking
\par}
\vspace{2pt}
%-----------EXPERIENCE-----------
\vspace{-1.4pt}
\section{Experience}
    \resumeSubHeadingListStart
        \resumeSubheading{TubeScience, Inc.}{Los Angeles, CA}{Product Manager, Ads Product \& Automation}{Aug 2026 -- Present}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{As the team's first PM hire, led a company-critical AI initiative end to end with a staff engineer and a data scientist, partnering with C-suite executives, the creative VP, and creative leads on scope and priorities}
            \resumeItem{Built an AI-powered ad reference discovery tool from 0 to 1, prototyping with Claude Code in 3 days and launching the MVP in 3 weeks; narrowed scope from a video-based concept to a lightweight text-based MVP based on user research}
            \resumeItem{Set review rounds as the north-star metric, cutting senior review cycles from 6 to 2 per ad and freeing senior creatives' time for higher-value work}
            \resumeItem{Defined search, retrieval, and ranking logic across 189K+ ads using performance, cost, and brand/industry signals, cutting reference discovery from 3.5 hours to under 5 minutes and speeding up ad draft production}
        \resumeItemListEnd

        \resumeSubheading{Dreamwriter, Inc.}{San Francisco, CA}{Product Management Intern, Growth}{Jun 2025 -- Aug 2025}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched an AI content calendar that turns each user's goals, audience, and style into a personalized multi-week plan and auto-generates every piece (emails, one-pagers, case studies), growing WAU 8\% in the first month after launch}
            \resumeItem{Owned automated onboarding in HubSpot; diagnosed a 4-email lifecycle where users opened but didn't act (Day 1 pushed upgrades before users saw value) and rebuilt each email around one next step, shifting from early monetization to progressive education}
            \resumeItem{A/B tested messaging, email order, and send cadence, lifting CTR by 11\%, sign-ups by 4\%, and paid conversion by 13.5\%}
        \resumeItemListEnd

        \resumeSubheading{Adobe Creative Cloud $\times$ UC Berkeley Co-op Program}{Berkeley, CA}{Product Strategy \& Design Project, Subscription Growth}{Sep 2024 -- Dec 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Identified a segment mismatch in Creative Cloud's growth strategy by analyzing 5 years of annual reports and usage data across 160K companies, showing businesses under 50 employees make up 53\% of customers and 71\% of revenue}
            \resumeItem{Authored a PRD and prototyped a segmented purchase flow (user-type routing, separate subscription and payment steps with a billing timeline, team seat assignment); in comparative usability tests with 40+ users, cut time-to-purchase by 37\% and lifted SMB purchase completion by 15\%}
        \resumeItemListEnd

        \resumeSubheading{Fabrica (UC Berkeley Lean LaunchPad Venture)}{Berkeley, CA}{Product Manager, B2B Fashion Sourcing Marketplace}{Oct 2024 -- May 2025}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Interviewed 80+ fashion brands, designers, and sourcing agents, including teams from Nike, Alo Yoga, Converse, and Lululemon, to validate a \$59B sourcing opportunity; identified 3 core pains: relationship-dependent supplier discovery, offline-only material vetting, and fragmented production communication}
        \resumeItemListEnd

        \resumeSubheading{Cider, Inc.}{Los Angeles, CA}{Product Management Intern, E-commerce Ops \& Consumer Experience}{May 2024 -- Aug 2024}
        \resumeItemListStart\vspace{2pt}
            \setlength{\itemsep}{1pt}
            \resumeItem{Launched personalized size recommendations that map shoppers' body measurements against historical fit and return data, lifting purchase conversion by 5\% and reducing size-related returns by 7\%; scaled to 130+ markets}
            \resumeItem{Standardized a manual, time-consuming quality-inspection workflow across 3 factories in the US and China by introducing a 3-level defect severity framework, making defect data objective and consistent for supplier evaluation and downstream reporting; cut inspection time by 45\% (27 min per batch), saved 88 inspector hours per week, and reduced quality-related returns by 4\%}
        \resumeItemListEnd

  \resumeSubHeadingListEnd

\vspace{-3pt}
%-----------EDUCATION-----------
\section{Education}
    \resumeSubHeadingListStart
        \resumeSubheading{University of California, Berkeley}{Sep 2024 -- May 2026}
        {Master of Engineering, Human-Computer Interaction}{}
        \resumeSubheading{Beijing Foreign Studies University}{Sep 2019 -- Jul 2023}
        {Bachelor of Arts, History}{}
    \resumeSubHeadingListEnd
%-------------------------------------------
\section{Technical Skills}
    \begin{itemize}[leftmargin=0.0in, label={}]
    \small{
        \item{
            \textbf{Product \& Analysis}{: SQL, A/B Testing, PostHog, Python, HubSpot, Roadmap Planning, Jira} \\
            \textbf{AI \& Prototyping}{: LLM APIs, Prompt Engineering, Claude Code, Cursor, Lovable, Figma, Framer, Adobe Creative Suite} \\
            \textbf{Research \& Strategy}{: User Research, JTBD, Journey Mapping, Qualitative \& Quantitative Analysis} \\
            \textbf{Coding}{: JavaScript, HTML/CSS, C++} \\
            \textbf{Language}{: English \& Mandarin (Bilingual), Spanish (Limited), Korean (Basic)} } } \end{itemize}
%-------------------------------------------
\end{document}
```
