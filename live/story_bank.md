# Story bank

每段经历整理成 1-2 个故事，用 STAR-L（Situation、Task、Action、Result、Learning）结构。故事正文是可以直接说出口的英文，提示和追问用中文。编号沿用你的格式：S01 = TubeScience，S02 = Dreamwriter，S03 = Adobe，S04 = Fabrica，S05 = Cider。【待补充】是我还不知道、需要你口述的部分。

## 故事索引（中文）

| 编号 | 故事 | 适合回答的 BQ | 状态 |
| --- | --- | --- | --- |
| S01-01 | TubeScience：用 AI 从 0 到 1 做 agent 产品，3 天原型、3 周上线 | 0-to-1、AI 产品、用 AI 做原型、缩小范围 | 完整 |
| S01-02 | TubeScience：180 人团队内部推广，\~75% 采用 | 推动采用、收集用户反馈、跨团队影响力 | 完整 |
| S01-03 | TubeScience：从推荐系统到搜索系统，放弃了什么、保留了什么 | 优先级、取舍、数据不完整时做决策 | 完整 |
| S01-04 | TubeScience：说服 CEO 先做 text，再做 video | 和高层意见不同、stakeholder 管理、用数据推动决策 | 完整 |
| S01-05 | TubeScience：manager 休假时定期汇报，让他回来就能接上 | Managing up、沟通、ownership | 完整 |
| S01-06 | TubeScience：和新同事建立信任 | 团队协作、建立关系、跨职能合作 | 完整 |
| S02-01 | Dreamwriter：AI 内容日历，WAU +8% | 0-to-1、产品策略、用户洞察、快速验证 | 完整 |
| S02-02 | Dreamwriter：Onboarding 改版，付费转化 +13.5% | 数据驱动、模糊问题、优先级、实验 | 完整 |
| S03-01 | Adobe：用数据发现增长策略与客群的错配 | 主动发起、发现机会、数据分析、商业思维 | 完整 |
| S03-02 | Adobe：重做 Creative Cloud 购买流程，time-to-purchase -37% | 用户研究、用户体验、验证方案、提案未被采纳 | 完整 |
| S04-01 | Fabrica：访谈 80+ 品牌，定义问题和机会 | 用户研究、发现机会、在不确定中推进 | 完整 |
| S04-02 | Fabrica：两次缩小 MVP 范围 | Pivot、优先级与取舍、没做成的项目 | 完整 |
| S05-01 | Cider：个性化尺码推荐，转化 +5%、退货 -7% | 产品上线、用户研究改变方案、第一个想法是错的 | 完整 |
| S05-02 | Cider：标准化质检流程，质检时间 -45% | B2B / 内部工具、用户研究、优先级（缩小范围）、标准化 | 完整 |

## Story index (English)

| ID | Story | Best for | Status |
| --- | --- | --- | --- |
| S01-01 | TubeScience: Built an AI agent product from 0 to 1, prototype in 3 days, launch in 3 weeks | 0-to-1, AI products, prototyping with AI, narrowing scope | Complete |
| S01-02 | TubeScience: Drove \~75% adoption across a 180-person team | Driving adoption, gathering user feedback, cross-team influence | Complete |
| S01-03 | TubeScience: Prioritized search filters when the data wasn't ready | Prioritization, trade-offs, technical blockers, MVP scoping | Complete |
| S01-04 | TubeScience: Aligned the CEO on a text-first MVP before video | Disagreeing with leadership, stakeholder management, data-driven decisions | Complete |
| S01-05 | TubeScience: Kept my manager in the loop while he was away | Managing up, communication, ambiguity and changing priorities | Complete |
| S01-06 | TubeScience: How I build trust | Something not on your resume, building trust, working with engineers, going beyond your role | Complete |
| S02-01 | Dreamwriter: AI content calendar, WAU +8% | 0-to-1, product strategy, user insight, fast validation | Complete |
| S02-02 | Dreamwriter: Onboarding redesign, paid conversion +13.5% | Data-driven decisions, ambiguity, prioritization, experimentation | Complete |
| S03-01 | Adobe: Found a mismatch between growth strategy and customer segments | Taking initiative, spotting opportunities, data analysis, business thinking | Complete |
| S03-02 | Adobe: Redesigned the Creative Cloud purchase flow, time-to-purchase -37% | User research, UX, validating solutions, an idea that wasn't adopted | Complete |
| S04-01 | Fabrica: Defined the problem through 80+ brand interviews | User research, spotting opportunities, working through uncertainty | Complete |
| S04-02 | Fabrica: Narrowed the MVP scope twice | Pivots, trade-offs, a project that didn't succeed | Complete |
| S05-01 | Cider: Personalized size recommendations, conversion +5%, returns -7% | Product launch, research changing the solution, a time you were wrong | Complete |
| S05-02 | Cider: Standardized quality inspection, inspection time -45% | B2B / internal tools, user research, scoping, standardization | Complete |

