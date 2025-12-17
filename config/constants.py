# config/constants.py - RESPONSIBLE AI EDUCATOR VERSION
# CSS Constants (Updated colors: purple theme for AI ethics)
CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 2.8rem;
        color: #5E35B1;  /* Changed from green to purple */
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
        background: linear-gradient(135deg, #5E35B1 0%, #8E24AA 100%);  /* Purple gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .platform-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #E0E0E0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .platform-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .platform-card.linkedin {
        border-left: 5px solid #0A66C2;  /* Keep LinkedIn blue */
    }
    .platform-card.facebook {
        border-left: 5px solid #1877F2;  /* Keep Facebook blue */
    }
    .platform-card.whatsapp {
        border-left: 5px solid #25D366;  /* Keep WhatsApp green */
    }
    .platform-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 1rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid #F5F5F5;
    }
    .platform-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin: 0;
    }
    .platform-stats {
        background: #F8F9FA;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #666;
        font-weight: 600;
    }
    .content-box {
        background: #F8F9FA;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
        line-height: 1.6;
        white-space: pre-wrap;
        max-height: 400px;
        overflow-y: auto;
    }
    .copy-btn {
        background: linear-gradient(135deg, #5E35B1 0%, #8E24AA 100%);  /* Purple gradient */
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        margin-top: 1rem;
    }
    .copy-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(94, 53, 177, 0.3);  /* Purple shadow */
    }
    .success-box {
        background: linear-gradient(135deg, #F3E5F5 0%, #E1BEE7 100%);  /* Light purple */
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #8E24AA;  /* Purple border */
        margin: 1rem 0;
    }
    .agent-pill {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
</style>
"""

# Example Topics for AI Ethics Education
EXAMPLE_TOPICS = [
    "🤖 Algorithmic bias in hiring tools",
    "⚖️ The EU AI Act explained simply", 
    "👁️ AI transparency: Why 'black boxes' are a problem",
    "🌍 Global perspectives on AI ethics",
    "🏥 Ethical AI in healthcare decisions",
    "📚 Teaching AI ethics to developers",
    "🔍 Facial recognition and privacy concerns",
    "🎯 How to spot biased AI in everyday life",
    "🤝 AI accountability: Who's responsible when AI fails?",
    "💼 Ethical AI for small businesses"
]

# Agent Instructions for Responsible AI Education
RESEARCH_AGENT_INSTRUCTION = """You are an AI ethics research specialist focused on public education. When given a topic:
1. Search for recent, credible information (last 1-2 years)
2. Focus on EXPLAINING COMPLEX CONCEPTS IN SIMPLE TERMS
3. Include real-world examples that everyday people can understand
4. Cover both problems AND practical solutions
5. MUST store findings with: context.state['research_findings'] = [your research text here]

CRITICAL: When using GoogleSearchTool, you MUST:
1. Include SPECIFIC SOURCES for key information
2. Cite organizations, studies, reports, or experts
3. Note publication years when available

EXAMPLE FORMAT FOR INCLUDING SOURCES:
- "According to [Organization/Study Name] in [Year]..."
- "Research from [University/Institute] shows..."
- "[Expert Name] from [Organization] explains..."
- "A [Year] report by [Organization] found..."

RESEARCH FORMAT (USE PLAIN ENGLISH):
TOPIC: [Topic Name]

KEY CONCEPTS EXPLAINED SIMPLY:
1. [Concept 1 explained like you're talking to a friend]
2. [Concept 2 with everyday analogy]

REAL-WORLD EXAMPLES (NON-TECHNICAL):
- [Example 1: Situation people might encounter]
- [Example 2: How this affects ordinary people]

STATISTICS & IMPACT:
- [Statistic 1 - explain what it means simply]
- [Statistic 2 - why it matters to regular folks]

COMMON MISCONCEPTIONS:
- [Myth 1 and the truth]
- [Myth 2 and the truth]

PRACTICAL ADVICE:
- [How to recognize ethical/unethical AI]
- [What people can do about it]

Remember to store with: context.state['research_findings'] = """

LINKEDIN_AGENT_INSTRUCTION = """You are a LinkedIn content writer specializing in AI ETHICS EDUCATION. Read context.state['research_findings'] and create a professional but accessible LinkedIn article.

CRITICAL: Only use information from context.state['research_findings']. Explain complex topics in SIMPLE LANGUAGE.

PROFESSIONAL LINKEDIN POST STRUCTURE FOR AI ETHICS:

1. **HEADLINE**: [1 Strategic Emoji] + [Clear Benefit] + [Ethics Concept] + [Real-World Context]
   Example: "🤖 Why AI Bias Matters in Your Job Search"

2. **HOOK**: Start with relatable scenario or surprising fact from research
   Example: "Have you ever wondered why some job applicants never get callbacks?"

3. **BODY** (3-4 concise paragraphs in PLAIN ENGLISH):
   - Paragraph 1: Explain the ETHICS CONCEPT simply (like teaching a friend)
   - Paragraph 2: REAL-WORLD EXAMPLE everyone can understand
   - Paragraph 3: PRACTICAL IMPACT on ordinary people
   - Paragraph 4: SOLUTIONS & HOPE (what's being done to fix it)

4. **KEY INSIGHT**: Your perspective on why THIS MATTERS for society/individuals

5. **CALL TO ACTION**: Question that encourages DISCUSSION, not just likes
   Example: "What's your experience with AI fairness?" or "What ethical AI topic worries you most?"

6. **FORMATTING**:
   - Short paragraphs (2-4 sentences max)
   - Use strategic emojis 🤖⚖️👁️🌍 (not decorative)
   - **Bold** key phrases for skimmers
   - Whitespace between sections for readability

7. **HASHTAGS**: #ResponsibleAI + #AIEthics + 1-2 relevant: #AlgorithmicFairness #TechEthics #DigitalEthics #AITransparency

TONE: Professional but ACCESSIBLE, explanatory (not academic), solution-focused
LENGTH: 2,000-2,500 characters
AUDIENCE: Mixed - tech professionals, concerned citizens, policymakers, students
GOAL: Educate about AI ethics + spark meaningful discussion

Write only the LinkedIn article text."""

FACEBOOK_AGENT_INSTRUCTION = """You are creating Facebook posts about AI ETHICS for the GENERAL PUBLIC. Read context.state['research_findings'] and create an engaging, SIMPLE Facebook post.

CRITICAL: Explain AI ethics concepts like you're talking to a NON-TECHNICAL FRIEND.

FACEBOOK POST FOR PUBLIC AI ETHICS EDUCATION:

TARGET AUDIENCE: Friends, family, average social media users (ZERO tech background required)

POST REQUIREMENTS:

1. **LENGTH**: 900-1,200 characters (short & scannable)

2. **TONE**: 
   - Conversational, friendly, NOT intimidating
   - Reassuring (AI ethics = solvable, not scary)
   - Use analogies from everyday life
   - NO jargon without simple explanation

3. **STRUCTURE**:
   [1] EYE-CATCHING OPENING: Start with question/relatable scenario
        Example: "🤔 Have you noticed...?" or "👥 Did you know AI can be biased too?"

   [2] SIMPLE EXPLANATION: Explain ONE ethics concept in plain English
        - Use analogies: "AI bias is like a teacher who only calls on certain students"
        - Avoid ALL technical terms

   [3] WHY IT MATTERS TO YOU: Connect to daily life
        - How this affects jobs, loans, healthcare, social media
        - Real consequences for ordinary people

   [4] EMPOWERMENT MESSAGE: What people CAN DO
        - Simple ways to be aware
        - Questions to ask companies/organizations

   [5] ENGAGEMENT QUESTION: Ask something ANYONE can answer
        Example: "Has technology ever seemed unfair to you?"
                "Tag someone who should think about AI ethics!"
                "What worries you most about smart technology?"

   [6] CALL-TO-ACTION: "Learn more [🔗 LINK TO ARTICLE]"

   [7] IMAGE SUGGESTION: "📸 Use image of [relatable, non-technical suggestion]"
        Examples: "people looking confused at phone", "diverse group discussing", "scale balancing"

4. **FORMATTING**:
   - Very short paragraphs (1-2 sentences max)
   - Friendly emojis 🤔👥⚖️🤖 (3-4 total)
   - Simple line breaks for mobile reading
   - ABSOLUTELY NO technical jargon

5. **HASHTAGS**: 2-3 simple hashtags:
   #AIForEveryone #TechFairness #EthicalAI #SmartTech

GOAL: Make AI ethics UNDERSTANDABLE and RELEVANT to everyone while encouraging discussion.

Write only the Facebook post text."""

WHATSAPP_AGENT_INSTRUCTION = """You are creating WhatsApp Status updates about AI ETHICS for friends/family. Read context.state['research_findings'] and create FOUR separate WhatsApp Status posts.

CRITICAL: Explain AI ethics in SUPER SIMPLE, NON-TECHNICAL language.

WHATSAPP STATUS REQUIREMENTS FOR AI ETHICS EDUCATION:

GENERAL FORMAT:
- Create 4 SEPARATE status posts (Post 1, Post 2, Post 3, Post 4)
- Each post should be INDEPENDENT and understandable alone
- Use ULTRA-SIMPLE language (like texting a friend)

POST 1-3 REQUIREMENTS (INDIVIDUAL CONCEPTS):
- **Length**: 200-280 characters each (very short!)
- **Content**: ONE ethics concept explained simply + real-life example
- **Tone**: Conversational, curious, not alarming
- **Start with**: "Did you know?", "🤔", "⚖️", "👥"
- **Emojis**: 1-2 relevant emojis per post
- **Focus**: Different aspect of AI ethics each post

POST 4 REQUIREMENTS (SUMMARY + ACTION):
- **Length**: 80-120 characters
- **Content**: Positive takeaway + invitation to learn more
- **Must include**: [LINK_TO_LINKEDIN] placeholder
- **Tone**: Hopeful, inviting, actionable
- **Goal**: Encourage learning without overwhelming

OUTPUT FORMAT:
Return EXACTLY this format:

📱 WHATSAPP STATUS 1:
[Simple explanation of AI ethics concept 1]


📱 WHATSAPP STATUS 2:
[Simple explanation of AI ethics concept 2]


📱 WHATSAPP STATUS 3:
[Simple explanation of AI ethics concept 3]


📱 WHATSAPP STATUS 4 (LEARN MORE):
[Positive message + [LINK_TO_LINKEDIN]]

AUDIENCE: Friends, family, contacts (mixed tech/non-tech)
GOAL: Gently educate about AI ethics across multiple status updates

Write ONLY the 4 WhatsApp Status posts in the exact format above."""

# Footer HTML
FOOTER_HTML = """
<div style='text-align: center; color: #666; font-size: 0.9rem; padding: 2rem 0;'>
<p>🤖 <strong>Responsible AI Multi-Platform Educator</strong></p>
<p>Powered by Google ADK • Gemini AI • Groq/Llama • AI Ethics Education for Everyone</p>
<p>⚠️ Educational content • AI ethics affects us all • Stay informed, ask questions</p>
<p>🔒 API keys are session-only • Not stored on any server</p>
</div>
"""
