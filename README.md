# Research-on-Generative-AI-applications
Research on generative AI applications, implementation challenges, and terminology.
*Author: Assylzhan Toktassyn *

---

## Why I wrote this

When people hear "Generative AI", most of them think of ChatGPT writing essays.
While researching for this assignment, I found that the chat window is only a small part of it.
The real action is happening inside products: code editors, help desks, hospitals,
law firms and classrooms.

For each use case below I tried to answer four simple questions:

1. **Why would a business pay for this?** (business value)
2. **What makes it hard to build?** (technical challenges)
3. **Where does it break?** (weak points)
4. **Who is already doing it?** (existing implementations)

## Contents

1. [Coding Assistants](#1-coding-assistants)
2. [Customer Support Agents](#2-customer-support-agents)
3. [Enterprise Knowledge Assistants](#3-enterprise-knowledge-assistants)
4. [Marketing and Content Creation](#4-marketing-and-content-creation)
5. [Image and Video Generation](#5-image-and-video-generation)
6. [Healthcare Documentation](#6-healthcare-documentation)
7. [Legal Document Analysis](#7-legal-document-analysis)
8. [Education and Tutoring](#8-education-and-tutoring)
9. [AI Agents for Workflow Automation](#9-ai-agents-for-workflow-automation)
10. [Translation, Voice and Localization](#10-translation-voice-and-localization)

---

## 1. Coding Assistants

**Business value.** This is probably the most mature GenAI use case right now. A coding assistant
sits inside the developer's editor and suggests the next lines while you type. It can also explain
an unfamiliar function, write unit tests or refactor several files from one plain-language request.
For a company, the value is easy to see: developers spend less time on boilerplate and searching
documentation, and new team members understand an old codebase faster. Since developer time is
expensive, even a small productivity gain adds up quickly across a big team.

**Technical challenges and weak points.** The hardest problem is context. A real project has
thousands of files, but the model's context window is limited, so the tool has to decide which
files are relevant before it sends anything to the LLM. Speed also matters a lot: if a suggestion
takes more than a second, people stop waiting for it, so low latency during inference is critical.
The weak points are serious, though. Generated code can look clean and still contain bugs, use
outdated libraries or open security holes. The model can even hallucinate a package that doesn't
exist. Companies also worry about sending private source code to external servers. In my opinion,
the biggest risk is human: developers get used to pressing "Tab" without really reading the code.

**Existing implementations:**
- [GitHub Copilot](https://github.com/features/copilot) – an AI pair programmer built into popular editors that suggests code, answers questions and can work as an agent on GitHub issues.
- [Cursor](https://cursor.com) – an AI-first code editor that can make changes across many files from a single request.
- [Tabnine](https://www.tabnine.com) – a coding assistant focused on privacy that companies can run on their own infrastructure.

---

## 2. Customer Support Agents

**Business value.** Support was one of the first places where GenAI clearly paid for itself.
Instead of the old "press 1 for billing" bots, a modern AI support agent understands a question
written in normal language and finds the answer in the company's help center. It replies in
seconds, at 3 a.m., in many languages. Businesses can handle more requests without hiring more
people. Human agents stop answering "how do I reset my password?" all day and focus on the
complicated or emotional cases.

**Technical challenges and weak points.** Writing a polite answer is easy for an LLM. Writing a
*correct* one is the difficult part. The bot has to be grounded in up-to-date company documents
(usually through RAG), follow strict guardrails, and know when to hand the conversation to a
human. Weak points include hallucinated policies, trouble with angry or unclear customers, and
handling PII such as addresses or card details. There have already been real cases where a
chatbot promised a refund rule that didn't exist, and the company was held responsible for it.
Another risk is prompt injection: a user can try to trick the bot into ignoring its system prompt.

**Existing implementations:**
- [Intercom Fin](https://fin.ai) – an AI customer service agent that answers questions using a company's own help content and passes complex cases to humans.
- [Zendesk AI](https://www.zendesk.com/service/ai/) – AI agents and agent-assist tools built into the Zendesk support platform.
- [Sierra](https://sierra.ai) – a platform for building branded conversational AI agents that can also take actions, like processing returns.

---

## 3. Enterprise Knowledge Assistants

**Business value.** In any large company, knowledge is spread across emails, wikis, chats,
tickets and shared drives. Finding one answer can take half an hour. Knowledge assistants search
all of these sources at once and return a short answer with links to the original documents.
For the business, this means less time lost searching, faster onboarding, and knowledge that
doesn't disappear when an experienced employee leaves.

**Technical challenges and weak points.** I was surprised to learn that this is mostly a data
problem, not a model problem. Documents have to be split into chunks, turned into embeddings and
stored in a vector database so the system can find them by meaning, not just by keywords.
The most important part is permissions: an intern must never get an answer built from a
confidential HR file. When the source documents are outdated or contradict each other, the
answer is wrong too ("garbage in, garbage out"). Hallucinations still happen, so good tools
always show their sources and let the user check them.

**Existing implementations:**
- [Glean](https://www.glean.com) – a work AI assistant that connects to company apps and answers questions while respecting each user's access rights.
- [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/copilot) – an assistant built into Word, Outlook, Teams and Excel that works with a company's own files and emails.
- [Notion AI](https://www.notion.com/product/ai) – AI features inside Notion that search, summarize and answer questions across a team's workspace.

---

## 4. Marketing and Content Creation

**Business value.** Marketing teams use GenAI to write first drafts of blog posts, product
descriptions, ad variations, newsletters and social media posts. The blank page problem goes
away: you start with a draft and edit it. A team can quickly create twenty versions of an ad for
different audiences, test them and keep the best. Content that used to take a week can be ready
in a day.

**Technical challenges and weak points.** The main challenge is brand voice. Generic AI text is
easy to recognize, and it often sounds flat or over-excited. Tools address this with prompt
engineering, brand guidelines in the system prompt, and sometimes fine-tuning on the company's
past content. Settings like temperature control how creative or predictable the output is.
On the weak side: facts and numbers still need checking, copyright questions are not fully
settled, and the internet is filling up with similar, low-value content. If everyone uses the
same tools in the same way, everyone ends up sounding the same.

**Existing implementations:**
- [Jasper](https://www.jasper.ai) – an AI content platform for marketing teams that keeps writing consistent with a company's brand voice.
- [Canva Magic Studio](https://www.canva.com/magic/) – a set of AI tools inside Canva for generating text, images and designs.
- [Grammarly](https://www.grammarly.com) – a writing assistant that uses GenAI to rewrite, shorten or change the tone of text.

---

## 5. Image and Video Generation

**Business value.** Image and video models turn a text description into visuals: a product mockup,
a banner, a storyboard or a short clip. Designers can explore dozens of ideas in an hour instead
of a week, and small businesses get decent visuals without hiring a studio for every task.
Video generation is especially interesting for training and marketing, where filming is
expensive and content needs frequent updates.

**Technical challenges and weak points.** Most of these tools are built on diffusion models,
which start from random noise and gradually "clean" it into an image that matches the prompt.
Video is much harder than images because every frame has to stay consistent: the same face,
the same lighting, objects that don't randomly change shape. Generation also needs a lot of
expensive computing power. The weak points are partly technical (strange hands, broken text
inside images, physics that looks wrong) and partly ethical. Some models were trained on artists'
work without permission. Deepfakes make it easy to create convincing fake videos of real people,
which is a big risk for elections, fraud and reputation.

**Existing implementations:**
- [Adobe Firefly](https://firefly.adobe.com) – Adobe's family of generative models, trained on licensed content and built into Photoshop and other Creative Cloud apps.
- [Midjourney](https://www.midjourney.com) – an image generator known for its artistic and highly detailed style.
- [Runway](https://runwayml.com) – a creative platform for generating and editing video with AI.

---

## 6. Healthcare Documentation

**Business value.** Doctors spend a surprising part of their day typing notes instead of looking
at patients. AI "scribes" listen to the doctor–patient conversation (with consent), transcribe
it, and turn it into a structured clinical note. Hospitals use them because they reduce burnout,
save hours of paperwork every week, and let doctors focus on the person in front of them.
I think this is one of the most "human" uses of GenAI: the technology gives people more time
for each other.

**Technical challenges and weak points.** This is a multimodal problem. The system has to turn
speech into text, understand medical terms and different accents, ignore background noise, and
then summarize the conversation correctly. Mistakes are dangerous: a wrong dose or a missed
allergy in a note can harm a patient. That's why human-in-the-loop review is required here.
The doctor must read and approve every note. Patient data is among the most sensitive data
there is, so privacy laws and security are a huge part of the work. A quieter risk is
"automation bias": after a hundred correct notes, a tired doctor may stop checking the hundred
and first one.

**Existing implementations:**
- [Abridge](https://www.abridge.com) – an AI platform that turns medical conversations into clinical notes and links each statement back to the original audio.
- [Microsoft Dragon Copilot](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot) – Microsoft's clinical assistant for voice dictation, ambient listening and automatic note creation.

---

## 7. Legal Document Analysis

**Business value.** Legal work involves reading a lot: contracts, case law, regulations, due
diligence files with thousands of pages. GenAI can summarize documents, compare contract versions,
find risky clauses and draft standard documents in minutes. For law firms and legal departments,
this means junior lawyers spend less time on repetitive review and more on actual legal thinking,
and clients get answers faster.

**Technical challenges and weak points.** In law, one wrong citation can ruin a case. LLMs have
already hallucinated court cases that never existed, and lawyers who submitted them without
checking were fined. Legal AI tools therefore depend heavily on grounding: every answer has to be
tied to a real, verifiable source. Long documents push against the context window, and legal
language is very precise, so a "small" paraphrase can change the meaning. Confidentiality is
critical too, because client documents cannot leak. Evaluation is also difficult: deciding if a
legal summary is "good" usually takes an expert, which makes testing slow and expensive.

**Existing implementations:**
- [Harvey](https://www.harvey.ai) – a GenAI platform built for law firms for research, contract analysis and drafting.
- [CoCounsel](https://www.thomsonreuters.com/en/cocounsel) – Thomson Reuters' AI assistant for legal research and document review, grounded in its legal databases.
- [Spellbook](https://www.spellbook.legal) – an AI tool inside Microsoft Word that helps lawyers draft and review contracts.

---

## 8. Education and Tutoring

**Business value.** Good private tutors are expensive, and teachers can't give individual
attention to thirty students at once. An AI tutor can explain the same topic five different
ways, give hints instead of answers, and adapt to the student's level, at any time. For education
companies, this makes personalized learning possible at scale. Teachers also use it to prepare
lesson plans, quizzes and feedback faster.

**Technical challenges and weak points.** A good tutor should *not* simply give the answer,
so the system prompt has to guide the model carefully to ask questions and let the student think.
The model can still explain something incorrectly with full confidence, and a beginner can't
tell the difference. That's the most dangerous kind of hallucination. Schools also worry about
cheating, children's data privacy, and students depending on AI instead of building their own
thinking skills. From my own experience as a student, AI helps most when I use it to check my
understanding, not to skip the learning part.

**Existing implementations:**
- [Khanmigo](https://www.khanmigo.ai) – Khan Academy's AI tutor that guides students with questions instead of giving away answers.
- [Duolingo Max](https://blog.duolingo.com/duolingo-max/) – a Duolingo subscription with AI features like "Explain My Answer" and roleplay conversations.
- [NotebookLM](https://notebooklm.google) – a Google tool that answers questions only from the sources you upload and can create study guides and audio overviews.

---

## 9. AI Agents for Workflow Automation

**Business value.** This is the newest and probably most hyped use case. An AI agent doesn't
just answer a question. It plans steps and takes actions: reading an email, checking a CRM,
creating a ticket, updating a spreadsheet and sending a reply. Businesses see a chance to
automate whole processes that used to need a person clicking between ten different systems,
such as invoice processing, lead qualification or IT requests.

**Technical challenges and weak points.** Agents work through tool calling: the LLM decides which
tool or API to use and with what parameters. Every extra step is another place where something
can go wrong, and errors pile up. A model that is right 95% of the time per step becomes
unreliable over a ten-step task. Agents can get stuck in loops, call the wrong tool, or take an
action that can't be undone. Security is a big concern. If an agent reads a malicious email,
prompt injection can make it do things the user never asked for. That's why good agent systems
use strict permissions, logs, guardrails and human approval for risky actions. Right now, agents
seem to work best on narrow, well-defined tasks, not as "do everything" assistants.

**Existing implementations:**
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) – a low-code platform for building custom AI agents connected to business data and tools.
- [n8n](https://n8n.io) – a workflow automation tool where AI agents can be combined with hundreds of app integrations.
- [Zapier Agents](https://zapier.com/agents) – AI agents that can act across thousands of apps connected through Zapier.

---

## 10. Translation, Voice and Localization

**Business value.** Companies that sell globally need their websites, apps, videos and support
in many languages. GenAI translation sounds much more natural than older machine translation,
and voice models can now dub a video into another language while keeping a similar voice.
This makes localization much cheaper and faster. A small company can reach international
customers without a full translation team.

**Technical challenges and weak points.** Translation is more than swapping words. Idioms,
humor, politeness levels and cultural context are hard to get right. As someone who uses more
than one language every day, I notice that AI sometimes translates "correctly" but still sounds
unnatural. Specialized terminology in medical, legal or technical text needs extra care or
fine-tuning. Voice cloning raises serious ethical questions: the same technology that dubs a
training video can be used to fake someone's voice in a phone scam. Responsible tools require
consent and add protections against misuse.

**Existing implementations:**
- [DeepL](https://www.deepl.com) – an AI translation service known for natural-sounding results, with tools for business documents.
- [ElevenLabs](https://elevenlabs.io) – an AI voice platform for text-to-speech, voice cloning and video dubbing.
- [HeyGen](https://www.heygen.com) – a tool for creating AI avatar videos and translating videos with lip-sync.

---

## Summary Table

| # | Use case | Maturity (my opinion) | Biggest risk |
|---|---|---|---|
| 1 | Coding assistants | 🟢 High | Insecure or buggy code accepted without review |
| 2 | Customer support | 🟢 High | Hallucinated policies and promises |
| 3 | Knowledge assistants | 🟡 Medium | Permission leaks, outdated sources |
| 4 | Marketing content | 🟢 High | Generic content, unchecked facts |
| 5 | Image and video | 🟡 Medium | Deepfakes and copyright |
| 6 | Healthcare documentation | 🟡 Medium | Errors in medical notes |
| 7 | Legal analysis | 🟡 Medium | Fake citations, confidentiality |
| 8 | Education | 🟡 Medium | Confident wrong explanations, over-dependence |
| 9 | AI agents | 🔴 Early | Error accumulation, prompt injection |
| 10 | Translation and voice | 🟢 High | Cultural mistakes, voice fraud |

---

## Conclusion

After going through all ten cases, I see the same pattern again and again. GenAI is very good at
producing a fast *first version* of something: code, an answer, a picture, a note, a translation.
It is much weaker at guaranteeing that this version is correct.

Three things show up in almost every successful product:

1. **Grounding in trusted data.** The best tools don't rely only on what the model "remembers".
   They connect it to real documents through RAG and show their sources.
2. **A human in the loop.** In serious areas like medicine, law or money, a person still makes
   the final decision.
3. **Guardrails and evaluation.** Companies that test their systems properly and limit what
   the AI is allowed to do avoid the embarrassing headlines.

My personal takeaway: the important skill isn't "using AI". It's knowing *when to trust it and
when to double-check*. That is what I want to learn during this course.

---

## How this report was made

- Research: DIAL AI chat for collecting ideas and product names; official product websites for checking facts and links.
- Writing: the structure and conclusions are my own; AI-assisted drafts were rewritten and edited manually.
- Terms used in this report are explained in [vocabulary.md](vocabulary.md).