## S01-01 TubeScience: Building an AI agent product from 0 to 1

适合回答：Tell me about a 0-to-1 product / how you use AI in your work / how you scoped an ambiguous idea / tell me about an AI product you built

这一版是你和 mentor 一起打磨过的，正文基本保留原句，只按 STAR-L 拆开。

- **Situation**: This was a time I used AI to build an ad reference discovery tool. For our creative strategists, finding reference ads took a lot of time, and their ideas still needed multiple rounds of senior review to judge what might work.
- **Task**: The goal was to help creative strategists find relevant ads faster and make that part of the workflow more efficient.
- **Action**:
  1. I used Claude Code with OpenSpec, a structured workflow for defining and validating product requirements, to turn a broad idea into a prototype.
  2. My first prompt was too open-ended, and the AI generated features we didn't need. So I narrowed the scope, gave it clearer constraints on what the tool should and shouldn't do, and used a Figma wireframe to show the core experience I wanted to test. That kept the prototype focused on one thing: a library of high-performing ads with smart search and filters.
  3. After speaking with internal users, I made a key product decision: we moved from a video-based concept to a simpler, lightweight text-based MVP, because that was enough for their immediate needs.
  4. I also worked with engineering and data science to prioritize the most useful search filters when the full dataset wasn't ready.
- **Result**: We got the first prototype in front of users in about three days and rolled out the MVP to 180 creative strategists in three weeks. The tool cut the time to find references from 3.5 hours to five minutes.
- **Learning**: Great AI tools aren't just about generating content faster. They're about reducing decision friction in complex workflows. AI helped me prototype in days, but the real value came from narrowing the scope based on what users truly need.

面试提示：

- 你原稿写的是 "reduced review time from 3.5 hours to five minutes"，但简历上 3.5 小时→5 分钟指的是找参考的时间，review 对应的是 6 轮→2 轮。我在正文里改成了 "the time to find references"，练习时也记得改。
- 想加分的话，Result 可以再补一句 "senior review rounds also dropped from 6 to 2"。
- video → text 的收窄和筛选器的取舍，在 S01-03 和 S01-04 里会展开讲。这个故事里一句带过就好，避免几个故事内容重复。

## S01-02 TubeScience: 180 人团队内部推广，\~75% 采用

适合回答：How do you drive adoption / how do you gather and act on user feedback / a time you influenced without authority / how you work with stakeholders

- **Situation**: After we launched the platform as an internal beta, the next challenge was getting a creative organization of more than 180 people to actually use it, while we kept iterating on the product.
- **Task**: I owned the rollout. I needed to drive adoption and build a feedback loop so that real usage shaped what we built next.
- **Action**:
  1. First, I wrote a detailed user playbook and shared it in the creative team's Slack channel, so people could get started on their own.
  2. Second, I turned that channel into our main place for questions, bugs, and ideas. I collected what people reported and scheduled time with engineering to fix issues in batches.
  3. Third, I set up weekly office hours every Friday afternoon with product, the creative VP, and the production team. Each group brought its own user input, and we used it to decide what to iterate on next.
  4. The feedback changed the product. We had planned a video-editing mode that broke each ad into 5-second shots, so strategists could adapt the visuals shot by shot. But strategists told us shots come much later in their process. They can tell whether an ad has a chance to win just by reading the script. So we dropped the shot-by-shot mode and focused on the text.
  5. I also dealt with hesitation. Some junior strategists pushed back at first. They worried the tool would replace them, so they said they didn't need it. When I talked with them, I made it clear the tool only shortens the search. Deciding which draft to change, and how to write it, stays with them: humans stay in the loop. Once that was clear, they were much more willing to try it.
- **Result**: About three quarters of the 180-person team started using the platform during the internal beta, and we kept improving it based on what we heard.
- **Learning**: Adoption isn't just about features. People need to see their feedback turn into real changes, and they need to trust that the tool is there to help them, not replace them.

面试提示：

- 这个故事里的"砍掉逐镜头剪辑"和 S01-04 的"说服 CEO 先做 text"是同一条线。区别是：这里讲的是推广中用户反馈怎么改变产品，S01-04 讲的是怎么说服高层。一场面试里两个都讲的话，这里一句带过就好。
- "年轻同事担心被取代"这个细节很有价值，尤其是面 AI PM 岗位时，它说明你理解 human-in-the-loop 和 AI 产品推广的真实阻力。
- 可能被追问：75% 是怎么统计的？提前想好口径（登录过，还是每周在用）。

## S01-03 TubeScience: Prioritizing search filters when the data wasn't ready

适合回答：How do you prioritize / tell me about a trade-off you made / a time you hit a technical blocker / how you scope an MVP

- **Situation**: When we were building the ad search and recommendation experience, I wanted to redesign the filter logic. The challenge was that the data we needed wasn't ready. Our data scientist was still organizing it, and without it, I couldn't build the full filter system or test a prototype with users before our launch date.
- **Task**: Instead of waiting for every field, I needed to find a way to keep moving and get a testable version in front of users on time.
- **Action**:
  1. First, I did competitive research. We already pulled ad data from Meta, TikTok, and Google's ad libraries, so I studied how those platforms structure their filters and search, and how they surface ads. I also analyzed Magic Brief, one of our direct competitors. None of them was built for our exact job, which is finding the right reference for a specific creative brief. That showed me which filters were table stakes and where we could go deeper.
  2. Then I broke the problem down. I divided the filters into three layers. The first covered core attributes: media type, brand, industry, client, campaign theme, and destination. The second covered more specific details, like video type, music, and script. The third covered the ad's content, such as the hook and summary.
  3. Next, I worked with our data scientist and engineer to prioritize the data behind the six core filters our strategists needed most, rather than trying to gather everything at once.
  4. I made a deliberate trade-off on personalization. Every strategist has their own search logic, especially senior strategists. Once they find a filter combination that surfaces the most relevant, most reusable ads, they want to use it again. Supporting that properly means personalized search, which calls the API over and over and gets expensive fast. For an MVP, that cost wasn't worth it. So we left personalized filters and a more refined recommendation formula out, giving up roughly 10% of the customization early adopters wanted in order to hit the timeline. As a middle ground, we let the two or three VPs define their own custom filters, since they were the heaviest users of saved search logic and the cost stayed small.
  5. I made that call because the first question we needed to answer was simple: does the core search experience actually help strategists find relevant ad references? A narrower version let us test that sooner.
- **Result**: We launched a lightweight, testable version on the MVP timeline without being blocked by every missing data point. Then we used strategists' feedback to decide which advanced filters to build next.
- **Learning**: When you hit a technical blocker, the solution isn't always to solve every problem at once. It's about figuring out what's essential, answering the most important question first, and keeping the product moving.

面试提示：

- 两版里核心筛选项不一样：第一版是 brand、industry、client、media type、destination，第二版是 industry、brand、campaign themes，而且把 media type 放在后面。已确认：第一层是 media type、brand、industry、client、campaign theme、destination 六个。你的第一版原稿里写的是"五个"，练习时记得改成六个。
- 可能被追问："10% 是怎么算的？" 如果是估算，就直接说是根据早期用户需求清单估的。
- 可能被追问："你的 filter 是怎么设计出来的？" / "你们的竞品是谁？" 就讲竞品研究：Meta、TikTok、Google 的广告库是我们的数据来源，你研究了它们的 filter 和搜索逻辑；Magic Brief 是直接竞品。重点说结论：它们都不是为"按 brief 找参考"这件事设计的，所以前三层 filter 里哪些是基本盘、哪些是我们的差异点。【准备一个具体例子：哪个 filter 是从竞品学来的，哪个是它们没有的。】
- 如果被问到有没有用过投放后台：可以说用过 Meta / TikTok / Google 的投放后台，但你的主要工作是做内部工具，所以对后台的理解主要用在"广告数据长什么样、投放团队怎么找素材"上。
- 可能被追问：上线后用户反馈让你加了哪个筛选项？有例子的话加到 Result 里，故事会更完整。

## S01-04 TubeScience: Aligning the CEO on a text-first MVP

适合回答：Tell me about a time you disagreed with leadership / how you manage stakeholders / a time you pushed back with data / how you balance user needs and business goals

- **Situation**: At my current company, leadership's expectations and users' actual needs were slightly different. Our CEO had a strong vision for a video feature. He wanted to help creative strategists find winning ads and turn ideas into video prototypes as quickly as possible, and he assumed strategists needed full video prototypes to evaluate ad ideas.
- **Task**: I needed to figure out what users actually needed, and get leadership aligned on the right first version.
- **Action**:
  1. I talked directly with our users. I found that they didn't need a fully produced video to evaluate an idea. A simple text script was often enough to judge whether an idea was worth investing in.
  2. I validated this at different levels. First, I talked with our VP of Creative Strategy, who confirmed that script-first is how the team reviews ideas. Then I talked with junior and mid-level strategists, and they said the same thing.
  3. So I decided to narrow the product direction: start with lightweight, text-based scripts, and build the video workflow later.
  4. Then I brought it to our CEO. He had a strong vision for the video feature, so I knew just saying no wouldn't work. I made my case with three points. First, I brought in user evidence from someone he trusted: our VP of Creative Strategy confirmed that script-first is how every strategist on the team works, from junior to mid-level, so it wasn't just my opinion, it was a validated workflow. Second, I didn't say no to his idea. I proposed we start with a lightweight version and add video on top later, once we knew it was needed. Third, I showed him the engineering reality. Building video from zero would have required pulling an extra engineer off other work, while scripts could build on functions we already had, so we could ship much sooner. That made it an easy yes: same goal, faster path, lower cost.
- **Result**: He agreed, and we launched the script version in 3 weeks. It cut the time to find references from 3.5 hours to 5 minutes, and we rolled it out to 180 people.
- **Learning**: Good product judgment is about finding the simplest solution that delivers meaningful user value while still supporting the business goal.

面试提示：

- 你原稿开头是 "a product I worked on at my previous company"，但你现在还在 TubeScience。我改成了 "my current company"，如果你在面试时已经离开了，再改回来。
- 同样把 "review hours" 改成了 "the time to find references"，和简历保持一致。
- 原稿里"CEO 假设需要视频"这段说了两遍，Learning 也重复了一句，我都合并了。
- 这个故事和 S01-01 都提到 video → text。如果一场面试里两个都讲，S01-01 里这一点一句带过就好。
- 可能被追问："What if the CEO had said no?" 提前想好，比如会提议先小范围测试两个方向。

## S01-05 TubeScience: Keeping my manager in the loop while he was away

适合回答：How do you manage up / tell me about your working style / how do you communicate with stakeholders / a time you worked through constant change or ambiguity

- **Situation**: When I joined my current company, my manager went on vacation almost right away, so I had very little onboarding. Before he left, he gave me a project to own. But while he was away, leadership kept changing the project's direction. Over about two weeks, the MVP direction changed around eight times. At the same time, two new engineers, a new VP, and a new CTO joined the team.
- **Task**: I wanted to keep my manager in the loop without interrupting his vacation, so he wouldn't come back to a project he no longer recognized.
- **Action**:
  1. Every two days, I sent him a super short update with the same five parts: what's happening, what I did, what's blocking me, what support I need from him, and my next step.
  2. I kept it consistent on purpose. If he was busy, he only had to read one line: what support I needed from him. If he had time, he could see the full picture.
  3. Together, the updates also became a record of every direction change and why it happened.
- **Result**: When he came back, he didn't need to catch up with everyone one by one. He already knew where the project stood, why the direction had changed, and who the new people were. So he could go straight into aligning with the CEO and the new leaders, and the project kept moving instead of pausing for a week of catch-up.
- **Learning**: Managing up isn't about reporting everything. It's about giving your manager exactly the context they need to lead, even when they're not in the room.

面试提示：

- 原稿写的是 "my last company"，和 S01-04 一样改成了 "my current company"。
- "两周内方向变了 8 次"这个细节很有画面感，同一个故事也能回答 "how do you handle ambiguity or changing priorities"。
- 可能被追问：方向变了 8 次，你自己是怎么应对的？有没有主动推动定下来？可以接到 S01-04（说服 CEO 收窄方向）。
- 五段式汇报模板可以当作你的"工作方式"来讲，回答 "what's your working style" 时很具体。

## S01-06 TubeScience: How I build trust

适合回答：Tell me something that's not on your resume / how do you build trust / how do you work with engineers / tell me about working with a hesitant teammate / a time you went beyond your role

- **Opening**: Something that's not on my resume is how I build trust. I genuinely care about the people I work with, whether they're users, teammates, or leadership, and that's often what makes the product work.
- **Situation**: When I joined my current company, I was the youngest person on the team, and I was given one of the hardest projects. Many of my engineers were decades older than me, and at first, they were understandably hesitant about what a young PM could bring.
- **Action**:
  1. Instead of trying to prove myself right away, I set up one-on-ones with each engineer I worked closely with.
  2. I learned their domain knowledge and how they liked to work, included them in every key discussion, and took their opinions seriously. We also had lunch together almost every day.
  3. I also try to help beyond my scope. I was the only person on the team with a design background, so when a colleague building an internal recruiting tool got stuck on design, I helped him almost every morning, even though it wasn't my project.
- **Result**: Over time, the engineers went from hesitant to proactively sharing ideas and raising concerns early, which made our product decisions much better.
- **Learning**: I believe products are built by people, and when people trust each other, the work moves faster.

面试提示：

- 原稿写的是 "my last company"，已经改成 "my current company"。
- 之前那版 Spark 的故事（"first product designer"）和简历对不上，已经用这一版替换掉了。
- 想更有说服力的话，Result 可以加一个具体例子：某个工程师主动提前提出的风险或想法，改变了什么决定。
- 这个故事和 S01-05（manager 不在时定期汇报）可以一起用来回答 "what's your working style"：一个讲向上沟通，一个讲和同事建立信任。

## S02-01 Dreamwriter: AI 内容日历，WAU +8%

适合回答：Tell me about a 0-to-1 product / how you identified a user need / how you validated an idea before building / product strategy

- **Situation**: Dreamwriter is a B2B2C AI content platform. We help small business sales and marketing teams create content for their own clients. We had over 2,000 users, but fewer than 200 were active in a given week.
- **Task**: When I talked to our users, I kept hearing the same pattern. These are busy salespeople. They know they need to keep sending content to their clients to stay in touch, but every time they had to start over: What did I send last time? What should I send next? How often? In what format? My goal was to turn Dreamwriter from a tool people opened once in a while into something that fit into their weekly workflow, because it saved them real time.
- **Action**: I did three things.
  1. First, I designed the product. When users sign up, they fill out a short goal-capture form. Based on their answers, AI generates a personalized content plan, such as a one-pager in week 1, a checklist in week 2, and a case study in week 4. Then the product automatically creates each piece following that plan. So if the calendar says "digital book in week 3," the digital book is already generated and ready to send. Every user gets a different plan. A SaaS seller mostly needs emails to drive free trials, while an insurance agent needs richer content, like a digital book explaining a policy.
  2. Second, I tested it before we built it. I made a simple Google Form and sent it to about 40 users. I put their answers into a prompt, had AI generate a plan for each of them, and asked for their feedback.
  3. Third, I fixed what didn't work. The first plans were too generic, because our questions were too generic. We asked "Who is your target audience?" and got answers like "small businesses." So we made every question specific, like "What are your clients' job titles and industry?" After a few rounds, the plans felt truly personal, and I worked with an engineer to build it into the product.
- **Result**: In the month after launch, weekly active users grew 8%. Since our base was small, I treated it as an early signal rather than proof, but it showed that automating planning and creation brought users back.
- **Learning**: The quality of what AI generates depends on the quality of what you ask the user. Now I test the inputs cheaply before investing in the build.

如果你更喜欢原来的结尾（I took a repetitive, time-consuming task off their plate...），可以用它做总结句，再接上面这句 Learning。

可以更好的地方：

- "把 8% 当作早期信号"这句很加分，体现了数据判断力，一定要保留。
- 原来的 Learning 是在复述结果，我已经换成了你学到的东西。如果不像你会说的话，可以直接改。
- 面试官可能追问：你怎么判断 WAU 增长是这个功能带来的？有没有对照组？

## S02-02 Dreamwriter: Onboarding 改版，付费转化 +13.5%

适合回答：A time you used data to make a decision / how you handled an ambiguous problem / how you prioritize / tell me about an experiment you ran

- **Situation**: Dreamwriter is a B2B2C AI content platform for small business sales and marketing teams. Users liked the product, but most free users dropped off in the first week, and very few upgraded to paid.
- **Task**: I owned our automated onboarding in HubSpot, and my goal was to improve engagement and paid conversion.
- **Action**:
  1. I started with the data on our four automated emails: Day 1, 7, 18, and 30. People opened them, but they didn't take any action. Day 1 had the highest open rate, around 40%, but also the highest unsubscribe rate, because our first email asked users to upgrade before they had created anything. Day 18 had no clear call to action. It was a long list of features, and the only button was buried at the very bottom.
  2. So I shifted the strategy from early monetization to progressive education.
  3. I started with Day 1 and Day 18, since they had the most potential impact. I rewrote each email around one easy next step. Day 1 went from "Upgrade now" to "Create your first document in 5 minutes."
  4. Then I A/B tested the messaging, the order of the emails, and how often we sent them.
- **Result**: CTR went up 11%, sign-ups rose 4%, and paid conversion went up 13.5%.
- **Learning**: We were asking users to pay before they had seen any value. Once I let them succeed first, they were much more willing to upgrade.

可以更好的地方：

- 这个故事很完整，是你最强的数据驱动故事。
- 面试官可能追问：为什么没先改 Day 7 和 Day 30？实验跑了多久、样本多大？提前准备一句话的回答。
- 同一个故事也能回答"a time you challenged the status quo"：公司原来的策略是尽早变现，你用数据证明了这条路走不通。

## S03-01 Adobe: Spotting a mismatch between growth strategy and customer segments

适合回答：Tell me about a time you took initiative / identified an opportunity no one asked you to find / used data to shape strategy

- **Situation**: During my master's at Berkeley, I joined a co-op program with Adobe. My co-op lead was a PM at Adobe, and Adobe's lead designers worked with us. I've used Creative Cloud for years, and I noticed something: people know Photoshop and Illustrator, but many don't realize these apps live on one all-in-one platform, Creative Cloud.
- **Task**: No one assigned this to me. I wanted to understand how Adobe could grow Creative Cloud subscriptions, and whether its strategy was targeting the right customers.
- **Action**:
  1. First, I read Adobe's last five years of annual reports. Digital Media is Adobe's largest business, and Creative Cloud is the largest part of Digital Media. Subscriptions make up the overwhelming share of revenue, so Creative Cloud subscriptions matter more than almost anything else.
  2. Second, I looked at usage data across about 160,000 companies that use Adobe. Companies with 10 to 50 employees were the most common users. Businesses under 50 employees made up 53% of customers and 71% of revenue. Mid-size companies were 34% of customers, and large enterprises were 13%.
  3. Third, I compared that to Adobe's stated strategy. Adobe said it wanted to target mid-size creative customers and grow its enterprise offering, but it had one broad goal, "grow subscriptions," with no plan tailored to each segment. That was the mismatch.
- **Result**: I wrote it up as a growth strategy report and presented it to the Adobe PMs and designers in the program. It reframed the problem as: how do we make it easy for small and mid-size businesses to buy Creative Cloud? That became the basis for my purchase-flow redesign (S03-02).
- **Learning**: A goal like "grow subscriptions" isn't a strategy until you know who you're growing with. Segmenting first made every later design decision clearer.

面试提示：

- 开场就说清楚这是 co-op 项目，不要让面试官以为你是 Adobe 员工。主动发起本身就是这个故事的亮点。
- 可能被追问：这些公司分布数据是从哪里来的？提前准备一句数据来源。

## S03-02 Adobe: Redesigning the Creative Cloud purchase flow

适合回答：Tell me about a product you redesigned / how you used user research / how you validated a solution / a time your idea wasn't adopted

- **Situation**: Once I knew small and mid-size businesses were the biggest opportunity, I interviewed more than 20 design teams at small, mid-size, and large companies across North America, China, and Melbourne, focusing on the people who actually buy software for their team. Then I mapped Creative Cloud's end-to-end purchase flow, and it was very messy.
- **Task**: My goal was to make it easy for SMBs to find the right plan and finish buying, without getting lost.
- **Action**: I found four main problems and redesigned the flow around them.
  1. **No user-type routing.** Users were pushed to "Buy now" or "Free trial" before the product knew who they were, and the flow defaulted to an individual plan. A business buyer could end up on the wrong plan. In my prototype, users choose their scenario first: individual, business, students and teachers, or schools. Everything after that is personalized, with a clear step-by-step progress bar.
  2. **Subscription and payment were mixed together.** Many users didn't know the difference between a monthly plan, an annual plan paid monthly, and annual prepaid. I separated the two steps: choose the subscription first, then the payment. A timeline on the right shows when the free trial ends and exactly when and how much they'll be charged.
  3. **Team buyers couldn't assign seats easily.** After checkout, team buyers can now assign seats to each member by email and export the list to PDF for finance.
  4. **No way to recover from mistakes.** I added confirmations, like "You've selected a business plan. Is that correct?", and users can jump back to any earlier step. I also added a top banner explaining what Creative Cloud includes and that it has a free trial, plus bundles pairing low-usage apps with popular ones. Bundles show up in two places: grouped by use case when users pick a plan, and as an offer, like a free add-on, when they're about to finish subscribing.
  5. Finally, I wrote a PRD and tested the prototype against the original flow with more than 40 users, including the people I had interviewed.
- **Result**: In testing, time-to-purchase dropped by 37%, and the share of users who completed a purchase went up 15%. Before, many users said no to bundles, even free ones, because they didn't see how the apps fit their work. With use-case bundles, 9% more users accepted a bundle. Adobe didn't adopt the proposal at the time. But months later, Adobe launched a purchase flow that routes users by type first and added a top banner, very close to what I had proposed.
- **Learning**: Not every good idea gets adopted right away. What I can control is grounding it in data and user evidence. Seeing Adobe later ship a similar direction told me my read on the problem was right.

面试提示：

- 说 Adobe 后来上线的时候，用"a similar direction"，不要说"they used my idea"。面试官更看重你判断对了，而不是功劳归谁。
- 你提到的 "A/B testing" 其实是新旧流程的对比可用性测试，面试时建议说 "comparative usability testing"。如果被追问样本量，这样说更站得住。
- 这个故事很适合回答 "a time your idea was rejected"。

* 被问到样本量时，直接说 "about 40 users, so I treated it as directional evidence, not statistical proof"。和你在 Dreamwriter 里对 8% 的处理一样，这种说法很加分。也要想好 15% 是完成率提高了 15 个百分点，还是相对提高 15%。

## S04-01 Fabrica: Finding the problem through 80+ interviews

适合回答：Tell me about your user research process / how you identified an opportunity / a time you worked in a fast-paced, ambiguous environment

- **Situation**: At Berkeley, I joined Lean LaunchPad, a competitive, year-long startup program that works like a mini Y Combinator. Each team builds a company with investors and mentors. Every week, we had to interview customers, report to investors and mentors, and pitch our progress in public, and pivot if something didn't work. I was the youngest member of my team, and most of my teammates had fashion and e-commerce backgrounds.
- **Task**: We noticed that small and mid-size US fashion brands often source fabric and materials from manufacturers in Asia, especially China. My job was to figure out whether there was a real problem worth solving there.
- **Action**:
  1. We interviewed more than 80 brands and people across the industry: designers and sourcing teams from Nike, Alo Yoga, Converse, and Lululemon; independent designers and store owners in San Francisco, from Fillmore Street to shops in Saks and Macy's; sourcing agents who connect brands with suppliers; and classmates from Parsons with sourcing experience.
  2. We found three core pains. First, finding a reliable supplier depended almost entirely on personal connections. Second, fabric has to be touched in person, so vetting stayed offline, and photos never matched the real thing. Third, once production started, communication was scattered across phone, email, and WeChat. There was no way to track status, and delays came with no warning, so designers sometimes had to fly over just to check progress.
  3. Big brands already have their own suppliers, so we focused on small and mid-size US brands, who feel these pains the most.
- **Result**: We sized the market at $59 billion and found no single platform that helps these brands find, compare, and work with reliable suppliers in Asia. That became Fabrica: a marketplace that bridges US SMB brands and vetted Asian suppliers.
- **Learning**: The most valuable insights came from asking how people actually do the work today, not whether they'd use our product. Every pain point we built around came from someone describing their real process.

面试提示：

- 开场说清楚这是 Lean LaunchPad 的创业项目。每周要访谈和 pitch，这个节奏本身就能体现你的执行力。
- 可能被追问：市场规模怎么算的？是 TAM 还是 SAM？提前准备一句来源。

## S04-02 Fabrica: Cutting a user group to sharpen the MVP

适合回答：Tell me about a time you pivoted / how you made a hard trade-off / how you scoped an MVP / tell me about a project that didn't succeed

- **Situation**: After our interviews, we decided to build a marketplace connecting US SMB fashion brands with suppliers in Asia. Our first plan was to serve three groups: brand designers and buyers, suppliers, and sourcing agents, the middlemen who help brands find suppliers.
- **Task**: As we scoped the MVP, I had to decide who it was really for and which features mattered most.
- **Action**:
  1. First, I questioned whether sourcing agents would ever use it. They make money by connecting brands with suppliers, so our product was a direct competitor to their business. They had no reason to adopt it.
  2. So we dropped sourcing agents as a user group and focused on brand designers and the people who buy materials. I checked this with classmates from Parsons who had sourcing experience, and they confirmed it was exactly what they were missing.
  3. Then we cut a second piece: production tracking. Our original idea was that after a brand picked a supplier, it could monitor every step on our platform, from samples to bulk production to delivery, and even shift part of an order to a backup supplier if there was a delay. But we learned it wouldn't work. Factory workers were unlikely to report progress on a platform, factories didn't want to expose their timelines to competitors, and decisions like delays or remakes still depended on designers seeing the work in person. So I cut it and focused the MVP on discovery: helping brands find the right supplier and start the first conversation.
- **Result**: We launched a discovery marketplace. Brands could filter suppliers in Asia by region, minimum order quantity, and fabric specs like fiber composition, weight, color, and texture. Then they could request samples and message suppliers directly about stock, lead times, site visits, and whether they'd take the order. We targeted an addressable base of about 155,000 brands and 12,000 suppliers, and the MVP got strong feedback from mentors and investors in a program that accepts teams from about 1,000 applicants. In the end, Fabrica didn't continue as a real company after the program.
- **Learning**: A feature only works if every side has a reason to use it. Sourcing agents had no reason to adopt us, and factories had no reason to report their progress. Asking "what's in it for them" early kept the MVP focused on the part we could actually make work.

面试提示：

- 一定会被问 "why didn't it continue?"。提前准备一个坦诚的答案，比如项目周期结束、团队去向不同、供应商侧冷启动太难等，再说你学到了什么。这比回避更加分。
- 155K / 12K 是可触达的数据库规模，不是平台用户。面试时说 "addressable"，不要说 "we connected"。

## S05-01 Cider: Personalized size recommendations

适合回答：Tell me about a product you launched / a time user research changed your solution / how you balance conversion and returns / a time your first idea was wrong

- **Situation**: Cider is a fast-growing DTC e-commerce company based in LA, selling apparel online to Gen Z women in more than 130 countries.
- **Task**: As the PM intern for the core shopping experience, my goal was to increase checkout conversion while reducing size-related returns.
- **Action**:
  1. First, I dug into the data: return reasons, customer reviews, and purchase behavior. Sizing uncertainty kept showing up as a top reason for both abandoned carts and returns. Many customers ordered two sizes of the same item, kept one, and returned the other, because they weren't confident about fit.
  2. At first, we thought the fix was a better size chart with more measurements and fit details. But when I talked to users, I realized the real problem wasn't missing information. It was how much effort it took to decide.
  3. So I launched a personalized size recommendation feature. Users enter their body measurements, and the system maps their profile against historical fit and return data to recommend the best size automatically. Instead of making customers guess from a complex chart, the product does the heavy lifting and just tells them their size.
- **Result**: After launch, purchase conversion went up 5%, and size-related returns dropped 7%. The feature was eventually rolled out across more than 130 markets.
- **Learning**: Better products don't always come from giving users more information or more advanced tools. What users really needed was confidence. Our job was to help them reach the right decision with less effort.

面试提示：

- 你原稿写的是 "As the PM"，但简历上是实习生。我改成了 "PM intern"，面试官会对照简历听，前后一致更安全。
- 可能被追问：推荐是怎么算出来的？你和谁合作（数据、工程）？是怎么测量转化提升的（A/B 测试还是上线前后对比）？
- "第一个想法是错的"这个转折很有价值，可以用来回答 "a time you were wrong"。

## S05-02 Cider: Redesigning the quality-inspection dashboard

适合回答：Tell me about an internal tool or B2B product you built / how you scoped a large problem / how you designed for users under time pressure / how user research shaped your solution

- **Situation**: At Cider, every item goes through quality inspection before it ships. Our inspection system supports 3 factories in the US and China and serves more than 130 markets. Inspectors check hundreds of items a day under time pressure and decide what ships and what gets rejected. Their records also feed supplier evaluations and downstream reports. But the logging was messy, so we couldn't tell which batches had the most defects, or whether a return came from a quality issue or something else.
- **Task**: I was the PM on the quality-inspection dashboard, working with 3 engineers, a content designer, and a UX researcher. My goal was to turn a manual, inconsistent process into a standardized, objective inspection system, so that every inspector logs defects the same way and the data can be trusted downstream.
- **Action**:
  1. **Research.** I spent about a week interviewing 2 operations managers and 4 warehouse inspectors, about 30 minutes each. Inspectors work on their feet with a tablet, rotate across product types, and multitask: inspecting, filling forms, packing, and running machines at the same time. They have no time to learn a complex system.
  2. **Scoping.** The workflow had several steps: scan the order, scan the SKU, recheck inventory, log non-conforming item data, and complete. The non-conforming data step had the most manual input and the most errors. Within it, I focused on appearance checks, because appearance is one of the biggest drivers of returns.
  3. **Problems.** I found four. The issue-type list had about 20 options with no hierarchy, so it was hard to scan. Severity was a free-text box, so everyone described it differently, and many skipped it. Notes were free text too, and hard to match to a specific defect. And there was a single photo upload button, so no one knew which photo belonged to which defect.
  4. **Solution.** First, I turned the flat list into a two-tier taxonomy: inspectors pick a primary category, like color, stitching, or finishing, then a specific issue. Second, and most important, I replaced free-text severity with three labels, minor, moderate, and critical, each with a visual cue and a short definition, so inspectors choose instead of describe. We reused existing label components, so engineering cost was low. Third, I made notes and photos map one-to-one to each defect. The new flow is: pick the issue, one click for severity, add a note if needed, and attach a photo to that exact defect.
- **Result**: Inspection time dropped 45%, saving an inspector about 27 minutes per batch and 88 hours per week in total. Quality-related returns dropped 4%. Because severity was now graded the same way everywhere, the defect data became consistent enough to use for supplier evaluation. The tool rolled out to serve customers in more than 130 countries, and inspectors told me they could finish checks much faster without constantly typing.
- **Learning**: Internal tools need deep domain knowledge. A dashboard like this is really about data, so you have to understand how the data is collected and who uses it downstream. Only then can you see the real product problem.

面试提示：

- 三级严重程度这个设计是故事的核心，可能被问"为什么是 3 级而不是 5 级"。可以说在时间压力下，少一个选项就少一种分歧。
- 你提到的 smart note suggestions 没有做完，可以当作"如果继续做会做什么"来讲，体现你想得更远。
- 你是实习生，但这是你自己负责的一整块。开场说清楚 scope："I owned the appearance-check redesign within the inspection dashboard"。

* 讲这个故事时先说产品层面的意义："把一个靠人工、不一致的流程变成标准化、客观的系统"，再讲具体的分级和照片对应。细节是证据，不是重点。
